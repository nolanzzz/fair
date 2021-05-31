cd src
python train.py mot --exp_id mta_dla34 --batch_size 64 --load_model '../exp/mot/mot17_dla34/model_last.pth' --num_epochs 30 --data_cfg '../src/lib/cfg/mta.json'
cd ..