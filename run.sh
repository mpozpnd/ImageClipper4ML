clipsize=256

ls imgs/ > datalist
perl -i -pe 's/^/imgs\//g' datalist
python ./ImageClipper.py ./datalist $clipsize ./clipped
ls clipped > imglist
perl -i -pe 's/^/clipped\//g' imglist
python ./jpg2np.py imglist $clipsize
