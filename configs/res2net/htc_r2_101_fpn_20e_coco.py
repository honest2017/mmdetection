_base_ = '../htc/htc_r50_fpn_1x_coco.py'
model = dict(
    pretrained=  # NOQA
    'https://shanghuagao.oss-cn-beijing.aliyuncs.com/res2net/res2net101_v1b_26w_4s_mmdetv2-f0a600f9.pth',  # NOQA
    backbone=dict(type='Res2Net', depth=101, scale=4, base_width=26))
# learning policy
lr_config = dict(step=[16, 19])
total_epochs = 20