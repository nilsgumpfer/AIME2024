# AIME2024
Towards Trustworthy AI in Cardiology - Supplementary Material (AIME2024)

% --- AVB ---

## Atrioventricular block

![AVB_gradient](./examples/AVB/AVB_gradient.png)
*ECG subsample from PTB-XL (Wagner et al. 2020) with heatmap overlay (red) based on XAI method Gradient (Zurada et al.) for predicted class _atrioventricular block_ (prob. 97%).*

![AVB_gradient_x_input](./examples/AVB/AVB_gradient_x_input.png)
*ECG subsample from PTB-XL (Wagner et al. 2020) with heatmap overlay (red) based on XAI method Gradient×Input (Shrikumar et al. 2017) for predicted class _atrioventricular block_ (prob. 97%).*

![AVB_gradient_x_sign](./examples/AVB/AVB_gradient_x_sign.png)
*ECG subsample from PTB-XL (Wagner et al. 2020) with heatmap overlay (red) based on XAI method Gradient×SIGN (Gumpfer et al. 2023) for predicted class _atrioventricular block_ (prob. 97%).*

![AVB_lrp_alpha_1_beta_0](./examples/AVB/AVB_lrp_alpha_1_beta_0.png)
*ECG subsample from PTB-XL (Wagner et al. 2020) with heatmap overlay (red) based on XAI method LRP-α₁β₀ (Bach et al. 2015) for predicted class _atrioventricular block_ (prob. 97%).*

![AVB_lrp_epsilon_0_5_std_x](./examples/AVB/AVB_lrp_epsilon_0_5_std_x.png)
*ECG subsample from PTB-XL (Wagner et al. 2020) with heatmap overlay (red) based on XAI method LRP-ε with ε = 0.5 ⋅ σ(x) (Bach et al. 2015) for predicted class _atrioventricular block_ (prob. 97%).*

![AVB_lrpsign_epsilon_0_5_std_x](./examples/AVB/AVB_lrpsign_epsilon_0_5_std_x.png)
*ECG subsample from PTB-XL (Wagner et al. 2020) with heatmap overlay (red) based on XAI method LRP-ε SIGN with ε = 0.5 ⋅ σ(x) and SIGN as input layer rule (Gumpfer et al. 2023) for predicted class _atrioventricular block_ (prob. 97%).*

![AVB_deep_shap](./examples/AVB/AVB_deep_shap.png)
*ECG subsample from PTB-XL (Wagner et al. 2020) with heatmap overlay (red) based on XAI method DeepSHAP (Lundberg et al.) for predicted class _atrioventricular block_ (prob. 97%).*

![AVB_grad_shap](./examples/AVB/AVB_grad_shap.png)
*ECG subsample from PTB-XL (Wagner et al. 2020) with heatmap overlay (red) based on XAI method GradSHAP (Lundberg et al.) for predicted class _atrioventricular block_ (prob. 97%).*

![AVB_grad_cam_timeseries](./examples/AVB/AVB_grad_cam_timeseries.png)
*ECG subsample from PTB-XL (Wagner et al. 2020) with heatmap overlay (red) based on XAI method Grad-CAM [Selvaraju2020] for predicted class _atrioventricular block_ (prob. 97%).*


% --- ISCH ---

## Myocardial ischemia

![ISCH_gradient](ISCH_gradient.png)
*ECG subsample from PTB-XL (Wagner et al. 2020) with heatmap overlay (red) based on XAI method Gradient (Zurada et al.) for predicted class _myocardial ischemia_ (prob. 69%).*

![ISCH_gradient_x_input](ISCH_gradient_x_input.png)
*ECG subsample from PTB-XL (Wagner et al. 2020) with heatmap overlay (red) based on XAI method Gradient×Input (Shrikumar et al. 2017) for predicted class _myocardial ischemia_ (prob. 69%).*

![ISCH_gradient_x_sign](ISCH_gradient_x_sign.png)
*ECG subsample from PTB-XL (Wagner et al. 2020) with heatmap overlay (red) based on XAI method Gradient×SIGN (Gumpfer et al. 2023) for predicted class _myocardial ischemia_ (prob. 69%).*

