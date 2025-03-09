from flask import Flask,request,render_template,session,url_for,flash,redirect
from fpdf import FPDF

store={}

header='REGINA CAELI SECONDARY SCHOOL OMOR'

address='P.O.BOX: 100, Ayamelum LGA, Anambra state'

exam='  2025 Entrance Exam Registration (2025-EER) Slip  '

bord= 'ADDMISSION AND GRADUATION BOARD'



app=Flask(__name__)


@app.route('/')
def home():
    return render_template('HOME.html')
    


@app.route('/about')
def about():
    return render_template('ABOUT.html')



@app.route('/portal')
def portal():
    return render_template('PORTAL.html')
    

    
@app.route('/support')
def support():
    return render_template('SUPPORT.html')
    

@app.route('/registration',methods=['POST','GET'])
def registration():
    if request.method=='POST':
        surname=request.form.get('surname')
        store['surname']=surname
        firstname=request.form.get('firstname')
        store['firstname']=firstname
        lastname=request.form.get('lastname')
        store['lastname']=lastname
        DOB=request.form.get('DOB')
        store['DOB']=DOB
        address=request.form.get('address')
        store['address']=address
        lga=request.form.get('lga')
        store['lga']=lga
        state=request.form.get('state')
        store['state']=state
        past_school=request.form.get('previous_school')
        school_address=request.form.get('school_address')
        school_state=request.form.get('school_state')
        yr_graduation=request.form.get('yr_graduation')
        first_school=request.form.get('first_school')
        guidan=request.form.get('pgn')
        guidan_numb=request.form.get('pgnu')
        guidan_state=request.form.get('pgs')
        Reg_mode=request.form.get('Reg')
        
       #adding form print

        class PDF(FPDF):
            def header(self):
        #add board name header
                self.set_font('times','B',25)
                self.set_text_color('#1E1670')
                doc_w=self.w
                bord_w=self.get_string_width(bord)
        
                self.set_x((doc_w-bord_w)/2)
                self.cell(bord_w,16,bord,align='C')
                self.ln(8)
        
        #add school header
                self.set_font('times','B',25)
                self.set_text_color('#1E1670')
                doc_w=self.w
                txt_w=self.get_string_width(header)
        
                self.set_x((doc_w-txt_w)/2)
                self.cell(txt_w,25,header,align='C')
                self.ln(12)
        
        
       #add address of school
                self.set_font('times','I',21)
                self.cell(0,25,address,align='C')
                self.ln(26)
        
        #add exam name or type
                self.set_font('times','B',22)
                self.set_fill_color('#1E1670')
                self.set_text_color(255,255,255)
                exam_w=self.get_string_width(exam)
                self.set_x((doc_w-exam_w)/2)
                self.cell(exam_w,10,exam,border=0,align='C',fill=1,ln=1)
                self.ln(10)
        
        #add double line
                self.set_font('times','B',45)
                self.line(5,self.y,doc_w-5,self.y)
                self.ln(2)
                self.line(5,self.y,doc_w-5,self.y)
                self.ln(8)
        
        
 #instatiate FPDF object       
        pdf=PDF('L','mm',(399,238))

#add our page
        pdf.add_page()

#add personal details header
        pdf.set_font('times','BU',26)
        pdf.set_text_color(0,0,0)
        doc_w=pdf.w
        pdf.cell(0,16,'Candidate Details',align='C',ln=1)
        pdf.ln(5)


#canditate infos
        pdf.set_text_color('#1E1670')
        pdf.set_font('times','B',20)
        pdf.cell(90,16,'NAMES:',align='L')
        pdf.cell(0,16,'Obiorah Chigozie Patrick',align='L',ln=1)

        pdf.ln(1)

        pdf.set_font('times','B',20)
        pdf.cell(90,16,'DATE OF BIRTH:',align='L')
        pdf.cell(0,16,'19/01/2006',align='L',ln=1)

        pdf.ln(1)

        pdf.set_font('times','B',20)
        pdf.cell(90,16,'ADDRESS:',align='L')
        pdf.cell(0,16,'Akanator Omor',align='L',ln=1)

        pdf.ln(1)

        pdf.set_font('times','B',20)
        pdf.cell(90,16,'LGA OF ORIGIN:',align='L')
        pdf.cell(0,16,'Ayamelum',align='L',ln=1)

        pdf.ln(1)

        pdf.set_font('times','B',20)
        pdf.cell(90,16,'STATE OF ORIGIN:',align='L')
        pdf.cell(0,16,'Anambra',align='L',ln=1)

        pdf.ln(5)

#adding break line
        pdf.set_font('times','B',45)
        pdf.line(5,pdf.y,doc_w-5,pdf.y)
        pdf.ln(2)
        pdf.line(5,pdf.y,doc_w-5,pdf.y)
        pdf.ln(5)

#add education details
        pdf.set_font('times','BU',26)
        pdf.set_text_color(0,0,0)
        doc_w=pdf.w
        pdf.cell(0,16,'Candidate Education Details',align='C',ln=1)
        pdf.ln(5)


#add education infos
        pdf.set_font('times','B',20)
        pdf.set_text_color('#1E1678')

        pdf.cell((doc_w/2)+15,15,'PREVIOUS SCHOOL',align='L')
        pdf.cell(0,15,'CERTIFICATION IN SCHOOL',align='R',ln=1)
        pdf.ln(1)


        pdf.set_font('times','',18)
        pdf.set_text_color('#1E1670')

        pdf.cell((doc_w/2),15,'Christ The King Primary School Omor',align='L')
        pdf.cell(0,15,'FSLC & NCEEC',align='L',ln=1)

        pdf.cell((doc_w/2),15,'Year: 2012',align='L')
        pdf.cell(0,15,'Year: 2012',align='L',ln=1)


#adding break line
        pdf.set_font('times','B',45)
        pdf.line(5,pdf.y,doc_w-5,pdf.y)
        pdf.ln(2)
        pdf.line(5,pdf.y,doc_w-5,pdf.y)
        pdf.ln(5)

        

        pdf.output('form.pdf')
        
        
        return redirect(url_for('form'))
    return render_template('REGISTRATION.html')
    
@app.route('/form',methods=['GET'])
def form():
    return render_template('FORM.html',store=store)

if __name__=='__main__':
    app.run()