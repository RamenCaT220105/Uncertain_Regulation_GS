 Uncertain_Regulation_GS

#El Proyecto es capaz de correr tanto en ubuntu 22 como 24. Solo asegurarse de verificar la ubicación y compatibilidad de versiones entre nvcc, cuda toolkit y driver. Si no desea usar docker recomiendo corer cada comando por separado


El entorno
source gs-env/bin/activate


python train.py \
  --source_path ./data/testscene \
  --model_path ./output/testscene \
  --images images \
  --white_background \
  --iterations 30000 \
  --densify_from_iter 500 \
  --densify_until_iter 15000 \
  --disable_viewer
