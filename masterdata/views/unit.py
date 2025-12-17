from django.contrib import messages
from masterdata.models import Unit
from masterdata.forms.unit import UnitAddForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def unit_list(request):
    units = Unit.objects.all()

    fields = [field.name for field in Unit._meta.fields]

    return render(
        request,
        'masterdata/unit/list.html',
        {
            'units': units,
            'fields': fields,
        }
    )

@login_required
def unit_add(request):
    form = UnitAddForm()
    
    if request.method == 'POST':
        form = UnitAddForm(request.POST)
        if form.is_valid():
            name=form['name'].value()
            symbol=form['symbol'].value()
            is_active=form['is_active'].value()
            user=request.user

            if Unit.objects.filter(name=name).exists():
                messages.error(request, 'Unidade de medida já cadastrada')
                return redirect('unit:add')
            unit = Unit.objects.create(
                name=name,
                symbol=symbol,
                is_active=is_active,
                created_by=user,
                updated_by=user
            )
            unit.save()
            messages.success(request, f'Unidade de medida {name} cadastrada com sucesso!')
            return redirect('unit:list')
    return render(request, 'masterdata/unit/add.html', {'form':form})