class FormProduto(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('nome', 'descricao', 'preco', 'estoque', 'imagem')  # 'estoque' adicionado
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control'}),
            'estoque': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'imagem': forms.FileInput(attrs={'accept': 'image/*'})
        }
