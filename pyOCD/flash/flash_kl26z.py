"""
 mbed CMSIS-DAP debugger
 Copyright (c) 2006-2013 ARM Limited

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

from flash import Flash

flash_algo = { 'load_address' : 0x20000000,
               'instructions' : [
    0xE00ABE00, 0x062D780D, 0x24084068, 0xD3000040, 0x1E644058, 0x1C49D1FA, 0x2A001E52, 0x4770D1F2,
    0xb510492e, 0x60084449, 0x2100482d, 0x482e6001, 0x44484a2c, 0x2100e9c0, 0x2280f44f, 0x2926082,
    0xf04f60c2, 0xe9c052a0, 0xf8802105, 0x1e491020, 0xf0006241, 0x2800f937, 0x2001d000, 0x2000bd10,
    0xb5084770, 0x447a4a21, 0xf3c19200, 0x460102cf, 0x2300481d, 0xf0004448, 0x2800f9df, 0x2001d000,
    0xb510bd08, 0x44794919, 0x39204817, 0xf0004448, 0x2800f89e, 0x2001d000, 0xb510bd10, 0x447b4b13,
    0x48114601, 0xf44f3b38, 0x44486200, 0xf8c3f000, 0xd0002800, 0xbd102001, 0x460cb538, 0x4479490b,
    0x91003958, 0x48084601, 0x46224613, 0xf0004448, 0x2800f966, 0x2001d000, 0xbd38, 0x4,
    0x40048100, 0x40020000, 0x8, 0x9f, 0x2480b51c, 0x1004f88d, 0x2005f88d, 0x4000f88d,
    0x2105466a, 0xbd1c4798, 0x4604b570, 0x25006800, 0x61b7803, 0x2370d5fc, 0x20007003, 0x280ce03a,
    0xe8dfd236, 0xa06f000, 0x1a16120e, 0x2a26221e, 0x6826322e, 0x71f37813, 0x6826e02a, 0x71b37853,
    0x6826e026, 0x71737893, 0x6826e022, 0x713378d3, 0x6826e01e, 0x72f37913, 0x6826e01a, 0x72b37953,
    0x6826e016, 0x72737993, 0x6826e012, 0x723379d3, 0x6826e00e, 0x73f37a13, 0x6826e00a, 0x73b37a53,
    0x6826e006, 0x73737a93, 0x6826e002, 0x73337ad3, 0xb2c01c40, 0xd9c24288, 0x20806821, 0xe0037008,
    0x1c416a60, 0x4780d000, 0x78006820, 0xd5f70600, 0x78006820, 0xd5010681, 0xe0062504, 0xd50106c1,
    0xe0022508, 0xd00007c0, 0x46282510, 0xb508bd70, 0x460b2244, 0x2000f88d, 0x2100466a, 0xbd084798,
    0x4614b538, 0xd002078a, 0x7080f44f, 0x6843bd38, 0xd803428b, 0x441a6882, 0xd80c428a, 0x428b68c3,
    0x6902d803, 0x428a441a, 0x2002d801, 0x1ac9bd38, 0x100f501, 0x1ac9e000, 0xf88d2208, 0xc0a2000,
    0x2001f88d, 0xf88d0a0a, 0xf88d2002, 0x466a1003, 0x47a02103, 0xe92dbd38, 0x460745f8, 0x46164698,
    0x2000687b, 0xf44f198a, 0x428b6500, 0x68bcd803, 0x4294441c, 0x68fbd20d, 0xd803428b, 0x441c693c,
    0xd2024294, 0xe8bd2002, 0x1acc85f8, 0x400f504, 0x1acce000, 0xf1f5fbb4, 0x4111fb05, 0xf44fb111,
    0xe7f07080, 0xf1f5fbb6, 0x6111fb05, 0x2001b1a9, 0xf88de7e9, 0xc20a000, 0x1f88d, 0xf88d0a20,
    0xf88d0002, 0x466a4003, 0x46382103, 0x47984643, 0xd1d82800, 0x442c1b76, 0xf04fe001, 0x2e000a09,
    0xe7d0d1e7, 0x6801b5f0, 0x780a2400, 0xd5fc0612, 0x700a2270, 0x21036802, 0x680171d1, 0x718d2580,
    0x21006802, 0x68037151, 0x711a22fc, 0x73d16802, 0x70156802, 0x78136802, 0xd5fc061b, 0x7a127a56,
    0xc0ff002, 0x2280f44f, 0xf1bc1057, 0xd2170f10, 0xf00ce8df, 0xd0a0808, 0x8151310, 0x27240815,
    0x808132a, 0xe00b6102, 0x3270f44f, 0xf44fe7fa, 0xe7f73260, 0x3240f44f, 0x6107e7f4, 0x6101e000,
    0x20ff006, 0xd2242a10, 0xf002e8df, 0x16131111, 0x221f1c19, 0x11112725, 0x11111111, 0x4280f44f,
    0xf44fe7e0, 0xe7dd4200, 0x3280f44f, 0x61c1e7da, 0xf44fe00f, 0xe7fa5180, 0x6100f44f, 0xf44fe7f7,
    0xe7f46180, 0x7100f44f, 0xf44fe7f1, 0xe7ee7180, 0x462061c5, 0x2140bdf0, 0x2120e7e9, 0xe92de7e7,
    0x461647fc, 0x461d4607, 0x198a2000, 0x8028f8dd, 0xd003078b, 0x7080f44f, 0x87fce8bd, 0xd00107b3,
    0xe7f92001, 0x428b687b, 0x68bcd803, 0x4294441c, 0x68fbd20c, 0xd803428b, 0x441c693c, 0xd2014294,
    0xe7e92002, 0xf5041acc, 0xe0000400, 0xf04f1acc, 0x2e000a06, 0xf88dd0e0, 0xc20a000, 0x1f88d,
    0xf88d0a20, 0xf88d0002, 0x78e84003, 0x4f88d, 0xf88d78a8, 0x78680005, 0x6f88d, 0xf88d7828,
    0x466a0007, 0x46382107, 0x47984643, 0xd1c32800, 0x1f361d24, 0xe7dc1d2d, 0x41fce92d, 0x9d086846,
    0x4c2eb01, 0xd803428e, 0x44376887, 0xd80a428f, 0x428f68c7, 0xf8d0d804, 0x4467c010, 0xd802428f,
    0xe8bd2002, 0x42a681fc, 0x6887d805, 0x42a74437, 0x1b89d301, 0x68c6e009, 0xd90342a6, 0x44376907,
    0xd3ed42a7, 0xf5011b89, 0x24080100, 0xf6f4fbb1, 0x1416fb04, 0xf44fb114, 0xe7e27080, 0xf88d2401,
    0xc0c4000, 0x4001f88d, 0xf88d0a0c, 0xf88d4002, 0xa111003, 0x1004f88d, 0x2005f88d, 0x3006f88d,
    0x2106466a, 0xe7cc47a8, 0xfffffffe, 0x0, 0x0,
                                ],
               'pc_init' : 0x20000021,
               'pc_eraseAll' : 0x20000083,
               'pc_erase_sector' : 0x2000009B,
               'pc_program_page' : 0x200000B9,
               'begin_stack' : 0x20000800,
               'begin_data' : 0x20000a00,
               'static_base' : 0x200005d0,
               'page_size' : 1024
              };

class Flash_kl26z(Flash):
    
    def __init__(self, target):
        super(Flash_kl26z, self).__init__(target, flash_algo)
    
