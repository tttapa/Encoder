#!/usr/bin/env python3

from os.path import dirname, join

max_num_interrupts = 60

ISRs = r"""
#if defined(ENCODER_USE_INTERRUPTS) && !defined(ENCODER_OPTIMIZE_INTERRUPTS)

    using ISR_fun_t = void (*)(void);

    ISR_fun_t ISRs[ENCODER_ARGLIST_SIZE] = {
"""

for i in range(max_num_interrupts):
    ISRs += f'      #if {i} < ENCODER_ARGLIST_SIZE\n'
    ISRs += f'        +[] {{ update(Encoder::interruptArgs[{i}]); }},\n'
    ISRs += f'      #endif\n'

ISRs += r"""    };

#endif
"""

with open(join(dirname(__file__), 'ISRs.ipp'), 'w') as f:
    f.write(ISRs)