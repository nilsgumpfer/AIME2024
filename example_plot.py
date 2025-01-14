import os

from signxai.methods.wrappers import calculate_relevancemap

from utils.data import load_and_preprocess_ecg
from utils.explainability import normalize_ecg_relevancemap
from utils.model import load_models_from_paths
from utils.viz import plot_ecg


def run(record_id, subsample_start=0, plot_dir='./examples/.ecgs', filetype='png'):
    # Generate plot dir
    os.makedirs(plot_dir, exist_ok=True)

    # Load ECG
    ecg = load_and_preprocess_ecg(record_id=record_id,
                                  ecg_filters=['BWR', 'BLA', 'AC50Hz', 'LP40Hz'],
                                  subsampling_window_size=2000,
                                  subsample_start=subsample_start)

    # Plot preparation
    os.makedirs(plot_dir, exist_ok=True)
    save_to = '{}/{}.{}'.format(plot_dir, record_id, filetype)

    # Plot ECG with explanation
    plot_ecg(ecg=ecg,
             title=record_id,
             save_to=save_to)



if __name__ == '__main__':
    run('03509_hr')
    run('12131_hr')
    run('14493_hr')
    run('02906_hr')