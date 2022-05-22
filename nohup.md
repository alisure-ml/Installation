### nohup

> 后台挂起执行程序


* `nohup python train.py > ./3.log 2>&1 &`

* `PYTHONPATH=. CUDA_VISIBLE_DEVICES=0,1,2,3 nohup python -m torch.distributed.launch --nproc_per_node=4 --master_port=12431 train.py --launcher pytorch > ./work_dirs/3.log 2>&1 &`

