cd src
CUDA_VISIBLE_DEVICES="2" python train.py mot --exp_id mta_dla34 --load_model '../exp/mot/mot17_dla34/model_last.pth' --data_cfg '../src/lib/cfg/mta.json' --gpus 2
cd ..