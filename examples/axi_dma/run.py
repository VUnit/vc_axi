# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2014-2019, Lars Asplund lars.anders.asplund@gmail.com

"""
AXI DMA
-------

Demonstrates the AXI read and write slave verification components as
well as the AXI-lite master verification component. An AXI DMA is
verified which uses an AXI master port to read and write data from
external memory. The AXI DMA also has a control register interface
via AXI-lite.
"""

from os.path import join, dirname, abspath
from vunit import VUnit


root = dirname(__file__)
src_path = join(root, "src")

ui = VUnit.from_argv()

ui.add_osvvm()
ui.use_verification_components(
    ui.add_verification_components(
        abspath(join(root, '..', '..', '..'))
    ),
    ['AXI']
)

ui.add_library("axi_dma_lib").add_source_files([
    join(src_path, "*.vhd"),
    join(src_path, "test", "*.vhd")
])

if __name__ == '__main__':
    ui.main()
