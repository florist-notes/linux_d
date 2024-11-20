# ROOFLINE MODELING:

[ code ] Walkthrough : [[ PRoof ](https://github.com/PRoof-framework/PRoof)]

### main.py :

```python
from typing import List
from pathlib import Path
from dataclasses import asdict
import os
import sys
import tempfile
import json
import argparse
import logging

import coloredlogs

import model.backend
from context import PerfContext
from util import TMPDIR

log = logging.getLogger(__name__)


def _get_batch_size_list(batch_size_arg: str) -> List[int]:
    if '-' in batch_size_arg:   # range
        min_b, max_b = map(int, batch_size_arg.split('-'))
        assert min_b > 0
        assert max_b >= min_b
        assert min_b & (min_b - 1) == 0
        assert max_b & (max_b - 1) == 0
        li = [min_b]
        while li[-1] < max_b:
            li.append(li[-1] * 2)
        assert li[-1] == max_b
        return li
    elif ',' in batch_size_arg:
        li = list(map(int, batch_size_arg.split(',')))
        assert all(b > 0 for b in li)
        return li
    else:   # number
        batch_size = int(batch_size_arg)
        assert batch_size > 0
        return [batch_size]

```

+ `from typing import List`: Enables the use of type hints like List[int] for clarity and type checking.
+ `from pathlib import Path`: Provides tools to handle filesystem paths in an object-oriented way.
+ `from dataclasses import asdict`: Converts a dataclass instance to a dictionary.
+ `import os, sys, tempfile, json, argparse, logging`:

    + Provides utilities for: 
        - Operating system interactions (os),
        - System-specific parameters and functions (sys),
        - Temporary file creation (tempfile),
        - JSON parsing and serialization (json),
        - Command-line argument parsing (argparse),
        - Logging for debugging and information (logging).

+ `import coloredlogs`: Adds colors to log messages for better readability.
+ `import model.backend`: Presumably imports the application's backend logic.
+ `from context import PerfContext`: Imports a custom context object, possibly used for performance tracking.
+ `from util import TMPDIR`: Imports a utility constant, likely representing a temporary directory path.
+ `log = logging.getLogger(__name__)`: Creates a logger named after the current module to record log messages.

Function: `_get_batch_size_list(batch_size_arg: str) -> List[int]`

Purpose:
This function takes a string argument (batch_size_arg) and returns a list of integers representing batch sizes. It supports three input formats:

+ A range: min-max (e.g., 4-64).
+ A comma-separated list: val1,val2,... (e.g., 4,16,32).
+ A single number: value (e.g., 32).


Class: _HelpFormatter

Purpose: This custom help formatter enhances the default argparse help formatting by improving line splitting when displaying help messages.

```python
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog = "PRoof",
        description = "PRoof is designed to be a universal, end-to-end, fine-grained AI model inference performance analysis and hardware AI benchmark tool",
        epilog = "for each model backend, it may contains it's own additional options (via -o), use '-B <backend> -o help' to view it's help",
        formatter_class=_HelpFormatter)

    parser.add_argument('-v', '--verbose', action='store_true', help="will set log_level to logging.DEBUG\n")
    parser.add_argument('-s', '--subjects', default='', help="test subjects to run, prefix means all sub subjects, empty value means all, available: %s" % PerfContext.list_subjects())
    parser.add_argument('-f', '--output', default="report.json", help="output file contain all test result\n")

    parser.add_argument('-B', '--model-backend', default='trtexec', help="backend to run model", choices=model.backend.get_available_backends())
    parser.add_argument('-D', '--data-width', default='32,32', help="specify data width for model analyze, format 'onnx,backend', \
        fp32 = 32, fp16 = 16, should same as data in onnx model and actual used in backend (e.g. in converted model)", type=str)
    parser.add_argument('-o', '--backend-options', default='', help="options passed to backend\n", type=str)

    parser.add_argument('-m', '--onnx-model', default='', help="[model] onnx format model to test")
    parser.add_argument('-b', '--batch-size', default='1', help="[model] specific or range of batch_size to test, like '4' or '1-16'")
    parser.add_argument('-r', '--repeat', default=10, help="[model] repeat count", type=int)
    parser.add_argument('--inputs-shape-override', default='', help="[model] override the shape of one or more input (dim0 will still been overwrite later as batch_size), use json format like: {\"input1\": [null, 128], ...}, null value will been skiped\n")


    parser.add_argument('--roofline-use-small-model', action='store_true', help="[roofline] use small model in roofline test, for edge or cpu")
    parser.add_argument('--llc-reuse-size', default=0.0, help="in MiB, size of activation DRAM access (R+W) reduced by Last-Level-Cache", type=float)
    parser.add_argument('--no-color', action='store_true', help="force disable coloredlogs, may useful for log record on Windows")
    args = parser.parse_args()

    log_level = logging.INFO
    if args.verbose:
        log_level = logging.DEBUG

    logging.addLevelName(logging.INFO, "INFO")
    logging.addLevelName(logging.DEBUG, "DEBUG")
    logging.addLevelName(logging.WARNING, "WARNING")
    logging.addLevelName(logging.CRITICAL, "CRITICAL")
    logging.basicConfig(format="%(asctime)s %(levelname)s %(name)s %(message)s", level=log_level)
    if not args.no_color:
        level_styles = coloredlogs.DEFAULT_LEVEL_STYLES.copy()
        level_styles['debug']['color'] = 'white'
        coloredlogs.install(fmt="%(asctime)s %(levelname)s %(name)s %(message)s", level=log_level, level_styles=level_styles)
    log.debug("NOTICE: debug logging is ON")

    log.info("Temporary directory (PROOF_TMPDIR): %s", TMPDIR)

    subjects = [x.strip() for x in (args.subjects.split(','))] if args.subjects else []

    if args.model_backend not in model.backend.get_available_backends():
        log.error("unsupported backend %s", args.model_backend)
        sys.exit(1)

    model_backend = model.backend.get_backend(args.model_backend)
    onnx_model = args.onnx_model
    batch_size_list = _get_batch_size_list(args.batch_size)
    repeat_count = args.repeat
    backend_options = args.backend_options
    data_width = tuple(map(int, args.data_width.split(",")))
    llc_reuse_size = args.llc_reuse_size
    roofline_small = args.roofline_use_small_model
    inputs_shape_override = json.loads(args.inputs_shape_override) if args.inputs_shape_override else {}

    if not subjects:
        subjects = PerfContext.list_subjects()
    log.info("subjects: %s", subjects)
    if any(x.startswith('model') for x in subjects):
        if not onnx_model:
            log.error("for subject 'model', the ONNX model to test is required (-m ./xxx.onnx)")
            sys.exit(1)

    ctx = PerfContext(subjects, model_backend,
        onnx_model, batch_size_list, repeat_count, backend_options, data_width,
        llc_reuse_size=llc_reuse_size,
        roofline_small=roofline_small,
        inputs_shape_override=inputs_shape_override)

    try:
        ctx.run()
    except BaseException as e:
        import traceback
        traceback.print_exc()
        log.error("got exception %s when running test" % e.__class__)
        log.error("report file (if any) maybe incomplete")
    finally:
        # TODO: cleanup
        pass

    if args.output:
        dat = asdict(ctx.collected_data)
        # DEBUG: to debug with dump error:
        # from test.util import dump_dict_with_type
        # dump_dict_with_type(dat)

        with open(args.output, 'w') as f:
            f.write(json.dumps(dat))
            log.info("collected data saved to %s", args.output)
```

This script is a robust command-line tool designed for AI model inference performance analysis and benchmarking. Here’s a detailed explanation of its functionality:

The `argparse.ArgumentParser` is set up to handle multiple command-line options, described below:

+ `prog`: Name of the tool (`PRoof`).
+ `description`: High-level description of the tool.
+ `epilog`: Extra usage tips or notes displayed at the end of the help text.
+ `formatter_class`: Uses the custom _HelpFormatter class for better help text formatting.

| **Flag**                | **Description**                                                                                                     | **Default Value**        |
|-------------------------|---------------------------------------------------------------------------------------------------------------------|--------------------------|
| `-v`, `--verbose`       | Enables debug-level logging.                                                                                        | `False`                 |
| `-s`, `--subjects`      | Specifies test subjects to run (empty means all). Example subjects are returned by `PerfContext.list_subjects()`.   | `''` (all subjects)     |
| `-f`, `--output`        | Specifies the output file for test results.                                                                         | `"report.json"`         |
| `-B`, `--model-backend` | Selects the backend for model inference (e.g., TensorRT, ONNX Runtime).                                              | `'trtexec'`            |
| `-D`, `--data-width`    | Specifies the data precision (`onnx,backend`). E.g., `32,16` for FP32 in ONNX and FP16 in backend.                  | `'32,32'`              |
| `-o`, `--backend-options` | Passes additional options to the backend.                                                                          | `''`                    |
| `-m`, `--onnx-model`    | Path to the ONNX model file for inference tests.                                                                    | `''` (required if `model` subject is selected) |
| `-b`, `--batch-size`    | Specifies batch sizes to test (e.g., `4` or `1-16`).                                                                | `'1'`                  |
| `-r`, `--repeat`        | Number of times each test is repeated.                                                                              | `10`                   |
| `--inputs-shape-override` | Overrides input shapes of the model using a JSON-like string.                                                      | `''`                   |
| `--roofline-use-small-model` | Uses a smaller model for roofline tests.                                                                         | `False`                |
| `--llc-reuse-size`      | Specifies the amount of activation memory reduced by the Last-Level Cache (LLC), in MiB.                            | `0.0`                  |
| `--no-color`            | Disables colored logging, useful for log recording on Windows.                                                      | `False`                |


`args = parser.parse_args()` : This processes the command-line arguments and stores them in args.

The log level is set to DEBUG if `--verbose` is specified, otherwise INFO. `coloredlogs` adds color to log messages unless `--no-color` is used.

#### Verify ONNX model:

```python
if any(x.startswith('model') for x in subjects) and not args.onnx_model:
    log.error("for subject 'model', the ONNX model to test is required (-m ./xxx.onnx)")
    sys.exit(1)
```

If a `model` subject is selected, the ONNX model file must be provided.

Create Context : Initializes a `PerfContext` object with the parsed arguments.

Run tests : Executes the test via `ctx.run()`, capturing and logging any exceptions.

### util.py :

```python
import os
import logging
from pathlib import Path
import sys
import tempfile

log = logging.getLogger(__name__)


TMPDIR = Path(os.getenv('PROOF_TMPDIR', str(Path(tempfile.gettempdir()) / 'proof')))
try:
    Path(TMPDIR).mkdir(parents=True, exist_ok=True)
    assert os.access(TMPDIR, os.W_OK)
except Exception as e:
    log.error('TMPDIR %s is not writeable (%s), you can change it via DNNROOF_TMPDIR env var', TMPDIR, e)
    sys.exit(1)
```

+ Setting Up a Temporary Directory:

    - The `TMPDIR` is defined using the environment variable `PROOF_TMPDIR`. If this variable is not set, it defaults to a temporary directory created inside the system's temp directory (`tempfile.gettempdir()`), named `proof`.
    - Example default value for `TMPDIR`: `/tmp/proof` on Linux, or something like `C:\Users\<username>\AppData\Local\Temp\proof on Windows`.

+ Creating the Directory:

    - The `mkdir` method of `Path` is used to create the directory represented by `TMPDIR`.
    - `parents=True`: Ensures that all missing parent directories are created.
    - `exist_ok=True`: Ensures no error occurs if the directory already exists.

+ Checking Write Access:

    - The `os.access` function checks if the TMPDIR is writable (`os.W_OK`).

### context.py :

```python
from __future__ import annotations

from typing import Tuple, List, Dict, Union
import os
import sys
from pathlib import Path
import logging
import numpy as np

from util import TMPDIR
from datatype import CollectedData, RooflineData, ModelData, ModelBenchData, ModelBenchBatchData
import model.analyze
from model.analyze.fuse import get_effort_fused_model
from model.backend import _BaseBackend

log = logging.getLogger(__name__)


# Used by main.py for CLI or as top level API of the package for other python program
class PerfContext():
    """Context of PRoof, """

    # defines all test subjects and their topology
    _ = None
    _all_subjects = {
        'roofline': _,
        'model': {
            'analyze': _,
            'bench': {
                'layer_prof': _,
                'e2e_prof': _
            }
        }
    }

    # test subjects and their depends
    _all_subjects_depends = {
        'model.bench': ['model.analyze'],
        'model.bench.layer_prof': ['model.bench.e2e_prof']
    }

    @classmethod
    def list_subjects(cls, _root: dict = _all_subjects) -> List[str]:
        l = []
        if _root:
            for k, v in _root.items():
                l.append(k)
                if type(v) is dict:
                    l += [k + '.' + x for x in cls.list_subjects(v)]
        return l

    def _process_subjects(self, subjects_list) -> None:
        "['a', 'b.1', 'b.2'] to {'a': ..., 'b': {'1': ..., '2': ...}}"

        self.subjects = set()
        subjects_list = subjects_list[:]

        for subject in subjects_list:
            all_pos = self._all_subjects
            subject_l = subject.split('.')
            for i in range(len(subject_l)):
                mid_name = subject_l[i]
                prefix = '.'.join(subject_l[:i+1])
                self.subjects.add(prefix)
                if mid_name not in all_pos:
                    log.error("no such subject '%s', available: %s", prefix, self.list_subjects())
                    sys.exit(1)

                all_pos = all_pos[mid_name]
                if prefix in self._all_subjects_depends:
                    subjects_list += self._all_subjects_depends[prefix]
            child_subjects = set(subject + '.' + x for x in self.list_subjects(_root=all_pos))
            self.subjects.update(child_subjects)

    def __init__(self,
            subjects: list,
            model_backend: _BaseBackend,

            # optional, keep the defaults same as in main.py
            onnx_model: str = '',
            batch_size_list: list = [1],
            repeat_count: int = 10,
            backend_options: str = '',
            data_width: Tuple[int, int] = (32, 32),
            *,

            # addition
            llc_reuse_size: float = .0,
            roofline_small: bool = False,
            inputs_shape_override: Dict[str, List[Union[int, None]]] = {}) -> None:

        self._process_subjects(subjects)
        self.collected_data = CollectedData()
        self.collected_data.subjects = list(self.subjects)

        self.model_backend = model_backend
        self.backend_options = backend_options
        self.data_width = data_width

        if 'roofline' in self.subjects:
            self.roofline_ctx = RooflineContext(self.subjects, self.collected_data, model_backend, backend_options, data_width, roofline_small)

        if 'model' in self.subjects:
            self.model_ctx = ModelContext(self.subjects, self.collected_data, model_backend, onnx_model, batch_size_list, repeat_count, backend_options, data_width, llc_reuse_size, inputs_shape_override)

    def run(self) -> None:
        if 'roofline' in self.subjects:
            self.roofline_ctx.run()

        if 'model' in self.subjects:
            self.model_ctx.run()


class RooflineContext():
    def __init__(self,
            subjects: list, collected_data: CollectedData, model_backend: _BaseBackend, backend_options: str, data_width: Tuple[int, int], small_model: bool) -> None:
        self.subjects = subjects
        self.collected_data = collected_data
        self.data_width_onnx = data_width[0]
        self.data_width_backend = data_width[1]

        self.collected_data.roofline = RooflineData()
        self.collected_data.roofline.backend = model_backend.__name__
        self.collected_data.roofline.backend_options = backend_options
        self.collected_data.roofline.data_width_onnx = data_width[0]
        self.collected_data.roofline.data_width_backend = data_width[1]

        from model.roofline import generate_roofline_test_model
        if not small_model:
            self.collected_data.roofline.model_type = 'default'
            model = generate_roofline_test_model(128, 8)    # default size, for GPU like NVIDIA A100
        else:
            self.collected_data.roofline.model_type = 'small'
            model = generate_roofline_test_model(32, 7)     # small size, for edge or cpu

        import onnx
        self.onnx_model = str(TMPDIR / 'roofline_test_model.onnx')
        onnx.save(model, self.onnx_model)

        self.model_backend_env: _BaseBackend = model_backend(self, self.onnx_model, [1], backend_options)
        self.collected_data.roofline.backend_version_info = self.model_backend_env.version_info()
        print(self.collected_data.roofline.backend_version_info)
        self.model_backend_env.prepare()

    def run(self) -> None:
        if 'layer_prof' not in self.model_backend_env.supported:
            log.error("can not run roofline test, backend %s not support [layer_prof]", self.collected_data.roofline.backend)
            return

        self.analyze = model.analyze.Analyze(self.onnx_model)
        self.model_backend_env.pre_batch_run(1)
        layer_prof = self.model_backend_env.layer_prof(1)

        flops: Dict[str, float] = {}    # name: FLOPS
        memory_bandwidth: Dict[str, float] = {}  # name: Byte/s
        for layer in layer_prof:
            onnx_nodes = layer.extra['onnx_nodes']
            for name in onnx_nodes:
                if name.startswith('MatMul'):
                    if len(onnx_nodes) > 1:
                        log.warning("in roofline_test_model, original onnx node %s is fused with %s, the results may inaccurate", name, onnx_nodes)
                    size = int(name[len('MatMul_'):])
                    flops[name] = layer.flops / layer.median_time
                    log.debug("MatMulOp size {}x{} reached {:.4f} GFLOPS".format(size, size, flops[name] / 1e9))
                if name.startswith('Relu_'):
                    if len(onnx_nodes) > 1:
                        log.warning("in roofline_test_model, original onnx node %s is fused with %s, the results may inaccurate", name, onnx_nodes)
                    size = int(name[len('Relu_'):])
                    memory_bandwidth[name] = layer.memory / layer.median_time
                    log.debug("ReluOp size {}x{} reached {:.4f} GB/s".format(size, size, memory_bandwidth[name] / 1e9))
                if name.startswith('Transpose_'):
                    if len(onnx_nodes) > 1:
                        log.warning("in roofline_test_model, original onnx node %s is fused with %s, the results may inaccurate", name, onnx_nodes)
                    size = int(name[len('Transpose_'):])
                    memory_bandwidth[name] = layer.memory / layer.median_time
                    log.debug("TransposeOp size {}x{} reached {:.4f} GB/s".format(size, size, memory_bandwidth[name] / 1e9))
                if name.startswith('Concat_'):
                    # if len(onnx_nodes) > 1:
                    #     log.warning("in roofline_test_model, original onnx node %s is fused with %s, the results may inaccurate", name, onnx_nodes)
                    memory_bandwidth[name] = layer.memory / layer.median_time
                    log.debug("{} reached {:.4f} GB/s".format(name, memory_bandwidth[name] / 1e9))

        self.collected_data.roofline.flops = max(flops.values())
        self.collected_data.roofline.memory_bandwidth = max(memory_bandwidth.values())
        print("reached roofline (large matmul): {:.4f} GFLOPS, {:.4f} GB/s".format(self.collected_data.roofline.flops / 1e9, self.collected_data.roofline.memory_bandwidth / 1e9))
        print("NOTE: Also run a ResNet-34 model to test Conv roofline, this may necessary for some device. ")

class ModelContext():
    def __init__(self, subjects: list, collected_data: CollectedData, model_backend: _BaseBackend, onnx_model: str, batch_size_list: list, repeat_count: int, backend_options: str, data_width: Tuple[int, int], llc_reuse_size: float, inputs_shape_override: Dict[str, List[Union[int, None]]]) -> None:
        self.subjects = subjects
        self.collected_data = collected_data
        self.onnx_model = onnx_model
        self.batch_size_list = batch_size_list
        self.repeat_count = repeat_count
        self.data_width_onnx = data_width[0]
        self.data_width_backend = data_width[1]
        log.info("data_width in onnx and backend is %s bit, change it if not correct", data_width)

        self.collected_data.model = ModelData()
        self.collected_data.model.name = Path(onnx_model).name
        self.collected_data.model.path = onnx_model
        self.collected_data.model.backend = model_backend.__name__
        self.collected_data.model.backend_options = backend_options
        self.collected_data.model.data_width_onnx = data_width[0]
        self.collected_data.model.data_width_backend = data_width[1]
        self.collected_data.model.llc_reuse_size = llc_reuse_size
        self.collected_data.model.inputs_shape_override = inputs_shape_override

        if inputs_shape_override:
            log.info("inputs_shape_override is set, will save the modified model to tmpdir as a copy")
            import onnx
            m = onnx.load(self.onnx_model)
            for t in m.graph.input:
                if t.name in inputs_shape_override:
                    for i, dim in enumerate(inputs_shape_override[t.name]):
                        if dim:
                            t.type.tensor_type.shape.dim[i].dim_value = dim
            self.onnx_model = str(TMPDIR / 'inputs_shape_override_model.onnx')
            if os.path.isfile(str(TMPDIR / 'model_external_data.pb')):
                os.unlink(str(TMPDIR / 'model_external_data.pb'))
            onnx.save(m, self.onnx_model, save_as_external_data=True, location="model_external_data.pb")

        if 'model.bench' in self.subjects:
            self.model_backend_env: _BaseBackend = model_backend(self, self.onnx_model, self.batch_size_list, backend_options)
            self.collected_data.model.backend_version_info = self.model_backend_env.version_info()
            print(self.collected_data.model.backend_version_info)
            self.model_backend_env.prepare()

    def run(self) -> None:

        if 'model.analyze' in self.subjects:
            self.analyze = model.analyze.Analyze(self.onnx_model)
            self.collected_data.model.analyze = self.analyze.export_data()

            # max fused memory
            effort_fused = get_effort_fused_model(self.analyze)
            self.collected_data.model.analyze.total_memory_effort_fused = effort_fused.get_memory()
            log.info("total memory %.3f M (vars) (approximate, effort fused)", effort_fused.get_memory() / 1e6)


        if 'model.bench' in self.subjects:
            self.collected_data.model.bench = ModelBenchData()
            self.collected_data.model.bench.batch_size_list = self.batch_size_list
            self.collected_data.model.bench.results = {}
            log.debug("batch_size_list: %s", self.batch_size_list)
            for batch_size in self.batch_size_list:
                batch_data = ModelBenchBatchData()
                batch_data.batch_size = batch_size

                print("="*60)
                print("batch_size: %s" % batch_size)

                self.model_backend_env.pre_batch_run(batch_size)
                if 'model.bench.layer_prof' in self.subjects:
                    if 'layer_prof' not in self.model_backend_env.supported:
                        log.error("layer_prof is not support in %s, skip", self.model_backend_env.__class__)
                    else:
                        batch_data.layer_prof = self.model_backend_env.layer_prof(batch_size)
                        batch_data.better_total_flops = sum(l.flops for l in batch_data.layer_prof)
                        batch_data.better_total_memory = sum(l.memory for l in batch_data.layer_prof)

                        DUMP_TO_DEBUG = False
                        DUMP_TO_DEBUG = True   # TODO_tmp: dev only
                        if DUMP_TO_DEBUG:
                            for layer in batch_data.layer_prof:
                                log.debug("[layer_prof dump] avg: %s ms, %s GFLOPS, %s GB/s, name: %s - %s",
                                    '{:8.4f}'.format(layer.median_time * 1000),
                                    '{:12.4f}'.format(layer.flops / layer.median_time / 1e9),
                                    '{:12.4f}'.format(layer.memory / layer.median_time / 1e9),
                                    '{:<64}'.format(layer.name),
                                    layer.extra)
                            log.debug("[layer_prof dump] GB/s is approximate memory bandwidth")
                            log.debug("[layer_prof dump] total_flops %.3f MFLOPs (%.3f * %d)",
                                batch_data.better_total_flops / 1e6,
                                batch_data.better_total_flops / 1e6 / batch_size,
                                batch_size)
                            log.debug("[layer_prof dump] total_memory %.3f MB (%.3f * %d)",
                                batch_data.better_total_memory / 1e6,
                                batch_data.better_total_memory / 1e6 / batch_size,
                                batch_size)
                            max_flops_layer = max(batch_data.layer_prof, key=lambda x: x.flops / x.median_time)
                            log.info(f"max flops node: {max_flops_layer.flops / max_flops_layer.median_time / 1e12:.3f} TFLOPS, ({max_flops_layer.median_time*1e3:.3f} ms)")


                if 'model.bench.e2e_prof' in self.subjects:
                    if 'e2e_prof' not in self.model_backend_env.supported:
                        log.error("e2e_prof is not support in %s, skip", self.model_backend_env.__class__)
                    else:
                        times = self.model_backend_env.e2e_prof(batch_size, self.repeat_count)

                        if isinstance(times, np.ndarray):
                            batch_data.times = list(times)
                            log.debug(times)

                            batch_data.time_avg = np.average(times)
                            batch_data.time_min = np.min(times)
                            batch_data.time_std = np.std(times)
                        elif isinstance(times, dict):
                            batch_data.time_avg = times['avg']
                            batch_data.time_min = times['min']
                            batch_data.time_std = times['std']

                        print("TIME:   average: {:12.4f} ms,        min: {:12.4f} ms,        std: {:8.4f} ms".format(
                            batch_data.time_avg * 1000, batch_data.time_min * 1000, batch_data.time_std * 1000))

                        if batch_data.better_total_flops and not os.getenv('PROOF_E2E_NOT_USE_LAYER_DATA'):
                            model_flops = batch_data.better_total_flops
                        else:
                            model_flops = float(self.collected_data.model.analyze.total_flops) * batch_size
                        batch_data.flops_avg = model_flops / batch_data.time_avg
                        batch_data.flops_max = model_flops / batch_data.time_min
                        batch_data.flops_std = np.std(model_flops / times) if isinstance(times, np.ndarray) else -1
                        print("GFLOPS: average: {:12.4f} GFLOPS,    max: {:12.4f} GFLOPS,    std: {:8.4f} GFLOPS".format(
                            batch_data.flops_avg / 1e9, batch_data.flops_max / 1e9, batch_data.flops_std / 1e9))

                        if batch_data.better_total_memory and not os.getenv('PROOF_E2E_NOT_USE_LAYER_DATA'):
                            accurate = "approximate"
                            model_memory_access = batch_data.better_total_memory
                        else:
                            accurate = "inaccurate"
                            model_memory_access = float(self.collected_data.model.analyze.total_memory) * batch_size
                        batch_data.memory_avg = model_memory_access / batch_data.time_avg
                        batch_data.memory_max = model_memory_access / batch_data.time_min
                        batch_data.memory_std = np.std(model_memory_access / times) if isinstance(times, np.ndarray) else -1
                        print("Memory: average: {:12.4f} GB/s,      max: {:12.4f} GB/s,      std: {:8.4f} GB/s \t({})".format(
                            batch_data.memory_avg / 1e9, batch_data.memory_max / 1e9, batch_data.memory_std / 1e9, accurate))


                self.collected_data.model.bench.results[str(batch_size)] = batch_data  # JSON format need a str for the key (batch_size)
                log.debug("run() model batch_size=%s done", batch_size)

            log.debug("run() model all batch_size done")

        log.debug("run() all done")
```