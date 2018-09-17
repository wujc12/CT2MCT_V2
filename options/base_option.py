from easydict import EasyDict


opt = EasyDict()

opt.dataroot = None
opt.batchSize = 1
opt.loadSize = 286
opt.fineSize = 256
opt.input_nc = 3
opt.output_nc = 3
opt.ngf = 64
opt.ndf = 64
opt.which_model_netD = 'basic'
opt.which_model_netG = 'resnet_9blocks'
opt.n_layers_D = 3
opt.gpu_ids = 0
opt.name = 'experiment_name'
opt.dataset_mode = 'aligned'
opt.model = 'pix2pix'
opt.which_direction = 'AtoB'
opt.nThreads = 4
opt.checkpoints_dir = './checkpoints'
opt.norm = 'instance'
opt.serial_batches = True
opt.display_winsize = 256
opt.display_id = 1
opt.display_server = 'http://locakhost'
opt.display_port = '8097'
opt.no_dropout = True
opt.max_dataset_size = float("inf")
opt.resize_or_crop = 'resize_and_crop'
opt.no_flip = True
opt.init_type = 'normal'
opt.verbose = True
opt.suffix = ''
