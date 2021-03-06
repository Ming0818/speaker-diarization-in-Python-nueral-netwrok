import numpy
import scipy.io.wavfile
import bob.io.base

from bob.bio.base.preprocessor import Preprocessor

class Base (Preprocessor):
  """Performs color space adaptations and data type corrections for the given image"""

  def __init__(self, **kwargs):
    # Each class needs to have a constructor taking
    # all the parameters that are required for the preprocessing as arguments
    self._kwargs = kwargs
    pass


  def read_original_data(self, original_file_name):
    """Reads the *original* wav data from file (usually .wav file)
    If you have different format, please overwrite this function.
    """
    rate, audio = scipy.io.wavfile.read(original_file_name)
    # We consider there is only 1 channel in the audio file => data[0]
    data= numpy.cast['float'](audio)
    return rate, data

  def write_data(self, data, data_file, compression=0):
    """Writes the given *preprocessed* data to a file with the given name.
    """
    f = bob.io.base.HDF5File(data_file, 'w')
    f.set("rate", data[0], compression=compression)
    f.set("data", data[1], compression=compression)
    f.set("labels", data[2], compression=compression)
   

  def read_data(self, data_file):
    f= bob.io.base.HDF5File(data_file)
    rate    = f.read("rate")
    data   = f.read("data")
    labels = f.read("labels")
    return rate, data, labels

