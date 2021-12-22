# Widget
"""
attrs - A dictionary containing HTML attributes to be set on the rendered widget. If you assing a value of True or False to an attribute, it will be rendered as an HTML5 boolean attribute.
It basically use to give class and ID to that field.

Like :- attrs = {'class':'somecss1', 'id':'uniqueid'}

Example :- 
feedback = forms.CharField(widget=forms.TextInput(attrs={'class':'somecss1 somecss2','id':'uniqueid'}))

BuildIn Widget
<input type="text"> - name = forms.CharField(widget=forms.TextInput)

<input type="number"> - NumberInput
<input type="email"> - EmailInput
<input type="url"> - URLInput
<input type="password"> - PasswordInput
input_type: 'hidden' - HiddenInput
input_type: 'text' - DateInput
input_type: 'text' - DateTimeInput
input_type: 'text' - TimeInput
textarea - Textarea
input_type: 'checkbox' - CheckboxInput
<input type="file" ...> - FileInput
SelectDateWidget 
"""
