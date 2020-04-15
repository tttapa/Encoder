// ========================================================================== //
//                                                                            //
//                        AUTOMATICALLY GENERATED FILE                        //
//                                DO NOT EDIT!                                //
//                                                                            //
// ========================================================================== //

// Edit and re-run  ISRs.py instead

#if defined(ENCODER_USE_INTERRUPTS) && !defined(ENCODER_OPTIMIZE_INTERRUPTS)

namespace EncoderISRs {

using ISR_fun_t = void (*)(void);

extern ISR_fun_t ISRs[ENCODER_ARGLIST_SIZE];

} // namespace EncoderISRs

#endif
