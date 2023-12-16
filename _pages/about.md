---
permalink: /
title: " "
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---
# 👋 Hi!
My name is Shuzhou Yang, and I am a 2nd-year Ph.D. student in <img src="/files/PKU.png" alt="PKU" width="20.842" height="20"> Computer Science, [Peking University](https://www.pku.edu.cn/), supervised by [Prof. Jian Zhang](https://jianzhang.tech/). Previously, I received my B.Eng degree from <img src="/files/DLUT.png" alt="DLUT" width="20.842" height="20"> [Dalian University of Technology](https://en.dlut.edu.cn/) in 2022.

My primary research interests include Computer Vision and Deep Learning, mainly focusing on Artificial Intelligence Generative Content (AIGC), and Low-level Vision.

# 📜 Research Area
1. AIGC
2. Low-level Vision

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
<em>Preprint</em>, 2023 <br>
<a href="https://arxiv.org/abs/2312.08882">arXiv</a>
|
<a href="https://nvedit.github.io/">Project Page</a>
|
<a href="https://github.com/Ysz2022/NVEdit">code<img src="https://img.shields.io/github/stars/Ysz2022/NVEdit?style=social&label=Stars"></a>
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
  <a href="https://arxiv.org/abs/2308.09279">
    <papertitle_just>DiffLLE: Diffusion-guided Domain Calibration for Unsupervised Low-light Image Enhancement</papertitle_just>     
  </a>
  <br>
  <strong>Shuzhou Yang</strong>†, Xuanyu Zhang†, Yinhuai Wang, Jiwen Yu, Yuhan Wang, Jian Zhang*.
  <br>
<em>Preprint</em>, 2023 <br>
<a href="https://arxiv.org/abs/2308.09279">arXiv</a>
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
  <a href="https://arxiv.org/abs/2303.11722">
    <papertitle_just>Implicit Neural Representation for Cooperative Low-light Image Enhancement</papertitle_just>     
  </a>
  <br>
  <strong>Shuzhou Yang</strong>, Moxuan Ding, Yanmin Wu, Zihan Li, Jian Zhang*.
  <br>
<em>International Conference on Computer Vision (ICCV)</em>, 2023 <br>
<a href="https://arxiv.org/abs/2303.11722">arXiv</a>
|
<a href="https://openaccess.thecvf.com/content/ICCV2023/html/Yang_Implicit_Neural_Representation_for_Cooperative_Low-light_Image_Enhancement_ICCV_2023_paper.html">Paper</a>
|
<a href="https://github.com/Ysz2022/NeRCo">code<img src="https://img.shields.io/github/stars/Ysz2022/NeRCo?style=social&label=Stars"></a>
<p></p>
<p>Normalize images by neural representation and enhance them based on CLIP prior.</p>
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
  Yinhuai Wang†, <strong>Shuzhou Yang</strong>†, Yujie Hu, Xinhua Cheng, Jian Zhang*.
  <br>
<em>Computer Vision and Pattern Recognition Workshop (CVPRW)</em>, 2023 <br>
<a href="https://arxiv.org/abs/2203.05189">arXiv</a>
|
<a href="https://github.com/wyhuai/NeRFocus">code<img src="https://img.shields.io/github/stars/wyhuai/NeRFocus?style=social&label=Stars"></a>
<p></p>
<p>Realize defocusing effect in 3D scenarios.</p>
</td>
</tr>
<!-- ###################################################################################################-->
</tbody></table>


# 🏫 Educations
- Sep'2022-Jul'2027: Ph.D. (Computer Science), <img src="/files/PKU.png" alt="PKU" width="20.842" height="20"> Peking University
- Sep'2018-Jul'2022: B.Eng (Software Engineering), <img src="/files/DLUT.png" alt="DLUT" width="20.842" height="20"> Dalian University of Technology


# 💻 Academic Services
- Reviewer: IEEE TMM
