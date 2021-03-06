from radiomics import firstorder, glcm, imageoperations, shape, glrlm, glszm
import SimpleITK as sitk
import sys, os

image = sitk.ReadImage(sys.argv[1])
mask = sitk.ReadImage(sys.argv[2])

(ii, im) = imageoperations.resampleImage(image, mask, [2, 2, 2])

sitk.WriteImage(ii, sys.argv[3])
sitk.WriteImage(im, sys.argv[4])
