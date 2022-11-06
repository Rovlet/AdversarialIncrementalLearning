epochs = 2
exemplars = 3000
batch_size = 120

methods = {
    'icarl': {
        'NETWORK': 'resnet32',
        'BATCH_SIZE': batch_size,
        'NUM_EXEMPLARS_PER_CLASS': 0,
        'MAX_NUM_EXEMPLARS': exemplars,
        'EXEMPLAR_SELECTION_METHOD': 'herding',
        'GRIDSEARCH_TASKS': -1,
        'NUM_EPOCHS': epochs,
        'LR': 0.1,
        'LR_MIN': 1e-4,
        'LR_FACTOR': 3,
        'LR_PATIENCE': 5,
        'CLIPPING': 10000,
        # 'MOMENTUM': 0.0,
        'WEIGHT_DECAY': 0.0,
        'WARMUP_NEPOCHS': 0,
        'WARMUP_LR_FACTOR': 1.0,
        'MULTI_SOFTMAX': False,
        'FIX_BN': False,
        'EVAL_ON_TRAIN': False,
        'NUM_WORKERS': 4,
        'PIN_MEMORY': False,
    },

    'r_walk': {
        'NETWORK': 'resnet32',
        'BATCH_SIZE': batch_size,
        'NUM_EXEMPLARS_PER_CLASS': 0,
        'MAX_NUM_EXEMPLARS': exemplars,
        'EXEMPLAR_SELECTION_METHOD': 'distance',
        'GRIDSEARCH_TASKS': -1,
        'NUM_EPOCHS': epochs,
        'LR': 0.1,
        'LR_MIN': 1e-4,
        'LR_FACTOR': 3,
        'LR_PATIENCE': 5,
        'CLIPPING': 10000,
        # 'MOMENTUM': 0.0,
        'WEIGHT_DECAY': 0.0,
        'WARMUP_NEPOCHS': 0,
        'WARMUP_LR_FACTOR': 1.0,
        'MULTI_SOFTMAX': False,
        'FIX_BN': False,
        'EVAL_ON_TRAIN': True,
        'NUM_WORKERS': 4,
        'PIN_MEMORY': False,
    },

    'path_integral': {
        'NETWORK': 'resnet32',
        'BATCH_SIZE': batch_size,
        'NUM_EXEMPLARS_PER_CLASS': 0,
        'MAX_NUM_EXEMPLARS': exemplars,
        'EXEMPLAR_SELECTION_METHOD': 'herding',
        'GRIDSEARCH_TASKS': -1,
        'NUM_EPOCHS': epochs,
        'LR': 0.1,
        'LR_MIN': 1e-4,
        'LR_FACTOR': 3,
        'LR_PATIENCE': 5,
        'CLIPPING': 10000,
        # 'MOMENTUM': 0.0,
        'WEIGHT_DECAY': 0.0,
        'WARMUP_NEPOCHS': 0,
        'WARMUP_LR_FACTOR': 1.0,
        'MULTI_SOFTMAX': False,
        'FIX_BN': False,
        'EVAL_ON_TRAIN': True,
        'NUM_WORKERS': 4,
        'PIN_MEMORY': False,
    },

#
    'ewc': {
        'NETWORK': 'resnet32',
        'BATCH_SIZE': batch_size,
        'NUM_EXEMPLARS_PER_CLASS': 0,
        'MAX_NUM_EXEMPLARS': exemplars,
        'EXEMPLAR_SELECTION_METHOD': 'herding',
        'GRIDSEARCH_TASKS': -1,
        'NUM_EPOCHS': epochs,
        'LR': 0.1,
        'LR_MIN': 1e-4,
        'LR_FACTOR': 3,
        'LR_PATIENCE': 5,
        'CLIPPING': 10000,
        # 'MOMENTUM': 0.0,
        'WEIGHT_DECAY': 0.0,
        'WARMUP_NEPOCHS': 0,
        'WARMUP_LR_FACTOR': 1.0,
        'MULTI_SOFTMAX': False,
        'FIX_BN': False,
        'EVAL_ON_TRAIN': False,
        'NUM_WORKERS': 4,
        'PIN_MEMORY': False,
    },
    'il2m': {
        'NETWORK': 'resnet32',
        'BATCH_SIZE': batch_size,
        'NUM_EXEMPLARS_PER_CLASS': 0,
        'MAX_NUM_EXEMPLARS': exemplars,
        'EXEMPLAR_SELECTION_METHOD': 'herding',
        'GRIDSEARCH_TASKS': -1,
        'NUM_EPOCHS': epochs,
        'LR': 0.1,
        'LR_MIN': 1e-4,
        'LR_FACTOR': 3,
        'LR_PATIENCE': 5,
        'CLIPPING': 10000,
        # 'MOMENTUM': 0.0,
        'WEIGHT_DECAY': 0.0,
        'WARMUP_NEPOCHS': 0,
        'WARMUP_LR_FACTOR': 1.0,
        'MULTI_SOFTMAX': False,
        'FIX_BN': False,
        'EVAL_ON_TRAIN': False,
        'NUM_WORKERS': 4,
        'PIN_MEMORY': False,
    },
    'bic': {
        'NETWORK': 'resnet32',
        'BATCH_SIZE': 50,
        'NUM_EXEMPLARS_PER_CLASS': 0,
        'MAX_NUM_EXEMPLARS': 3000,
        'EXEMPLAR_SELECTION_METHOD': 'herding',
        'GRIDSEARCH_TASKS': -1,
        'NUM_EPOCHS': 10,
        'LR': 0.1,
        'LR_MIN': 1e-4,
        'LR_FACTOR': 3,
        'LR_PATIENCE': 5,
        'CLIPPING': 10000,
        'MOMENTUM': 0.0,
        'WEIGHT_DECAY': 0.0,
        'WARMUP_NEPOCHS': 0,
        'WARMUP_LR_FACTOR': 1.0,
        'MULTI_SOFTMAX': False,
        'FIX_BN': False,
        'EVAL_ON_TRAIN': True,
        'NUM_WORKERS': 4,
        'PIN_MEMORY': False,
    },
    'dmc': {
        'NETWORK': 'resnet32',
        'BATCH_SIZE': 50,
        'NUM_EXEMPLARS_PER_CLASS': 0,
        'MAX_NUM_EXEMPLARS': 0,
        'EXEMPLAR_SELECTION_METHOD': 'herding',
        'GRIDSEARCH_TASKS': -1,
        'NUM_EPOCHS': 10,
        'LR': 0.1,
        'LR_MIN': 1e-4,
        'LR_FACTOR': 3,
        'LR_PATIENCE': 5,
        'CLIPPING': 10000,
        'MOMENTUM': 0.0,
        'WEIGHT_DECAY': 0.0,
        'WARMUP_NEPOCHS': 0,
        'WARMUP_LR_FACTOR': 1.0,
        'MULTI_SOFTMAX': False,
        'FIX_BN': False,
        'EVAL_ON_TRAIN': True,
        'NUM_WORKERS': 4,
        'PIN_MEMORY': False,
    },

    'lucir': {
        'NETWORK': 'resnet32',
        'BATCH_SIZE': 80,
        'NUM_EXEMPLARS_PER_CLASS': 0,
        'MAX_NUM_EXEMPLARS': 3000,
        'EXEMPLAR_SELECTION_METHOD': 'herding',
        'GRIDSEARCH_TASKS': -1,
        'NUM_EPOCHS': 15,
        'LR': 0.1,
        'LR_MIN': 1e-4,
        'LR_FACTOR': 3,
        'LR_PATIENCE': 5,
        'CLIPPING': 10000,
        # 'MOMENTUM': 0.0,
        'WEIGHT_DECAY': 0.0,
        'WARMUP_NEPOCHS': 0,
        'WARMUP_LR_FACTOR': 1.0,
        'MULTI_SOFTMAX': False,
        'FIX_BN': False,
        'EVAL_ON_TRAIN': True,
        'NUM_WORKERS': 4,
        'PIN_MEMORY': False,
    },
'joint': {
        'NETWORK': 'resnet32',
        'BATCH_SIZE': batch_size,
        'NUM_EXEMPLARS_PER_CLASS': 0,
        'MAX_NUM_EXEMPLARS': 0,
        'EXEMPLAR_SELECTION_METHOD': 'herding',
        'GRIDSEARCH_TASKS': -1,
        'NUM_EPOCHS': epochs,
        'LR': 0.1,
        'LR_MIN': 1e-4,
        'LR_FACTOR': 3,
        'LR_PATIENCE': 5,
        'CLIPPING': 10000,
        # 'MOMENTUM': 0.0,
        'WEIGHT_DECAY': 0.0,
        'WARMUP_NEPOCHS': 0,
        'WARMUP_LR_FACTOR': 1.0,
        'MULTI_SOFTMAX': False,
        'FIX_BN': False,
        'EVAL_ON_TRAIN': False,
        'NUM_WORKERS': 4,
        'PIN_MEMORY': False,
    },
    'freezing': {
        'NETWORK': 'resnet32',
        'BATCH_SIZE': 120,
        'NUM_EXEMPLARS_PER_CLASS': 0,
        'MAX_NUM_EXEMPLARS': exemplars,
        'EXEMPLAR_SELECTION_METHOD': 'herding',
        'GRIDSEARCH_TASKS': -1,
        'NUM_EPOCHS': epochs,
        'LR': 0.1,
        'LR_MIN': 1e-4,
        'LR_FACTOR': 3,
        'LR_PATIENCE': 5,
        'CLIPPING': 10000,
        # 'MOMENTUM': 0.0,
        'WEIGHT_DECAY': 0.0,
        'WARMUP_NEPOCHS': 0,
        'WARMUP_LR_FACTOR': 1.0,
        'MULTI_SOFTMAX': False,
        'FIX_BN': False,
        'EVAL_ON_TRAIN': False,
        'NUM_WORKERS': 4,
        'PIN_MEMORY': False,
    },
    'mas': {
        'NETWORK': 'resnet32',
        'BATCH_SIZE': batch_size,
        'NUM_EXEMPLARS_PER_CLASS': 0,
        'MAX_NUM_EXEMPLARS': exemplars,
        'EXEMPLAR_SELECTION_METHOD': 'herding',
        'GRIDSEARCH_TASKS': -1,
        'NUM_EPOCHS': epochs,
        'LR': 0.1,
        'LR_MIN': 1e-4,
        'LR_FACTOR': 3,
        'LR_PATIENCE': 5,
        'CLIPPING': 10000,
        # 'MOMENTUM': 0.0,
        'WEIGHT_DECAY': 0.0,
        'WARMUP_NEPOCHS': 0,
        'WARMUP_LR_FACTOR': 1.0,
        'MULTI_SOFTMAX': False,
        'FIX_BN': False,
        'EVAL_ON_TRAIN': False,
        'NUM_WORKERS': 4,
        'PIN_MEMORY': False,
    },
    'lwf': {
        'NETWORK': 'resnet32',
        'BATCH_SIZE': batch_size,
        'NUM_EXEMPLARS_PER_CLASS': 0,
        'MAX_NUM_EXEMPLARS': exemplars,
        'EXEMPLAR_SELECTION_METHOD': 'herding',
        'GRIDSEARCH_TASKS': -1,
        'NUM_EPOCHS': epochs,
        'LR': 0.1,
        'LR_MIN': 1e-4,
        'LR_FACTOR': 3,
        'LR_PATIENCE': 5,
        'CLIPPING': 10000,
        # 'MOMENTUM': 0.0,
        'WEIGHT_DECAY': 0.0,
        'WARMUP_NEPOCHS': 0,
        'WARMUP_LR_FACTOR': 1.0,
        'MULTI_SOFTMAX': False,
        'FIX_BN': False,
        'EVAL_ON_TRAIN': False,
        'NUM_WORKERS': 4,
        'PIN_MEMORY': False,
    },
    'lwm': {
        'NETWORK': 'resnet32',
        'BATCH_SIZE': batch_size,
        'NUM_EXEMPLARS_PER_CLASS': 0,
        'MAX_NUM_EXEMPLARS': exemplars,
        'EXEMPLAR_SELECTION_METHOD': 'herding',
        'GRIDSEARCH_TASKS': -1,
        'NUM_EPOCHS': epochs,
        'LR': 0.1,
        'LR_MIN': 1e-4,
        'LR_FACTOR': 3,
        'LR_PATIENCE': 5,
        'CLIPPING': 10000,
        # 'MOMENTUM': 0.0,
        'WEIGHT_DECAY': 0.0,
        'WARMUP_NEPOCHS': 0,
        'WARMUP_LR_FACTOR': 1.0,
        'MULTI_SOFTMAX': False,
        'FIX_BN': False,
        'EVAL_ON_TRAIN': False,
        'NUM_WORKERS': 4,
        'PIN_MEMORY': False,
    },

    'eeil': {
            'NETWORK': 'resnet32',
            'BATCH_SIZE': batch_size,
            'NUM_EXEMPLARS_PER_CLASS': 0,
            'MAX_NUM_EXEMPLARS': exemplars,
            'EXEMPLAR_SELECTION_METHOD': 'herding',
            'GRIDSEARCH_TASKS': -1,
            'NUM_EPOCHS': epochs,
            'LR': 0.1,
            'LR_MIN': 1e-4,
            'LR_FACTOR': 3,
            'LR_PATIENCE': 5,
            'CLIPPING': 10000,
            # 'MOMENTUM': 0.0,
            'WEIGHT_DECAY': 0.0,
            'WARMUP_NEPOCHS': 0,
            'WARMUP_LR_FACTOR': 1.0,
            'MULTI_SOFTMAX': False,
            'FIX_BN': False,
            'EVAL_ON_TRAIN': False,
            'NUM_WORKERS': 4,
            'PIN_MEMORY': False,
        },
}

DATABASE = "malware"
number_of_adversarial_examples_pr_attack = 2000
base_settings = {
    "malware": {
        'number_of_classes': 10,
        'x_train': 'X_train_ustc.npy',
        'x_test': 'X_test_ustc.npy',
        'y_train': 'y_train_ustc.npy',
        'y_test': 'y_train_ustc.npy',
        'taskcla' : [(0, 10), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1)]
    },
    "cicids": {
        'number_of_classes': 9,
        'x_train': 'X_train_cicids.npy',
        'x_test': 'X_test_cicids.npy',
        'y_train': 'y_train_cicids.npy',
        'y_test': 'y_test_cicids.npy',
        'taskcla' : [(0, 9), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1)]
    }
}
config = base_settings[DATABASE]
base_classes_number = config['number_of_classes']
RESULT_PATH = './results/'
VALIDATION_SIZE = 2000
SAVE_MODELS = False
LOG = ['disk']
GPU = 0
LAST_LAYER_ANALYSIS = True
MAX_ADV_PER_EPSILON = 2000
EPSILONS = [
    0.03,
    0.1,
    0.3,
    0.5,
]
