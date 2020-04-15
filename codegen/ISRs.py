#!/usr/bin/env python3

from os.path import dirname, join, basename

max_num_interrupts = 60

header = f"""\
// ========================================================================== //
//                                                                            //
//                        AUTOMATICALLY GENERATED FILE                        //
//                                DO NOT EDIT!                                //
//                                                                            //
// ========================================================================== //

// Edit and re-run  {basename(__file__)} instead

#if defined(ENCODER_USE_INTERRUPTS) && !defined(ENCODER_OPTIMIZE_INTERRUPTS)

namespace EncoderISRs {{

"""

footer = f"""

}} // namespace EncoderISRs

#endif
"""

decl = """\
using ISR_fun_t = void (*)(void);

extern ISR_fun_t ISRs[ENCODER_ARGLIST_SIZE];"""

ISRs = "ISR_fun_t ISRs[ENCODER_ARGLIST_SIZE] = {\n"
for i in range(max_num_interrupts):
    ISRs += f'  #if {i} < ENCODER_ARGLIST_SIZE\n'
    ISRs += f'    +[] {{ Encoder::update(Encoder::interruptArgs[{i}]); }},\n'
    ISRs += f'  #endif\n'
ISRs += "};"

with open(join(dirname(__file__), 'ISRs-decl.ipp'), 'w') as f:
    f.write(header)
    f.write(decl)
    f.write(footer)

with open(join(dirname(__file__), 'ISRs-def.ipp'), 'w') as f:
    f.write(header)
    f.write(ISRs)
    f.write(footer)
