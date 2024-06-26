'''
โมเดล User เป็นตัวแทนของผู้ใช้ในระบบการยืนยันตัวตนของ Django 
โดยมีฟิลด์พื้นฐาน เช่น username, password, email ฯลฯ
'''
from django.contrib.auth.models import User
'''
UserCreationForm เป็นฟอร์มที่ Django เตรียมไว้สำหรับการลงทะเบียนผู้ใช้ใหม่ 
โดยมีฟิลด์เช่น username, password1, password2 เพื่อให้ผู้ใช้กรอกข้อมูลในการลงทะเบียน
'''
from django.contrib.auth.forms import UserCreationForm
'''
โมดูล forms ใช้สำหรับการสร้างและจัดการฟอร์มใน Django
คุณสามารถสร้างฟอร์มใหม่โดยการสืบทอดจาก forms.Form 
หรือ forms.ModelForm และกำหนดฟิลด์ต่างๆ ตามที่ต้องการใช้งาน
'''
from django import forms

# นำเข้าโมเดลข้อมูลรีวิว
from .models import Review

class ReviewForm(forms.ModelForm):
    # เพิ่ม widget สำหรับให้ผู้ใช้กรอกข้อความ และกำหนดจำนวนตัวอักษรสูงสุด
    text = forms.CharField(
        label='ข้อความ',  # เปลี่ยน Text เป็น ข้อความ
        widget=forms.Textarea(attrs={'rows': 1, 'cols': 10, 'class': 'form-control'}),
    )

    class Meta:
        model = Review
        fields = ['text', 'rating']
        labels = {
            'rating': 'คะแนน'  # เปลี่ยน Rating เป็น คะแนน
        }
        widgets = {
            'rating': forms.NumberInput(attrs={'step': '1', 'min': '1', 'max': '5', 'class': 'form-control'})
        }

# สร้างแบบฟอร์มสำหรับการค้นหาและเก็บข้อมูลล่าสุดที่ค้นหาไว้ในตัวแปร 'search_query'
class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=255)

# สร้างแบบฟอร์มสำหรับสมัครสมาชิก
class SignUpForm(UserCreationForm):
	# email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'กรุณากรอก Email ของท่าน'}))
	# first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'กรุณากรอกชื่อของท่าน'}))
	# last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'กรุณากรอกนามสกุลของท่าน'}))

	class Meta:
		model = User
		fields = ('username', 'password1', 'password2')
		# fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'กรุณากรอก Username ของท่าน เช่น myusername1234@.+-_'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>ต้องการขั้นต่ำ 4 ตัวอักษรหรือน้อยกว่า 150 กรุณาพิมพ์ด้วยตัวอักษร ตัวเลข และตัวอักษรพิเศษ เช่น @/./+/-/_ เท่านั้นครับ</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'กรุณากรอก Password ของท่าน'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>รหัสผ่านของคุณต้องไม่เหมือนกับข้อมูลส่วนบุคคลอื่นๆ ของคุณมากเกินไป</li><li>รหัสผ่านของคุณต้องมีอย่างน้อย 8 ตัวอักษร</li><li>รหัสผ่านของคุณต้องไม่ใช่รหัสผ่านที่ใช้กันทั่วไป</li><li>รหัสผ่านของคุณต้องไม่เป็นตัวเลขทั้งหมด</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'กรุณากรอก Password อีกครั้ง'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>กรุณาป้อนรหัสผ่านอีกครั้งเพื่อการยืนยันการสมัครสมาชิก</small></span>'

	# def __init__(self, *args, **kwargs):
	# 	super(SignUpForm, self).__init__(*args, **kwargs)

	# 	self.fields['username'].widget.attrs['class'] = 'form-control'
	# 	self.fields['username'].widget.attrs['placeholder'] = 'กรุณากรอก Username ของท่านเป็นภาษาอังกฤษ เช่น Username1234'
	# 	self.fields['username'].label = ''
	# 	self.fields['username'].help_text = '<span class="form-text text-muted"><small>กรุณากรอกเป็นภาษาอังกฤษ ต้องการขั้นต่ำ 150 ตัวอักษรหรือน้อยกว่า กรุณาพิมพ์ด้วยตัวอักษร ตัวเลข และตัวอักษรพิเศษ เช่น @/./+/-/_ เท่านั้นครับ</small></span>'

	# 	self.fields['password1'].widget.attrs['class'] = 'form-control'
	# 	self.fields['password1'].widget.attrs['placeholder'] = 'กรุณากรอก Password ของท่าน'
	# 	self.fields['password1'].label = ''
	# 	self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>รหัสผ่านของคุณต้องไม่เหมือนกับข้อมูลส่วนบุคคลอื่นๆ ของคุณมากเกินไป</li><li>รหัสผ่านของคุณต้องมีอย่างน้อย 8 ตัวอักษร</li><li>รหัสผ่านของคุณต้องไม่ใช่รหัสผ่านที่ใช้กันทั่วไป</li><li>รหัสผ่านของคุณต้องไม่เป็นตัวเลขทั้งหมด</li></ul>'

	# 	self.fields['password2'].widget.attrs['class'] = 'form-control'
	# 	self.fields['password2'].widget.attrs['placeholder'] = 'กรุณากรอก Password อีกครั้ง'
	# 	self.fields['password2'].label = ''
	# 	self.fields['password2'].help_text = '<span class="form-text text-muted"><small>กรุณาป้อนรหัสผ่านอีกครั้งเพื่อการยืนยันการสมัครสมาชิก</small></span>'