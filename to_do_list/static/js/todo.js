/**
 * Created by jinlinlin on 2016/6/24.
 */
    $(function(){
//        alert('this is a test');
//        alert($("#checkbox1").is(':checked'));

//        $("#checkbox1").click(function(){
//            alert('test');
//            alert($(this).is(':checked'));
//            if($(this).is(':checked')==true){
//                alert('选中了');
//                $(this).closest('.list-group-item').addClass('completed_item');
//            }else{
//                alert('取消选中');
//                $(this).closest('.list-group-item').removeClass('completed_item');
//            };
//        });

//{# 复选框操作，完成时，添加中间线，并且更改复选框对应编辑表单input-value为1，自动点击提交按钮；取消时相反       #}
        $("ol input[type='checkbox']").click(function(){
            var check_input = $(this).closest('.list-group-item').find('.check_input');
            if($(this).is(':checked')==true){
                alert('又完成一项工作，放松一下吧！');
                 check_input.attr('value','1');
                $(this).closest('.list-group-item').find('.p1').addClass('completed_item');
                $(this).closest('.list-group-item').find('.check_button').trigger('click');

            }else{
                alert('你确定要重新开始这个工作吗？');
                check_input.attr('value','0');
                $(this).closest('.list-group-item').find('.p1').removeClass('completed_item');
                $(this).closest('.list-group-item').find('.check_button').trigger('click');
            }
        });

//{# 删除数据时，调用数据到删除表单的input       #}
        $('.p_form button').click(function(){
            var value1 = $(this).closest('.text_holder').find('.p1').text();
            $(this).closest('.p_form').find('.p_input').attr('value',value1)
        });

//{#编辑按钮触发，显示需要输入的input，同时将原数据插入到另一input，以提交update-filter时使用        #}
        $('.edit').click(function(){
            var p = $(this).closest('.list-group-item').find('.p1');
            p.css('display', 'none');
            var inp = $(this).closest('.list-group-item').find('.li_input');
            var inp1 = $(this).closest('.list-group-item').find('.li_input1');
            inp.attr('value', p.text());
            inp1.attr('value', p.text());
            $(this).closest('.list-group-item').find('.in_form').css('display', 'block');
        });

//{#网页加载后，根据数据库state的数据，确定复选框操作        #}
         $(document).ready(function(){
            $("input[name='check_input']").each(function(){
                var val_check = $(this).val();
                var check = $(this).closest('.checkbox').find('.pull-right');
                if(val_check == 'True'){
                    check.attr('checked','checked');
                    $(this).closest('.list-group-item').find('.p1').addClass('completed_item');
                }
            })
         });

//{#正则验证        #}
//    {# 添加时的验证       #}
        $("input[name='add_list']").click(function(){
            var str = $(this).closest('.label_addlist').find('.form-control').val();
            var ret = /\S/;
            if(ret.test(str)==false){
                alert('您输入的内容为空，请重新输入');
                return false;
            };
        });

        //{# 编辑时的验证       #}
        $(".in_button").click(function(){
            var str = $(this).closest('.in_form').find('.li_input').val();
            var ret = /\S/;
            if(ret.test(str)==false){
                alert('您输入的内容为空，请重新输入');
                return false;
            };
        });
    });