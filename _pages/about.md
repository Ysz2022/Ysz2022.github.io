---
permalink: /
title: " "
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

Currently, I am a 4th-year Ph.D. student in Computer Science, School of Electronic and Computer Engineering, <img src="/files/PKU.png" alt="PKU" width="20.842" height="20"> [Peking University](https://www.pku.edu.cn/), supervised by [Prof. Jian Zhang](https://jianzhang.tech/). Previously, I received my B.Eng degree of software engineering from <img src="/files/DLUT.png" alt="DLUT" width="20.842" height="20"> [Dalian University of Technology](https://en.dlut.edu.cn/) in 2022. During my undergraduate studies, I am privileged to work closely with [Prof. Risheng Liu](https://rsliu.tech/) and [Prof. Xin Fan](https://scholar.google.com/citations?user=vLN1njoAAAAJ&hl=zh-CN) in the field of low-level vision.

My primary research interests include computer vision, diffusion model, and machine learning, mainly focusing on video-related Artificial Intelligence Generated Content (AIGC), Low-level Vision, and Novel View Synthesis. You are welcome to contact me via my email: szyang AT stu DOT pku DOT edu DOT cn

# 📜 Research Area
1. Video-related AIGC
2. Novel View Synthesis
3. Low-level Vision

# 📝 Selected Publications
<style type="text/css">
    /* Color scheme stolen from Sergey Karayev */
    a {
    color: #1772d0;
    text-decoration:none !important;
    }
    a:focus, a:hover {
    color: #f09228;
    text-decoration:none !important;
    }
    table,td,th,tr{
    	border:none !important;
    }
    body,td,th,tr,p,a {
    font-family: 'Lato', Verdana, Helvetica, sans-serif;
    font-size: 14px
    }
    strong {
    font-family: 'Lato', Verdana, Helvetica, sans-serif;
    font-size: 14px;
    }
    heading {
    font-family: 'Lato', Verdana, Helvetica, sans-serif;
    font-size: 22px;
    }
    papertitle {
    font-family: 'Lato', Verdana, Helvetica, sans-serif;
    font-size: 14px;
    font-weight: 700
    }
    papertitle_just {
    font-family: 'Lato', Verdana, Helvetica, sans-serif;
    font-size: 14px;
    font-weight: 700;
    text-align: justify
    }
    name {
    font-family: 'Lato', Verdana, Helvetica, sans-serif;
    font-size: 32px;
    }
    .one
    {
    width: 160px;
    height: 160px;
    position: relative;
    }
    .two
    {
    width: 160px;
    height: 160px;
    position: absolute;
    transition: opacity .2s ease-in-out;
    -moz-transition: opacity .2s ease-in-out;
    -webkit-transition: opacity .2s ease-in-out;
    }
    .fade {
     transition: opacity .2s ease-in-out;
     -moz-transition: opacity .2s ease-in-out;
     -webkit-transition: opacity .2s ease-in-out;
    }
    span.highlight {
        background-color: #ffffd0;
    }
</style>
<!-- ################################  CONTENT START  ##################################################-->
<table width="100%" align="center" border="0" cellspacing="0" cellpadding="10">
<tbody>
&ensp;Equal Contribution†, Corresponding Author*, [<font color=GoldenRod>J</font>] Journal, [<font color=GoldenRod>C</font>] Conference
<!-- ###################################################################################################-->
<tr onmouseout="gencompositor_stop()" onmouseover="gencompositor_start()" >
<td width="20%">
<div class="one">
<div class="two" id = 'gencompositor_image'><img src='./files/gencompositor_after.gif'></div>
<img src='./files/gencompositor_before.gif'>
</div>
<script type="text/javascript">
function gencompositor_start() {
document.getElementById('gencompositor_image').style.opacity = "1";
}
function gencompositor_stop() {
document.getElementById('gencompositor_image').style.opacity = "0";
}
gencompositor_stop()
</script>
</td>
<td valign="top" width="80%">
  <a href="https://arxiv.org/abs/2509.02460">
    <papertitle_just>GenCompositor: Generative Video Compositing with Diffusion Transformer</papertitle_just>     
  </a>
  <br>
  <strong>Shuzhou Yang</strong>, Xiaoyu Li, Xiaodong Cun, Guangzhi Wang, Lingen Li, Ying Shan, Jian Zhang*.
  <br>
<em>Preprint</em>, 2025 <br>
<a href="https://arxiv.org/abs/2509.02460">arXiv</a>
|
<a href="https://gencompositor.github.io/">Project Page</a>
|
<a href="https://github.com/TencentARC/GenCompositor">Code<img src="https://img.shields.io/github/stars/TencentARC/GenCompositor?style=social&label=Stars"></a>
<p></p>
<p>The prioneer work that enables effortlessly compositing different videos guided by user-specified trajectories and scales.</p>
</td>
</tr>
<!-- ###################################################################################################-->
  
<!-- ###################################################################################################-->
<tr onmouseout="d4vd_stop()" onmouseover="d4vd_start()" >
<td width="20%">
<div class="one">
<div class="two" id = '4dvd_image'><img src='./files/4dvd_after.gif'></div>
<img src='./files/4dvd_before.gif'>
</div>
<script type="text/javascript">
function d4vd_start() {
document.getElementById('4dvd_image').style.opacity = "1";
}
function d4vd_stop() {
document.getElementById('4dvd_image').style.opacity = "0";
}
d4vd_stop()
</script>
</td>
<td valign="top" width="80%">
  <a href="https://arxiv.org/abs/2508.04467">
    <papertitle_just>4DVD: Cascaded Dense-view Video Diffusion Model for High-quality 4D Content Generation</papertitle_just>     
  </a>
  <br>
  <strong>Shuzhou Yang</strong>, Xiaodong Cun, Xiaoyu Li*, Yaowei Li, Jian Zhang*.
  <br>
<em>Preprint</em>, 2025 <br>
<a href="https://arxiv.org/abs/2508.04467">arXiv</a>
|
<a href="https://4dvd.github.io/">Project Page</a>
<p></p>
<p>Generating dense-view videos through cascaded diffusion model.</p>
</td>
</tr>
<!-- ###################################################################################################-->
  
<!-- ###################################################################################################-->
<tr onmouseout="fourier123_stop()" onmouseover="fourier123_start()" >
<td width="20%">
<div class="one">
<div class="two" id = 'fourier123_image'><img src='./files/fourier123_after.gif'></div>
<img src='./files/fourier123_before.png'>
</div>
<script type="text/javascript">
function fourier123_start() {
document.getElementById('fourier123_image').style.opacity = "1";
}
function fourier123_stop() {
document.getElementById('fourier123_image').style.opacity = "0";
}
fourier123_stop()
</script>
</td>
<td valign="top" width="80%">
  <a href="https://arxiv.org/abs/2405.20669">
    <papertitle_just>Hybrid Fourier Score Distillation for Efficient One Image to 3D Object Generation</papertitle_just>     
  </a>
  <br>
  <strong>Shuzhou Yang</strong>, Yu Wang, Haijie Li, Jiarui Meng, Yanmin Wu, Xiandong Meng, Jian Zhang*.
  <br>
<em>Visual Intelligence (<font color=GoldenRod>VI</font>)</em> [<font color=GoldenRod>J</font>], 2025 <br>
<a href="https://arxiv.org/abs/2405.20669">arXiv</a>
|
<a href="https://link.springer.com/article/10.1007/s44267-025-00089-8">Paper</a>
|
<a href="https://fourier1-to-3.github.io/">Project Page</a>
|
<a href="https://github.com/Ysz2022/Fourier123">Code<img src="https://img.shields.io/github/stars/Ysz2022/Fourier123?style=social&label=Stars"></a>
<p></p>
<p>Using both 2D and 3D diffusion models to generate 3D asset from a single image with hybrid fourier score distillation.</p>
</td>
</tr>
<!-- ###################################################################################################-->
  
<!-- ###################################################################################################-->
<tr onmouseout="nvedit_stop()" onmouseover="nvedit_start()" >
<td width="20%">
<div class="one">
<div class="two" id = 'nvedit_image'><img src='./files/nvedit_after.gif'></div>
<img src='./files/nvedit_before.gif'>
</div>
<script type="text/javascript">
function nvedit_start() {
document.getElementById('nvedit_image').style.opacity = "1";
}
function nvedit_stop() {
document.getElementById('nvedit_image').style.opacity = "0";
}
nvedit_stop()
</script>
</td>
<td valign="top" width="80%">
  <a href="https://arxiv.org/abs/2312.08882">
    <papertitle_just>Neural Video Fields Editing</papertitle_just>     
  </a>
  <br>
  <strong>Shuzhou Yang</strong>, Chong Mou, Jiwen Yu, Yuhan Wang, Xiandong Meng, Jian Zhang*.
  <br>
<em>Computational Visual Media (<font color=GoldenRod>CVMJ</font>)</em> [<font color=GoldenRod>J</font>], 2025 <br>
<a href="https://arxiv.org/abs/2312.08882">arXiv</a>
|
<a href="https://nvedit.github.io/">Project Page</a>
|
<a href="https://github.com/Ysz2022/NVEdit">Code<img src="https://img.shields.io/github/stars/Ysz2022/NVEdit?style=social&label=Stars"></a>
<p></p>
<p>Editing long videos coherently via neural video fields.</p>
</td>
</tr>
<!-- ###################################################################################################-->
  
<!-- ###################################################################################################-->
<tr onmouseout="difflle_stop()" onmouseover="difflle_start()" >
<td width="20%">
<div class="one">
<div class="two" id = 'difflle_image'><img src='./files/difflle_after.png'></div>
<img src='./files/difflle_before.png'>
</div>
<script type="text/javascript">
function difflle_start() {
document.getElementById('difflle_image').style.opacity = "1";
}
function difflle_stop() {
document.getElementById('difflle_image').style.opacity = "0";
}
difflle_stop()
</script>
</td>
<td valign="top" width="80%">
  <a href="https://link.springer.com/article/10.1007/s11263-024-02292-4">
    <papertitle_just>DiffLLE: Diffusion-based Domain Calibration for Weak Supervised Low-light Image Enhancement</papertitle_just>     
  </a>
  <br>
  <strong>Shuzhou Yang</strong>†, Xuanyu Zhang†, Yinhuai Wang, Jiwen Yu, Yuhan Wang, Jian Zhang*.
  <br>
<em>International Journal of Computer Vision (<font color=GoldenRod>IJCV</font>)</em> [<font color=GoldenRod>J</font>], 2024 <br>
<a href="https://arxiv.org/abs/2308.09279">arXiv</a>
|
<a href="https://link.springer.com/article/10.1007/s11263-024-02292-4">Paper</a>
<p></p>
<p>Bridge the gap between real scenes and training data by diffusion model prior.</p>
</td>
</tr>
<!-- ###################################################################################################-->

<!-- ###################################################################################################-->
<tr onmouseout="nerco_stop()" onmouseover="nerco_start()" >
<td width="20%">
<div class="one">
<div class="two" id = 'nerco_image'><img src='./files/nerco_after.png'></div>
<img src='./files/nerco_before.png'>
</div>
<script type="text/javascript">
function nerco_start() {
document.getElementById('nerco_image').style.opacity = "1";
}
function nerco_stop() {
document.getElementById('nerco_image').style.opacity = "0";
}
nerco_stop()
</script>
</td>
<td valign="top" width="80%">
  <a href="https://openaccess.thecvf.com/content/ICCV2023/html/Yang_Implicit_Neural_Representation_for_Cooperative_Low-light_Image_Enhancement_ICCV_2023_paper.html">
    <papertitle_just>Implicit Neural Representation for Cooperative Low-light Image Enhancement</papertitle_just>     
  </a>
  <br>
  <strong>Shuzhou Yang</strong>, Moxuan Ding, Yanmin Wu, Zihan Li, Jian Zhang*.
  <br>
<em>International Conference on Computer Vision (<font color=GoldenRod>ICCV</font>)</em> [<font color=GoldenRod>C</font>], 2023 <br>
<a href="https://arxiv.org/abs/2303.11722">arXiv</a>
|
<a href="https://openaccess.thecvf.com/content/ICCV2023/html/Yang_Implicit_Neural_Representation_for_Cooperative_Low-light_Image_Enhancement_ICCV_2023_paper.html">Paper</a>
|
<a href="https://github.com/Ysz2022/NeRCo">Code<img src="https://img.shields.io/github/stars/Ysz2022/NeRCo?style=social&label=Stars"></a>
<p></p>
<p>Normalize images by neural representation and enhance them based on CLIP prior.</p>
</td>
</tr>
<!-- ###################################################################################################-->

<!-- ###################################################################################################-->
<tr onmouseout="sepc_stop()" onmouseover="sepc_start()" >
<td width="20%">
<div class="one">
<div class="two" id = 'sepc_image'><img src='./files/sepc_after.png'></div>
<img src='./files/sepc_before.png'>
</div>
<script type="text/javascript">
function sepc_start() {
document.getElementById('sepc_image').style.opacity = "1";
}
function sepc_stop() {
document.getElementById('sepc_image').style.opacity = "0";
}
sepc_stop()
</script>
</td>
<td valign="top" width="80%">
  <a href="https://ieeexplore.ieee.org/document/10363208">
    <papertitle_just>Multi-scale Synergism Ensemble Progressive and Contrastive Investigation for Image Restoration</papertitle_just>     
  </a>
  <br>
  Zhiying Jiang†, <strong>Shuzhou Yang</strong>†, Jinyuan Liu, Xin Fan, Risheng Liu*.
  <br>
<em>IEEE Transactions on Instrumentation and Measurement (<font color=GoldenRod>TIM</font>)</em> [<font color=GoldenRod>J</font>], 2023 <br>
<a href="https://ieeexplore.ieee.org/document/10363208">Paper</a>
|
<a href="https://github.com/Ysz2022/SEPC">Code</a>
<p></p>
<p>Restore image degradation through a multi-scale progressive network.</p>
</td>
</tr>
<!-- ###################################################################################################-->

<!-- ###################################################################################################-->
<tr onmouseout="nerfocus_stop()" onmouseover="nerfocus_start()" >
<td width="20%">
<div class="one">
<div class="two" id = 'nerfocus_image'><img src='./files/nerfocus_after.png'></div>
<img src='./files/nerfocus_before.png'>
</div>
<script type="text/javascript">
function nerfocus_start() {
document.getElementById('nerfocus_image').style.opacity = "1";
}
function nerfocus_stop() {
document.getElementById('nerfocus_image').style.opacity = "0";
}
nerfocus_stop()
</script>
</td>
<td valign="top" width="80%">
  <a href="https://arxiv.org/abs/2203.05189">
    <papertitle_just>NeRFocus: Neural Radiance Field for 3D Synthetic Defocus</papertitle_just>     
  </a>
  <br>
  Yinhuai Wang†, <strong>Shuzhou Yang</strong>†, Yujie Hu, Jian Zhang*.
  <br>
<em>Computer Vision and Pattern Recognition Workshop (<font color=GoldenRod>CVPRW</font>)</em> [<font color=GoldenRod>C</font>], 2023 <br>
<a href="https://arxiv.org/abs/2203.05189">arXiv</a>
|
<a href="https://github.com/wyhuai/NeRFocus">Code</a>
<p></p>
<p>Realize defocusing effect in 3D scenarios.</p>
</td>
</tr>
<!-- ###################################################################################################-->
</tbody></table>

# 💻 Academic Services
- Journal Reviewer:
  - IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI)
  - International Journal of Computer Vision (IJCV)
  - IEEE Transactions on Image Processing (TIP)
  - IEEE Transactions on Multimedia (TMM)
  - IEEE Transactions on Circuits and Systems for Video Technology (TCSVT)
  - ACM Transactions on Multimedia Computing, Communications and Applications (TOMM)
  - IEEE Journal of Selected Topics in Signal Processing (JSTSP)
- Conference Reviewer: CVPR, ICCV, ECCV, NeurIPS, ICML, ICLR, Siggraph, AAAI, etc.

# 🎖️ Selected Honors
- [2025] Peking University May Fourth Scholarship. 🏆️
- [2023&2025] Outstanding Student Award at Peking University.
- [2019-2021] The First Class Excellence Scholarship at Dalian University of Technology.

# 🏫 Educations
- Sep'2022-Jul'2027: Ph.D. (Computer Science), <img src="/files/PKU.png" alt="PKU" width="20.842" height="20"> Peking University
- Sep'2018-Jul'2022: B.Eng (Software Engineering), <img src="/files/DLUT.png" alt="DLUT" width="20.842" height="20"> Dalian University of Technology
