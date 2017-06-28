from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import TextInput
from tethys_sdk.gizmos import Button

@login_required()
def home(request):
    """
    Controller for the app home page.
    """

    context = {}

    return render(request, 'sprint/home.html', context)

def info(request):
    """
    Controller for the app home page.
    """
    context = {}

    return render(request, 'sprint/info.html', context)

def map(request):
    """
    Controller for the app home page.
    """
    context = {}

    return render(request, 'sprint/map.html', context)

def gizmo(request):
    """
    Controller for the app home page.
    """
    if request.POST:
            runoff = float(request.POST['runoff'])
            intensity = float(request.POST['intensity'])
            area = float(request.POST['area'])
            flow = runoff * intensity * area

    text_input1 = TextInput(display_text='Runoff Coeficient, c',
                            name='runoff',
                            initial='0.8', )

    text_input2 = TextInput(display_text='Rainfall Intensity, i [in/hr]',
                            name='intensity',
                            initial='6', )

    text_input3 = TextInput(display_text='Drainage Area, A [acre]',
                            name='area',
                            initial='160', )

    single_button = Button(display_text='Calculate Flow',
                           name='flow',
                           attributes='form=flow-form',
                           submit=True)

    context = {'single_button': single_button, 'text_input1': text_input1, 'text_input2': text_input2, 'text_input3': text_input3}

    return render(request, 'sprint/gizmo.html', context)

def flow(request):
    """
    Controller for the app home page.
    """
    if request.POST:
        runoff = float(request.POST['runoff'])
        intensity = float(request.POST['intensity'])
        area = float(request.POST['area'])
        flow = runoff * intensity * area
    context = {'runoff': runoff, 'intensity': intensity, 'area': area, 'flow': flow}

    return render(request, 'sprint/flow.html', context)