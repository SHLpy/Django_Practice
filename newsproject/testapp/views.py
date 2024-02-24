from django.shortcuts import render

# Create your views here.
def movies_info(request):
    head_masg = 'Movies Information'
    sub_msg1 = 'Eagle movie was nice.....'
    sub_msg2 = 'OG will come very soon.....'
    sub_msg3 = 'Planning for Aashiqui-3 with Mahesh sir & Sunny Leone.....'
    my_dict = {'head_msg':head_masg, 'sub_msg1':sub_msg1, 'sub_msg2':sub_msg2, 'sub_msg3':sub_msg3}
    return render(request,'testapp/news.html',my_dict)

def sports_info(request):
    head_masg = 'Sports Information'
    sub_msg1 = 'Yesterday There Was No Matches...'
    sub_msg2 = 'Upcoming IPL will start March-23rd'
    sub_msg3 = 'Kabaddi Kabaddi'
    type = 'sports'
    my_dict = {'head_msg':head_masg, 'sub_msg1':sub_msg1, 'sub_msg2':sub_msg2, 'sub_msg3':sub_msg3,'type':type}
    return render(request,'testapp/news.html',my_dict)

def politics_info(request):
    head_masg = 'Politics Information'
    sub_msg1 = 'Telangana CM Revanth Reddy'
    sub_msg2 = 'Upcoming CM for Ap ???????'
    sub_msg3 = 'If u r not getting Django join the politics.....Become MLA.......'
    type = 'politics'
    my_dict = {'head_msg':head_masg, 'sub_msg1':sub_msg1, 'sub_msg2':sub_msg2, 'sub_msg3':sub_msg3,'type':type}
    return render(request,'testapp/news.html',my_dict)