![ISCH_lrp_alpha_1_beta_0](ISCH_lrp_alpha_1_beta_0.png)
*ECG subsample from PTB-XL (Wagner et al. 2020) with heatmap overlay (red) based on XAI method LRP-α₁β₀ (Bach et al. 2015) for predicted class _myocardial ischemia_ (prob. 69%).*

![ISCH_lrp_epsilon_0_5_std_x](ISCH_lrp_epsilon_0_5_std_x.png)
*ECG subsample from PTB-XL (Wagner et al. 2020) with heatmap overlay (red) based on XAI method LRP-ε with ε = 0.5 ⋅ σ(x) (Bach et al. 2015) for predicted class _myocardial ischemia_ (prob. 69%).*

![ISCH_lrpsign_epsilon_0_5_std_x](ISCH_lrpsign_epsilon_0_5_std_x.png)
*ECG subsample from PTB-XL (Wagner et al. 2020) with heatmap overlay (red) based on XAI method LRP-ε SIGN with ε = 0.5 ⋅ σ(x) and SIGN as input layer rule (Gumpfer et al. 2023) for predicted class _myocardial ischemia_ (prob. 69%).*

![ISCH_deep_shap](ISCH_deep_shap.png)
*ECG subsample from PTB-XL (Wagner et al. 2020) with heatmap overlay (red) based on XAI method DeepSHAP (Lundberg et al.) for predicted class _myocardial ischemia_ (prob. 69%).*

![ISCH_grad_shap](ISCH_grad_shap.png)
*ECG subsample from PTB-XL (Wagner et al. 2020) with heatmap overlay (red) based on XAI method GradSHAP (Lundberg et al.) for predicted class _myocardial ischemia_ (prob. 69%).*

![ISCH_grad_cam_timeseries](ISCH_grad_cam_timeseries.png)
*ECG subsample from PTB-XL (Wagner et al. 2020) with heatmap overlay (red) based on XAI method Grad-CAM [Selvaraju2020] for predicted class _myocardial ischemia_ (prob. 69%).*


% --- RBBB ---

## Right bundle branch block

![RBBB_gradient](RBBB_gradient.png)
*ECG subsample from PTB-XL (Wagner et al. 2020) with heatmap overlay (red) based on XAI method Gradient (Zurada et al.) for predicted class _right bundle branch block_ (prob. 99%).*

![RBBB_gradient_x_input](RBBB_gradient_x_input.png)
*ECG subsample from PTB-XL (Wagner et al. 2020) with heatmap overlay (red) based on XAI method Gradient×Input (Shrikumar et al. 2017) for predicted class _right bundle branch block_ (prob. 99%).*

![RBBB_gradient_x_sign](RBBB_gradient_x_sign.png)
*ECG subsample from PTB-XL (Wagner et al. 2020) with heatmap overlay (red) based on XAI method Gradient×SIGN (Gumpfer et al. 2023) for predicted class _right bundle branch block_ (prob. 99%).*

![RBBB_lrp_alpha_1_beta_0](RBBB_lrp_alpha_1_beta_0.png)
*ECG subsample from PTB-XL (Wagner et al. 2020) with heatmap overlay (red) based on XAI method LRP-α₁β₀ (Bach et al. 2015) for predicted class _right bundle branch block_ (prob. 99%).*

![RBBB_lrp_epsilon_0_5_std_x](RBBB_lrp_epsilon_0_5_std_x.png)
*ECG subsample from PTB-XL (Wagner et al. 2020) with heatmap overlay (red) based on XAI method LRP-ε with ε = 0.5 ⋅ σ(x) (Bach et al. 2015) for predicted class _right bundle branch block_ (prob. 99%).*

