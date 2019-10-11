//弹出框水平垂直居中
    (window.onresize = function () {
        var win_height = $(window).height();
        var win_width = $(window).width();
        if (win_width <= 768){
            $(".tailoring-content").css({
                "top": (win_height - $(".tailoring-content").outerHeight())/2,
                "left": 0
            });
        }else{
            $(".tailoring-content").css({
                "top": (win_height - $(".tailoring-content").outerHeight())/2,
                "left": (win_width - $(".tailoring-content").outerWidth())/2
            });
        }
    })();

    //弹出图片裁剪框
    $("#replaceImg").on("click",function () {
        $(".tailoring-container").toggle();
        $('#tailoringImg').cropper("enable");
        $("#message").html('<span class="ml-2">只支持JPG、PNG, 大小不超过2.5M.</span>')
    });
    //图像上传
    function selectImg(file) {
        if (!file.files || !file.files[0]){
            return;
        }

        // 类型检查
        var up_types = new Array("image/jpg","image/jpeg","image/png");
        if (up_types.indexOf(file.files[0].type) > -1){
            $("#message").html('<span class="ml-2 text-info">编辑后保存上传.</span>')
        }else{
            $("#message").html('<span class="ml-2 text-warning">格式错误, 只支持JPG、PNG.</span>')
            return;
        }

        // 检查大小，限制2.5M内
        if (file.files[0].size/1024 > 2500){
            $("#message").html('<span class="ml-2 text-warning">图片大小不能超过2.5M.</span>')
            return;
        }

        var reader = new FileReader();
        reader.onload = function (evt) {
            var replaceSrc = evt.target.result;
            //更换cropper的图片
            $('#tailoringImg').cropper('replace', replaceSrc,false);//默认false，适应高度，不失真
        }
        reader.readAsDataURL(file.files[0]);
    }
    //cropper图片裁剪
    $('#tailoringImg').cropper({
        aspectRatio: 1/1,//默认比例
        preview: '.previewImg',//预览视图
        guides: false,  //裁剪框的虚线(九宫格)
        autoCropArea: 0.5,  //0-1之间的数值，定义自动剪裁区域的大小，默认0.8
        movable: false, //是否允许移动图片
        dragCrop: true,  //是否允许移除当前的剪裁框，并通过拖动来新建一个剪裁框区域
        movable: true,  //是否允许移动剪裁框
        cropBoxResizable: true,  //是否允许改变裁剪框的大小
        zoomable: false,  //是否允许缩放图片大小
        rotatable: true,  //是否允许旋转图片
        crop: function(e) {
            // 输出结果数据裁剪图像。
        }
    });
    //旋转
    $(".cropper-rotate-btn").on("click",function () {
        $('#tailoringImg').cropper("rotate", 45);
    });
    //复位
    $(".cropper-reset-btn").on("click",function () {
        $('#tailoringImg').cropper("reset");
    });
    //换向
    var flagX = true;
    $(".cropper-scaleX-btn").on("click",function () {
        if(flagX){
            $('#tailoringImg').cropper("scaleX", -1);
            flagX = false;
        }else{
            $('#tailoringImg').cropper("scaleX", 1);
            flagX = true;
        }
        flagX != flagX;
    });

    //裁剪后 上传
    $("#sureCut").on("click",function () {
        if ($("#tailoringImg").attr("src") == null ){
            return false;
        }else{
            $('#tailoringImg').cropper('getCroppedCanvas').toBlob(function(blob) {
                var formData = new FormData();
                formData.append('croppedImage', blob);

                $("#message").html('<span class="ml-2 text-primary">正在上传，请稍候</span>')
                $.ajax({
                    url: "/user/upload_avatar/",
                    type: "POST",
                    processData: false,
                    contentType: false,
                    data: formData,
                    success: function (data){
                        if (data["success"]) {
                            $("#message").html('<span class="ml-2 text-success">上传成功!</span>')
                            document.getElementById('finalImg').src=data["avatar_url"]+"?t=" + Math.random();
                            setTimeout(function(){
                                closeTailor();
                            },300)
                        }else{
                            var new_html = '<span class="">'
                            new_html += data["message"]
                            new_html += '</span>'
                            $("#message").html(new_html)
                        };
                    },
                    error: function() {
                         $("#message").html('<span class="ml-2 text-danger">上传错误</span>')
                    }
                });

             });
        }
    });
    //关闭裁剪框
    function closeTailor() {
        $('#tailoringImg').cropper("reset");
        $('#tailoringImg').cropper("disable");
        $(".tailoring-container").toggle();
    }