#ifndef INCLUDED_GR_WAVFILE_SOURCE_H	
#define INCLUDED_GR_WAVFILE_SOURCE_H

from gnuradio import gr
from gnuradio import audio
from gnuradio import digital
#from gnuradio import analog, digital
from gnuradio import blocks
from gnuradio import filter




class psk31_demod(gr.top_block):

    def __init__(self, src_file):
        gr.top_block.__init__(self)

        sample_rate = 11025
	ampl = 0.1
        print src_file
        # Audio source (.wav file)
        # TODO : Make the filename a VARIABLE
        # src_file = input("Enter .wav File PSK31 : ")
        src = blocks.wavfile_source(src_file, False)

        # Raw float data output file.
        # TODO : To make the raw file also a variable, for psk31decoder2.py to run
        dst = blocks.file_sink(1, "./output.raw")

        # Delay line. This delays the signal by 32ms
        dl = blocks.delay(gr.sizeof_float, int(round(sample_rate/31.25)))

        # Multiplier
        # Multiplying the source and the delayed version will give us
        # a negative output if there was a phase reversal and a positive output
        # if there was no phase reversal
        mul = blocks.multiply_ff(1)

        # Low Pass Filter. This leaves us with the envelope of the signal
        lpf_taps = filter.firdes.low_pass(
            5.0,
            sample_rate,
            15,
            600,
            filter.firdes.WIN_HAMMING)
        lpf = filter.fir_filter_fff(1, lpf_taps)

        # Binary Slicer (comparator)
        slc = digital.binary_slicer_fb()

        # Connect the blocks.
        self.connect(src, dl)
        self.connect(src, (mul, 0))
        self.connect(dl,  (mul, 1))
        self.connect(mul, lpf)
        self.connect(lpf, slc)
        self.connect(slc, dst)

# Instantiate the demodulator
if __name__ == '__main__':
    try:
        psk31_demod("./bpsk31.wav").run()
    except KeyboardInterrupt:
        pass

#endif /* INCLUDED_GR_WAVFILE_SOURCE_H */

