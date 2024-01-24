import os

from spectral import open_image
from happy.data import HappyData
from happy.writers import MatlabWriter

sample_id = "92AV3C"
base_dir = "."
local_file = os.path.join("../92AV3C", "92AV3C.lan")
print("Converting test data: %s" % local_file)
img = open_image(local_file)
img_data = img.load()
wavenumbers = [x for x in range(img.nbands)]
happy_data = HappyData(sample_id, "1", img_data, {}, {}, wavenumbers)
print("Saving test data: %s/%s" % (base_dir, sample_id))
writer = MatlabWriter(base_dir=base_dir)
writer.write_data(happy_data)
print("Finished writing matlab data!")