![RBBB_lrpsign_epsilon_0_5_std_x](RBBB_lrpsign_epsilon_0_5_std_x.png)
*ECG subsample from PTB-XL (Wagner et al. 2020) with heatmap overlay (red) based on XAI method LRP-ε SIGN with ε = 0.5 ⋅ σ(x) and SIGN as input layer rule (Gumpfer et al. 2023) for predicted class _right bundle branch block_ (prob. 99%).*

![RBBB_deep_shap](RBBB_deep_shap.png)
*ECG subsample from PTB-XL (Wagner et al. 2020) with heatmap overlay (red) based on XAI method DeepSHAP (Lundberg et al.) for predicted class _right bundle branch block_ (prob. 99%).*

![RBBB_grad_shap](RBBB_grad_shap.png)
*ECG subsample from PTB-XL (Wagner et al. 2020) with heatmap overlay (red) based on XAI method GradSHAP (Lundberg et al.) for predicted class _right bundle branch block_ (prob. 99%).*

![RBBB_grad_cam_timeseries](RBBB_grad_cam_timeseries.png)
*ECG subsample from PTB-XL (Wagner et al. 2020) with heatmap overlay (red) based on XAI method Grad-CAM [Selvaraju2020] for predicted class _right bundle branch block_ (prob. 99%).*


% --- LBBB ---

## Left bundle branch block

![LBBB_gradient](LBBB_gradient.png)
*ECG subsample from PTB-XL (Wagner et al. 2020) with heatmap overlay (red) based on XAI method Gradient (Zurada et al.) for predicted class _left bundle branch block_ (prob. 98%).*

![LBBB_gradient_x_input](LBBB_gradient_x_input.png)
*ECG subsample from PTB-XL (Wagner et al. 2020) with heatmap overlay (red) based on XAI method Gradient×Input (Shrikumar et al. 2017) for predicted class _left bundle branch block_ (prob. 98%).*

![LBBB_gradient_x_sign](LBBB_gradient_x_sign.png)
*ECG subsample from PTB-XL (Wagner et al. 2020) with heatmap overlay (red) based on XAI method Gradient×SIGN (Gumpfer et al. 2023) for predicted class _left bundle branch block_ (prob. 98%).*

![LBBB_lrp_alpha_1_beta_0](LBBB_lrp_alpha_1_beta_0.png)
*ECG subsample from PTB-XL (Wagner et al. 2020) with heatmap overlay (red) based on XAI method LRP-α₁β₀ (Bach et al. 2015) for predicted class _left bundle branch block_ (prob. 98%).*

![LBBB_lrp_epsilon_0_5_std_x](LBBB_lrp_epsilon_0_5_std_x.png)
*ECG subsample from PTB-XL (Wagner et al. 2020) with heatmap overlay (red) based on XAI method LRP-ε with ε = 0.5 ⋅ σ(x) (Bach et al. 2015) for predicted class _left bundle branch block_ (prob. 98%).*

![LBBB_lrpsign_epsilon_0_5_std_x](LBBB_lrpsign_epsilon_0_5_std_x.png)
*ECG subsample from PTB-XL (Wagner et al. 2020) with heatmap overlay (red) based on XAI method LRP-ε SIGN with ε = 0.5 ⋅ σ(x) and SIGN as input layer rule (Gumpfer et al. 2023) for predicted class _left bundle branch block_ (prob. 98%).*

![LBBB_deep_shap](LBBB_deep_shap.png)
*ECG subsample from PTB-XL (Wagner et al. 2020) with heatmap overlay (red) based on XAI method DeepSHAP (Lundberg et al.) for predicted class _left bundle branch block_ (prob. 98%).*

![LBBB_grad_shap](LBBB_grad_shap.png)
*ECG subsample from PTB-XL (Wagner et al. 2020) with heatmap overlay (red) based on XAI method GradSHAP (Lundberg et al.) for predicted class _left bundle branch block_ (prob. 98%).*

![LBBB_grad_cam_timeseries](LBBB_grad_cam_timeseries.png)
*ECG subsample from PTB-XL (Wagner et al. 2020) with heatmap overlay (red) based on XAI method Grad-CAM [Selvaraju2020] for predicted class _left bundle branch block_ (prob. 98%).*
