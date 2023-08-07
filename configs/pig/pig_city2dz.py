# Default PIG Configuration for Cityscapes->Dark Zurich
_base_ = [
    '../_base_/default_runtime.py',
    '../_base_/models/daformer_sepaspp_mitb5.py',
    '../_base_/datasets/nfnet_cs2dz.py',
    '../_base_/uda/dacs_a999_fdthings.py',
    '../_base_/schedules/adamw.py',
    '../_base_/schedules/poly10warm.py'
]
# Random Seed
seed = 2
# PIG Configuration
model = dict(
    type='HRDAEncoderDecoder',
    decode_head=dict(
        type='HRDAHead',
        single_scale_head='DAFormerHead',
        attention_classwise=True,
        hr_loss_weight=0.1),
    scales=[1, 0.5],
    hr_crop_size=[512, 512],
    feature_scale=0.5,
    crop_coord_divisible=8,
    hr_slide_inference=True,
    test_cfg=dict(
        mode='slide',
        batched_slide=True,
        stride=[512, 512],
        crop_size=[1024, 1024]))
data = dict(
    train=dict(
        rare_class_sampling=dict(
            min_pixels=3000, class_temp=0.01, min_crop_ratio=2.0),
        target=dict(crop_pseudo_margins=[30, 240, 30, 30]),
    ),
    workers_per_gpu=1)
# Optimizer Hyperparameters
optimizer_config = None
optimizer = dict(
    lr=6e-05)
n_gpus = 1
gpu_model = 'NVIDIA_RTX_A6000'
runner = dict(type='IterBasedRunner', max_iters=40000)
# Logging Configuration
checkpoint_config = dict(by_epoch=False, interval=4000, max_keep_ckpts=1)
evaluation = dict(interval=4000, metric='mIoU')
# Meta Information for Result Analysis
name = 'city2dz_pig'
exp = 'basic'
name_dataset = 'city2dz'
name_architecture = 'hrda1-512-0.1_daformer_sepaspp_sl_mitb5'
name_encoder = 'mitb5'
name_decoder = 'hrda1-512-0.1_daformer_sepaspp_sl'
name_uda = 'dacs_a999_fdthings_rcs0.01-2.0_cpl2'
name_opt = 'adamw_6e-05_pmTrue_poly10warm_1x2_40k'