import datetime
from calendar import month
from urllib import response
from datetime import datetime, timedelta
from django.contrib import messages
from django.shortcuts import render,redirect
from .models import *
from errno import ETIME
from datetime import date
from re import S
from re import A, S
from this import s
from unittest import signals
from webbrowser import get
from django.db.models.functions import Coalesce
from xml.etree.ElementTree import tostring
from django.db.models import Sum
from cgi import print_arguments
from multiprocessing import context
from symtable import Symbol
from unicodedata import name
from urllib import request
from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import JsonResponse
from django.db.models.functions import TruncDay
from django.db.models.functions import TruncMonth
from django.db.models.functions import TruncDate
from django.db.models.functions import Extract
from django.db.models import Count
# Create your views here.

def base(request):
    return render(request, 'base.html')

#......................jisha........................

def company_list(request):
    com=Companies.objects.all()
    return render(request,'company_list.html',{'comp':com})    

def change_company(request):
	com=Companies.objects.all()
	return render(request, 'change_company.html',{'comp':com})

def select_c(request):
	com = Companies.objects.all()
	return render(request,'select_c.html',{'com':com})

def shut_cmpny(request):
	com=Companies.objects.all() 
	return render(request, 'shut_cmpny.html',{'com':com})

def shut(request,pk):
    c=Companies.objects.get(id=pk)
    c.status=False
    c.save()
    return redirect('shut_cmpny') 

def enable(request,pk):
    c=Companies.objects.get(id=pk)
    c.status=True
    c.save()
    return redirect('/')

def ledgers(request,pk):
	grp=tally_group.objects.all()
	com=Companies.objects.get(id=pk) 
	return render(request,'ledgers.html',{'grp' : grp,'cmp':com})

def vouchers(request,pk):
	com=Companies.objects.get(id=pk) 
	return render(request, 'vouchers.html',{'cmp':com})

def groups(request):
	com=Companies.objects.filter(status=True) 
	return render(request, 'group.html',{'com':com})

def group_alt(request):
    return render(request, 'group_alt.html')

def currency(request,pk):
    cmp=Companies.objects.get(id=pk)
    return render(request, 'currency.html',{'cmp':cmp})

def c_create(request,pk):
    cmp=Companies.objects.get(id=pk)
    return render(request, 'c_create.html',{'cmp':cmp})

def c_alter(request,pk):
    cmp=Companies.objects.get(id=pk)
    return render(request, 'c_alter.html',{'cmp':cmp})

def cost(request):
	costt=cost_centre.objects.all()
	return render(request,'cost.html',{'costt' : costt})

def cost_alt(request):
	costt=cost_centre.objects.all()
	return render(request, 'cost_alt.html',{'costt' : costt})

def rates(request):
	ccr=currencyAlteration.objects.all()
	context={'ccr' : ccr}
	return render(request,'rates.html',context)

def create_cmpny(request):
    return render(request, 'create_cmpny.html')

def tally_gst(request,pk):
	company=Companies.objects.get(id=pk)
	return render(request, 'gst.html',{'company':company})

def gst_tax(request,pk):
	company=Companies.objects.get(id=pk)
	return render(request, 'gst_tax.html',{'company':company})

def features(request):
	return render(request, 'features.html')

def tds(request,pk):
	comp=Companies.objects.get(id=pk)
	return render(request, 'tds.html',{'company':comp})    

def person(request,pk):
	comp=Companies.objects.get(id=pk)
	return render(request, 'tds_person.html',{'company':comp})
    
def c_rates(request):
    return render(request, 'c_rates.html')

def bank_details(request):
	bn = bank_name.objects.all()
	return render(request,'bank_details.html',{'bn' : bn})

def lut_bond(request):
    return render(request, 'lut_bond.html')

def cheque(request):
    return render(request, 'cheque.html')

def ledger_gst(request):
    return render(request, 'ledger_gst.html')

def ledger_chequed(request):
    return render(request, 'ledger_chequed.html')

def vouch_advance(request,pk):
    cmp=Companies.objects.get(id=pk)
    return render(request, 'vouch_advance.html',{'cmp':cmp})

def ledger_taxgst(request):
    return render(request, 'ledger_taxgst.html')

def b_name(request):
	comp=Companies.objects.all()
	return render(request,'bankname.html',{'comp':comp})

def create_group(request):
	if request.method=='POST':
		gname=request.POST['gname']
		galias=request.POST['alias']
		under=request.POST['group']
		nature=request.POST['group_nature']
		gross=request.POST['gorss_profit']
		ledg=request.POST['ledger']
		cred=request.POST['debit/credit']
		calc=request.POST['calculation']
		invc=request.POST['invoice']
		grp=tally_group(group_name=gname,
                group_alias=galias,
                group_under=under,
                nature=nature,
                gross_profit=gross,
                sub_ledger=ledg,
                debit_credit=cred,
                calculation=calc,
                invoice=invc,
                )          
		grp.save()
		print("added")
		return redirect('/')

def create_currency(request,pk):
	if request.method=='POST':
		cmp=Companies.objects.get(id=pk)
		smbl=request.POST['c_symbl']
		fname=request.POST['fname']
		isoc=request.POST['isocode']
		dcml=request.POST['decimal_p']
		amt=request.POST['show_amt']
		sfx=request.POST['suffix']
		spc=request.POST['add_space']
		wrd=request.POST['word_rep']
		ndcml=request.POST['no_decimal']
		crny=currencyAlteration(Symbol=smbl,
                        FormalName = fname,
                        ISOCurrency = isoc,
                        DecimalPlace = dcml,
                        showAmount = amt,
                        suffixSymbol = sfx,
                        AddSpace = spc,
                        wordRep = wrd,
                        DecimalWords = ndcml,company=cmp)          
		crny.save()
		print("added")
		return redirect('/')

def create_ROE(request,pk):
	if request.method=='POST':
		cmp=Companies.objects.get(id=pk)
		# dt=request.POST['dt']
		crname=request.POST['curname']
		stdr=request.POST['stdr']
		# lv=request.POST['lvr']
		ssr=request.POST['ssr']
		# lv1=request.POST['lvr2']
		bsr=request.POST['bsr']
		croe=rateofexchange(
                        currencyName = crname,
                        std_rate = stdr,
                        
                        sell_specified_rate = ssr,
						
                        buy_voucher_rate = bsr,company=cmp)          
		croe.save()
		return redirect('/')

def alter_currency(request,pk):
	if request.method=='POST':
		cmp=Companies.objects.get(id=pk)
		smbl=request.POST['c_symbl']
		fname=request.POST['fname']
		isoc=request.POST['isocode']
		dcml=request.POST['decimal_p']
		amt=request.POST['show_amt']
		sfx=request.POST['suffix']
		spc=request.POST['add_space']
		wrd=request.POST['word_rep']
		ndcml=request.POST['no_decimal']
		crny=company_alt_currency(c_symbol=smbl,
                        formal_name = fname,
                        iso_Ccode = isoc,
                        decimal_place = dcml,
                        show_amtM = amt,
                        suffix_smblA = sfx,
                        add_space = spc,
                        word_rep = wrd,
                        no_decimal = ndcml,company=cmp)          
		crny.save()
		print("added")
		return redirect('/')

def load_centre(request):
	if request.method=='POST':
		nm=request.POST['cst_name']
		als=request.POST['alias']
		unr=request.POST['c_under']
		cost=cost_centre(cname=nm,
                        cost_alias = als,
                        under = unr)          
		cost.save()
		print("added")
		return render(request,'cost.html')
		

def create_tds(request,pk):
	id=Companies.objects.get(id=pk)
	if request.method=='POST':
		t_reg = request.POST['tan_reg_no']
		tax_clct = request.POST['tax_ded_clctn']
		ded_type = request.POST['deductor_type']
		ded_bd = request.POST['ded_brachdevision']
		prsn_res = request.POST['person_res']
		ignr = request.POST['ignore_it']
		st_itm = request.POST['tds_stock_items']
		
		ctds=Tds_Details(tan_regno=t_reg,
                        tan = tax_clct,
                        deductor_type = ded_type,
                        deductor_branch = ded_bd,
                        person_details = prsn_res,
                        ignore_it = ignr,
                        active_tds = st_itm,
						company = id)          
		ctds.save()
		print("added")
		return redirect('/')
	return render(request,'tds.html')

def person_tds(request,pk):
	id=Companies.objects.get(id=pk)
	if request.method=='POST':
		name = request.POST['name']
		sd = request.POST['son_daughter']
		des = request.POST['designation']
		pan = request.POST['pan']
		ftno = request.POST['flat_no']
		pnm = request.POST['premise_name']
		str = request.POST['street']
		are = request.POST['area']
		city = request.POST['city']
		st = request.POST['state']
		pcd = request.POST['pincode']
		m_no = request.POST['mobile_no']
		std = request.POST['std_code']
		tph = request.POST['telephone']
		emal = request.POST['email']
	    
		prs=tds_person(name=name,
                        son_daughter = sd,
                        designation = des,
                        pan = pan,
                        flat_no = ftno,
                        building = pnm,
                        street = str,
                        area = are,
                        town = city,
                        state = st,
                        pincode = pcd,
                        mobile = m_no,
                        std = std,
                        telephone = tph,
                        email = emal,
						company = id)          
		prs.save()
		print("added")
		return redirect('/')
	return render(request,'tds_person.html')

def create_voucher(request,pk):
	if request.method=='POST':
		cmp=Companies.objects.get(id=pk)
     
		nm=request.POST['vname']
		als=request.POST['alias']
		vtp=request.POST['vouch_type']
		abbr=request.POST['Abbreviation']
		actp=request.POST['activate_Vtype']
		mvno=request.POST['method_Vno']
		prnt=request.POST['prevent']
		acn=request.POST['advance_con']
		use=request.POST['use_EDV']
		zero=request.POST['zero_val']
		mvd=request.POST['mVoptional_defualt']
		anar=request.POST['allow_nar']
		prvdl=request.POST['provide_L']
		jrnl=request.POST['manu_jrnl']
		track=request.POST['track_purchase']
		enbl=request.POST['enable_acc']
		prntva=request.POST['prnt_VA_save']
		prntfml=request.POST['prnt_frml']
		juri=request.POST['jurisdiction']
		tprint=request.POST['title_print']
		setaltr=request.POST['set_alter']
		posinv=request.POST['pos_invoice']
		msg1=request.POST['msg_1']
		msg2=request.POST['msg_2']
		dbank=request.POST['default_bank']
		nc=request.POST['name_class']

		vhr=Voucher(voucher_name=nm,
                    alias = als,
                    voucher_type = vtp,
                    abbreviation = abbr,
                    voucherActivate = actp,
                    voucherNumber = mvno,
                    preventDuplicate = prnt,
                    advance_con = acn,
                    voucherEffective = use,
                    transaction = zero,
                    make_optional = mvd,
                    voucherNarration = anar,
                    provideNarration = prvdl,
                    manu_jrnl = jrnl,
                    track_purchase = track,
                    enable_acc = enbl,
                    prnt_VA_save = prntva,
                    prnt_frml = prntfml,
                    jurisdiction = juri,
                    title_print = tprint,
                    set_alter = setaltr,
                    pos_invoice = posinv,
                    msg_1 = msg1,
                    msg_2 = msg2,
                    default_bank = dbank,
                    name_class = nc,
                    company=cmp)          
		vhr.save()
		print("Added")
		return redirect('/')



def create_gst(request,pk):
	id=Companies.objects.get(id=pk)
	if request.method=='POST':
		st = request.POST['state']
		rt = request.POST['registration_type']
		at = request.POST['assessee_territory']
		gsta = request.POST['gst_applicable']
		gstuin = request.POST['gstin_uin']
		prd = request.POST['periodicity']

	# .................regular.................

		kfca = request.POST['kerala_fca']
		af = request.POST['applicable_from']
		gstrd = request.POST['gst_rate_details']
		tla = request.POST['tl_advanceR']
		tlr = request.POST['tl_reverseC']
		gstc = request.POST['gst_classification'] 
		lb = request.POST['lut_bond']

    # ................composition................  
	  
		tr = request.POST['tax_rate']
		tc = request.POST['tax_calculation']
		tp = request.POST['tax_purchase']

	# ............e-Way bill applicable...........

		ea = request.POST['e_waybillA']
		aaf = request.POST['applicable_f']
		tli = request.POST['thresholdlimit_include']
		tl = request.POST['threshold_limit']
		intr = request.POST['intrastate']
		itl = request.POST['ithreshold_limit']
		pnw = request.POST['print_eway']

	# .............e-Invoice applicable..............

		einva = request.POST['e_invoiceA']
		appf = request.POST['app_f']
		bfp = request.POST['billfrom_place']
		peir = request.POST['period_einvoiceR']
		sewdei = request.POST['send_eW_details_einvoice']
        
		gstd=GST(state=st,
						reg_type=rt,
						assessee=at,
						gst_applicable=gsta,
						gstin=gstuin,
						periodicity=prd,
					# ........regular.......
						flood_cess=kfca,
						applicable_from=af,
						gst_rate_details=gstrd,
						advance_receipts=tla,
						reverse_charge=tlr,
						gst_classification=gstc,
						bond_details=lb,	
					# ........composition.......
						tax_rate=tr,		
						tax_calc=tc,		
						tax_purchase=tp,
					# ........e-Way bill applicable.......
						eway_bill=ea,
						applicable_form=aaf,
						threshold_includes=tli,
						threshold_limit=tl,
						intrastate=intr,
						threshold_limit2=itl,
						print_eway=pnw,
					# ........e-Invoice applicable.......
						e_invoice=einva,
						app_from=appf,
						billfrom_place=bfp,
						dperiod=peir,
						send_ewaybill=sewdei,
						company=id)
		gstd.save()
		print("Added")
		return redirect('/')
	return render(request,'gst.html')

def create_gsttax(request,pk):
	id=Companies.objects.get(id=pk)
	if request.method=='POST':
		txb=request.POST['taxability']
		af=request.POST['appicable_from']
		it=request.POST['integrated_tax']
		ces=request.POST['cess']
		fc=request.POST['flood_cess']
		
		cost=gst_taxability(taxability=txb,
                        applicable_dt = af,
                        integrated_tax = it,      
                        cess = ces,      
                        flood_cess = fc,
						company = id)          
		cost.save()
		print("Added")
		return redirect('/')
	return render(request,'gst_tax.html')

def create_lutbond(request,pk):
	if request.method=='POST':
		lbno=request.POST['lut_bondNo']
		afrom=request.POST['application_from']
		ato=request.POST['application_to']
		lb=gst_lutbond(lutbond=lbno,
                        validity_from = afrom,
                        validity_to = ato)      
		lb.save() 
		print("Added")
		return redirect('lut_bond')
	return render(request,'lut_bond')

def create_ledger(request,pk):
    if request.method=='POST':
        cmp=Companies.objects.get(id=pk)
        nm=request.POST.get('name')
        als=request.POST.get('alias')
        under=request.POST.get('under')
        mname=request.POST.get('mailingname')
        adr=request.POST.get('address')
        st=request.POST.get('state')
        cntry=request.POST.get('country')
        pin=request.POST.get('pincode')
        pno=request.POST.get('pan_no')
        bdetls=request.POST.get('bank_details')
        rtype=request.POST.get('registration_type')
        gst_uin=request.POST.get('gst_uin')
        opnbn=request.POST.get('opening_blnc')

        spdl=request.POST.get('set_odl')
        achnm=request.POST.get('ac_holder_nm')
        acno=request.POST.get('acc_no')
        ifsc=request.POST.get('ifsc_code')
        scode=request.POST.get('swift_code')
        bn=request.POST.get('bank_name')
        brnch=request.POST.get('branch')
        sacbk=request.POST.get('SA_cheque_bk')
        ecp=request.POST.get('Echeque_p')
        sacpc=request.POST.get('SA_chequeP_con')

        typofled=request.POST.get('type_of_ledger')
        rometh=request.POST.get('rounding_method')
        rolmt=request.POST.get('rounding_limit')

        typdutytax=request.POST.get('type_duty_tax')
        taxtyp=request.POST.get('tax_type')
        valtype=request.POST.get('valuation_type')
        rateperu=request.POST.get('rate_per_unit')
        percalc=request.POST.get('percentage_of_calcution')
        rondmethod=request.POST.get('rond_method')
        roimlit=request.POST.get('rond_limit')

        gstapplicbl=request.POST.get('gst_applicable')
        sagatdet=request.POST.get('setalter_gstdetails')
        typsupply=request.POST.get('type_of_supply')
        asseval=request.POST.get('assessable_value')
        appropto=request.POST.get('appropriate_to')
        methcalcu=request.POST.get('method_of_calculation')

        balbillbybill=request.POST.get('balance_billbybill')
        credperiod=request.POST.get('credit_period')
        creditdaysvouch=request.POST.get('creditdays_voucher')
        
        ldr=tally_ledger(name=nm,alias=als,under=under,mname=mname,address=adr,state=st,country=cntry,
						pincode=pin,pan_no=pno,bank_details=bdetls,registration_type=rtype,gst_uin=gst_uin,
						opening_blnc=opnbn,set_odl=spdl,ac_holder_nm=achnm,acc_no=acno,ifsc_code=ifsc,swift_code=scode,
						bank_name=bn,branch=brnch,SA_cheque_bk=sacbk,Echeque_p=ecp,SA_chequeP_con=sacpc,
						type_of_ledger=typofled,rounding_method=rometh,rounding_limit=rolmt,type_duty_tax=typdutytax,tax_type=taxtyp,
						valuation_type=valtype,rate_per_unit=rateperu,percentage_of_calcution=percalc,rond_method=rondmethod,rond_limit=roimlit,
						gst_applicable=gstapplicbl,setalter_gstdetails=sagatdet,type_of_supply=typsupply,assessable_value=asseval,
						appropriate_to=appropto,method_of_calculation=methcalcu,balance_billbybill=balbillbybill,credit_period=credperiod,
						creditdays_voucher=creditdaysvouch,company=cmp)
		
        ldr.save()
        return redirect('/')
    return render(request,'ledgers.html')

def create_ledgerdimension(request,pk):
	if request.method == 'POST':
		cw= request.POST.get('cheque_width')
		ch= request.POST.get('cheque_height')
		sle= request.POST.get('startL_leftEdge')
		slte= request.POST.get('startL_topEdge')
		dlle= request.POST.get('distancel_leftEdge')
		dlte= request.POST.get('distancel_topEdge')
		ds= request.POST.get('date_style')
		dts= request.POST.get('date_seperator')
		sw= request.POST.get('separator_width')
		cd= request.POST.get('character_distance')
		pdle= request.POST.get('Pdistancel_leftEdge')
		pdlte= request.POST.get('Pdistancel_topEdge')
		aw= request.POST.get('area_width')
		sldte= request.POST.get('secondL_DTE')
		sflh= request.POST.get('secondfirstL_height')
		fldte= request.POST.get('firstL_dTE')
		slfle= request.POST.get('sl_fisrtl_LE')
		slsle= request.POST.get('sl_secondl_LE')
		awa= request.POST.get('amount_widtharea')
		cfnmp= request.POST.get('currencyFNM_print')
		dfte= request.POST.get('df_TE')
		sle= request.POST.get('startL_LE')
		amwa= request.POST.get('amt_widtharea')
		csp= request.POST.get('currencyS_print')
		cn= request.POST.get('company_name')
		pcn= request.POST.get('print_CN')
		sfs= request.POST.get('salutation_Fsign')
		sss= request.POST.get('salutation_Ssign')
		tes= request.POST.get('top_Edistance')
		slfl= request.POST.get('startLF_leftE')
		wsa= request.POST.get('width_sign_area')
		hsa= request.POST.get('height_sign_area')

		cld= ledger_cheque_demension(cheque_width=cw,cheque_height=ch,startL_leftEdge=sle,startL_topEdge=slte,distancel_leftEdge=dlle,
									distancel_topEdge=dlte,date_style=ds,date_seperator=dts,separator_width=sw,character_distance=cd,
									Pdistancel_leftEdge=pdle,Pdistancel_topEdge=pdlte,area_width=aw,secondL_DTE=sldte,secondfirstL_height=sflh,
									firstL_dTE=fldte,sl_fisrtl_LE=slfle,sl_secondl_LE=slsle,amount_widtharea=awa,currencyFNM_print=cfnmp,
									df_TE=dfte,startL_LE=sle,amt_widtharea=amwa,currencyS_print=csp,company_name=cn,print_CN=pcn,
									salutation_Fsign=sfs,salutation_Ssign=sss,top_Edistance=tes,startLF_leftE=slfl,width_sign_area=wsa,
									height_sign_area=hsa,company=cmp)

		cld.save()
		return redirect('/')
	return render(request,'ledger_chequed.html')

def company_create(request):
	if request.method=="POST":
		name=request.POST['companyname']
		mname=request.POST['mailing_name']
		addr=request.POST['address']
		st=request.POST['state']
		cntry=request.POST['country']
		pncd=request.POST['pincode']
		tlphn=request.POST['telephone']
		mbl=request.POST['mobile']
		fax=request.POST['fax']
		email=request.POST['email']
		wbsit=request.POST['website']
		fin_begin=request.POST['fyear']
		bk_begin=request.POST['byear']
		crny_symbol=request.POST['currency']
		frml_name=request.POST['formal']

		ccmp=Companies.objects.filter(name=name)
		out=datetime.strptime (fin_begin,'%Y-%m-%d')+timedelta (days=364) 
		a=out.date()
		

		if ccmp:
			messages.info(request,'Company name already exists!!')
			return redirect('create_cmpny')
		else:
			cmp=Companies(name=name,mailing_name=mname,address=addr,state=st,country=cntry,
                pincode=pncd,telephone=tlphn,mobile=mbl,fax=fax,email=email,website=wbsit,fin_begin=fin_begin,
                books_begin=bk_begin,currency_symbol=crny_symbol,formal_name=frml_name,fin_end=a)
			cmp.save()
			messages.info(request,'Company created successfully(Enable the features as per your business needs)')
			return render(request,'features.html',{'cmp':cmp})

def company_feature(request,cf):
	id=Companies.objects.get(id=cf)
	if request.method=="POST":
		ma=request.POST['maintain_account']
		be=request.POST['billwise_entry']
		cc=request.POST['cost_centre']
		ic=request.POST['interest_calculation']
		mi=request.POST['maintain_inventry']
		ai=request.POST['account_inventry']
		mpl=request.POST['multiple_pricelevel']
		eb=request.POST['enable_batches']
		edt=request.POST['expiry_date']
		jop=request.POST['job_order_procress']
		ct=request.POST['cost_tracking']
		jc=request.POST['job_costing']
		dc=request.POST['discount_column']
		sa=request.POST['seperte_actual']
		gst=request.POST['gst']
		tds=request.POST['tds']
		tcs=request.POST['tcs']
		vat=request.POST['vat']
		excise=request.POST['excise']
		st=request.POST['service_tax']
		prl=request.POST['payroll']
		maddr=request.POST['multiple_address']
		mark_mod=request.POST['mark_modified']

		cmp_fet=Features(maintain_accounts=ma,bill_wise_entry=be,cost_centres=cc,interest_calc=ic,maintain_inventory=mi,
		integrate_accounts=ai,multiple_price_level=mpl,batches=eb,expirydate_batches=edt,joborder_processing=jop,cost_tracking=ct,job_costing=jc,discount_invoices=dc,
		Billed_Quantity=sa,gst=gst,tds=tds,tcs=tcs,vat=vat,excise=excise,servicetax=st,payroll=prl,multiple_addrss=maddr,
		vouchers=mark_mod,company=id)

		cmp_fet.save()
		return redirect('/')
	return render(request,'features.html',{'cmp':id})

def create_bankdetails(request,p):
	if request.method=='POST':
		transaction_type=request.POST['transaction_type']
		acp=request.POST['ac_payee']
		acc_no=request.POST['acc_no']
		ifsc_code=request.POST['ifsc_code']
		bank_name=request.POST['bank_name']
		lbd=ledger_bankdetails(transaction_type=transaction_type,
                        cross_using = acp,
                        acc_no = acc_no,      
                        ifsc_code = ifsc_code,      
                        bank_name =bank_name)      
		lbd.save() 
		print("Added")
		return redirect('bank_details')
	return render(request,'bank_details.html')


def bankname(request):
	if request.method=='POST':
		bn = request.POST['bank_name']
		bnn=bank_name(bankname = bn)
		bnn.save()
		return redirect('bankname')
	return render(request,'bankname.html')


def create_chequebk(request):
	if request.method=='POST':
		fn=request.POST['from_number']
		tn=request.POST['to_number']
		nc=request.POST['number_cheques']
		nmc=request.POST['name_chequebk']
		lcb=ledger_chequebook(from_number=fn,
                        to_number = tn,
                        no_of_cheques = nc,
                        cheque_bookname = nmc)      
		lcb.save() 
		print("Added")
		return redirect('cheque')
	return render(request,'cheque.html')

def create_ledger_gst(request,pk):
	if request.method=='POST':
		cmp=Companies.objects.get(id=pk)
		ntrot=request.POST['nature_of_transaction']
		txbl=request.POST['taxable']
		txblty=request.POST['taxability']
		aplifm=request.POST['appicable_from']
		inttx=request.POST['integrated_tax']
		ces=request.POST['cess']
		lgst=ledger_gstvalues(nature_of_transaction=ntrot,
                        taxable = txbl,
                        taxability = txblty,
                        appicable_from = aplifm,
                        integrated_tax = inttx,
                        cess = ces,company=cmp)    
		lgst.save()  
		print("Added")
		return redirect('ledger_gst')
	return render(request,'ledger_gst.html')

def create_voucher_advance(request,pk):
	if request.method=='POST':
		cmp=Companies.objects.get(id=pk)
		stn=request.POST['starting_no']
		npw=request.POST['numerical_partwidth']
		pz=request.POST['prefill_zero']
		rsad=request.POST['restart_applicable_dt']
		rsrtsno=request.POST['restart_startingno']
		repert=request.POST['restart_particular']
		pread=request.POST['prefix_applicable_dt']
		preper=request.POST['prefix_particular']
		sfxapd=request.POST['suffix_applicable_dt']
		sfxper=request.POST['suffix_particular']

		cva=voucher_advanceconf(starting_no=stn,
                        numerical_partwidth = npw,
                        prefill_zero = pz,
                        restart_applicable_dt = rsad,
                        restart_startingno = rsrtsno,
                        restart_particular = repert,
                        prefix_applicable_dt = pread,
                        prefix_particular = preper,
                        suffix_applicable_dt = sfxapd,
                        suffix_particular = sfxper,company=cmp)    
		cva.save()  
		print("Added")
		return redirect('/')
	return render(request,'vouch_advance.html')


def create_ledger_taxgst(request,pk):
	if request.method=='POST':
		cmp=Companies.objects.get(id=pk)
		regtp=request.POST['registration_type']
		assester=request.POST['assessee_teritory']
		comop=request.POST['commerce_operator']
		partde=request.POST['party_deemed']
		partytyp=request.POST['party_type']
		gstinuin=request.POST['gstin_uin']
		transp=request.POST['transporter']
		transpid=request.POST['transporter_id']

		lgt=ledger_taxreggst(registration_type=regtp,
                        assessee_teritory = assester,
                        commerce_operator = comop,
                        party_deemed = partde,
                        party_type = partytyp,
                        gstin_uin = gstinuin,
                        transporter = transp,
                        transporter_id = transpid,company=cmp)    
		lgt.save()  
		print("Added")
		return redirect('ledger_taxgst')
	return render(request,'ledger_taxgst.html')


#......................Ajmy........................


def index(request):
    return render(request, 'home.html')

def group(request):
    return render(request, 'groups.html')

def branch(request):
    return render(request, 'branch.html')

def ledger(request):
    return render(request, 'ledger.html')

def primary(request):
    return render(request, 'primarycost.html')

def costcat(request):
    return render(request, 'costcat.html')

def voucher(request):
    return render(request, 'voucher.html')

def vouchpage(request):
    return render(request, 'vouchpage.html')

def groupsummarypage(request):
    gps=CreateStockGrp.objects.all()
    con={
        'gps':gps,
        } 
    return render(request,'groupsummarypage.html',con)

def catgroupsummary(request):
    cat=CreateStockCateg.objects.all()
    con={
        'cat':cat,
        } 
    return render(request,'catgroupsummary.html',con)

def creategroups(request):
    gps=StockGroup.objects.all()
    con={
        'gps':gps,
        } 
    return render(request, 'creategroup.html',con)   

def createcategory(request):
    cat=Stockcategory.objects.all()
    con={
        'cat':cat,
        } 
    return render(request, 'createcategory.html',con) 

def savestockgroup(request):
    if request.method=='POST':
        gpname=request.POST['name']
        s=StockGroup(grp_name=gpname)
        s.save()
        abr=request.POST['alias']
        grp=request.POST.get('u')
        gp=StockGroup.objects.get(grp_name=grp)
        q=request.POST.get('qty')
        sg=CreateStockGrp(name=gpname,alias=abr,quantities=q,under=grp,group=gp)
        sg.save()
        return redirect('groupsummarypage')

def savestockcategory(request):
    if request.method=='POST':
        catname=request.POST['name']
        s=Stockcategory(cat_name=catname)
        s.save()
        abr=request.POST['alias']
        cat=request.POST.get('u')
        c=Stockcategory.objects.get(cat_name=cat)
        q=request.POST.get('qty')
        sc=CreateStockCateg(name=catname,alias=abr,quantities=q,under=cat,category=c)
        sc.save()
        return redirect('catgroupsummary')

def primarygrpsummary(request,sk):
    cmp=company.objects.get(id='1')
    gps=CreateStockGrp.objects.filter(group_id=sk)
    gt=0
    for g in gps:
        gg=StockGroup.objects.get(grp_name=g.name)
        gpsi= CreateStockGrp.objects.filter(group_id=gg.id)
        l=[]
        i=0
        h=0
        for gi in gpsi:
           gg=StockGroup.objects.get(grp_name=gi.name)
           si=stock_item.objects.filter(group_id=gg.id)
           ttpq=0
           ttsq=0
           r=0
           a=0
           y=0
      
           for s in si:
               w=s.rateper 
               oqty=s.quantity
               val=s.value
               tpq=voucherlist.objects.filter(item_id=s.id,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
               tpq=tpq+oqty
               ttpq=tpq+ttpq
               tsq=voucherlist.objects.filter(item_id=s.id,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
               ttsq=tsq+ttsq
               ttq=tpq-tsq
               s.qy=ttq
               s.value=ttq * w
               a=a+s.value
               y=y+w
           gi.q=ttpq-ttsq 
           gi.i=a
           h=h+gi.i
           gi.y=y
           i=i+1 
           gi.h=h   
           g.h=h
        gt=gt+g.h   
            



    con={
        'gpsi':gpsi,
        'gps':gps,
        'sk':sk,
        'gt':gt,
        'cmp':cmp
        } 
    return render(request, 'primarygrpsummary.html',con)  

def primarycatsummary(request,sk):
    cmp=company.objects.get(id='1')
    cat=CreateStockCateg.objects.filter(category_id=sk)
    gt=0
    for c in cat:
        cc=Stockcategory.objects.get(cat_name=c.name)
        cgsi= CreateStockCateg.objects.filter(category_id=cc.id)
        l=[]
        i=0
        h=0
        for ci in cgsi:
           cc=Stockcategory.objects.get(cat_name=ci.name)
           si=stock_item.objects.filter(category_id=cc.id)
           ttpq=0
           ttsq=0
           r=0
           a=0
           y=0
      
           for s in si:
               w=s.rateper 
               oqty=s.quantity
               val=s.value
               tpq=voucherlist.objects.filter(item_id=s.id,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
               tpq=tpq+oqty
               ttpq=tpq+ttpq
               tsq=voucherlist.objects.filter(item_id=s.id,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
               ttsq=tsq+ttsq
               ttq=tpq-tsq
               s.qy=ttq
               s.value=ttq * w
               a=a+s.value
               y=y+w
           ci.q=ttpq-ttsq 
           ci.i=a
           h=h+ci.i
           ci.y=y
           i=i+1 
           ci.h=h   
           c.h=h
        gt=gt+c.h   
            



    con={
        'cgsi':cgsi,
        'cat':cat,
        'sk':sk,
        'gt':gt,
        'cmp':cmp
        } 
    return render(request, 'primarycatsummary.html',con)

def secondarygrpsummary(request,sk):
    cmp=company.objects.get(id='1')
    gps=CreateStockGrp.objects.get(id=sk)
    gg=StockGroup.objects.get(grp_name=gps.name)
    gps= CreateStockGrp.objects.filter(group_id=gg.id)
    l=[]
    i=0
    h=0
    for g in gps:
      gg=StockGroup.objects.get(grp_name=g.name)
      si=stock_item.objects.filter(group_id=gg.id)
      ttpq=0
      ttsq=0
      r=0
      a=0
      y=0
      
      for s in si:
            w=s.rateper 
            oqty=s.quantity
            val=s.value
            tpq=voucherlist.objects.filter(item_id=s.id,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            tpq=tpq+oqty
            ttpq=tpq+ttpq
            tsq=voucherlist.objects.filter(item_id=s.id,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            ttsq=tsq+ttsq
            ttq=tpq-tsq
            s.qy=ttq
            s.value=ttq * w
            a=a+s.value
            y=y+w
      g.q=ttpq-ttsq 
      g.i=a
      h=h+g.i
      g.y=y
      i=i+1 
    con={
        'gps':gps,'a':a,'y':y,'gps':gps,'l':l,'h':h,'cmp':cmp
        } 
    return render(request, 'secondarygrpsummary.html',con) 

def secondarycatsummary(request,sk):
    cat=CreateStockCateg.objects.get(id=sk)
    cmp=company.objects.get(id='1')
    cc=Stockcategory.objects.get(cat_name=cat.name)
    cat= CreateStockCateg.objects.filter(category_id=cc.id)
    l=[]
    i=0
    h=0
    for c in cat:
      cc=Stockcategory.objects.get(cat_name=c.name)
      si=stock_item.objects.filter(category_id=cc.id)
      ttpq=0
      ttsq=0
      r=0
      a=0
      y=0
      
      for s in si:
            w=s.rateper 
            oqty=s.quantity
            val=s.value
            tpq=voucherlist.objects.filter(item_id=s.id,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            tpq=tpq+oqty
            ttpq=tpq+ttpq
            tsq=voucherlist.objects.filter(item_id=s.id,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            ttsq=tsq+ttsq
            ttq=tpq-tsq
            s.qy=ttq
            s.value=ttq * w
            a=a+s.value
            y=y+w
      c.q=ttpq-ttsq 
      c.i=a
      h=h+c.i
      c.y=y
      i=i+1 
    con={
        'cat':cat,'a':a,'y':y,'l':l,'h':h,'cmp':cmp
        } 
    return render(request, 'secondarycatsummary.html',con) 


def productsummary(request,sk):
    gps=CreateStockGrp.objects.get(id=sk)
    cmp=company.objects.get(id='1')
    gg=StockGroup.objects.get(grp_name=gps.name)
    si=stock_item.objects.filter(group_id=gg.id)
    ttpq=0
    ttsq=0
    r=0
    a=0
    y=0
    for s in si:
        w=s.rateper
        qty=s.quantity
        val=s.value
        tpq=voucherlist.objects.filter(item_id=s.id,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        tpq=tpq+qty
        ttpq=tpq+ttpq
        tsq=voucherlist.objects.filter(item_id=s.id,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        ttsq=tsq+ttsq
        ttq=tpq-tsq
        s.qy=ttq
        s.value=ttq * w
        a=a+s.value
        y=y+w
    
    
    q=ttpq-ttsq   
    con={
        'si':si,'ttpq':ttpq,'q':q,'ttpq':ttq,'w':w,'a':a,'y':y,'cmp':cmp
        } 
    return render(request, 'productsummary.html',con)


def prcatsummary(request,sk):
    cmp=company.objects.get(id='1')
    cat=CreateStockCateg.objects.get(id=sk)
    cc=Stockcategory.objects.get(cat_name=cat.name)
    si=stock_item.objects.filter(category_id=cc.id)
    ttpq=0
    ttsq=0
    r=0
    a=0
    y=0
    for s in si:
        w=s.rateper
        qty=s.quantity
        val=s.value
        tpq=voucherlist.objects.filter(item_id=s.id,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        tpq=tpq+qty
        ttpq=tpq+ttpq
        tsq=voucherlist.objects.filter(item_id=s.id,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        ttsq=tsq+ttsq
        ttq=tpq-tsq
        s.qy=ttq
        s.value=ttq * w
        a=a+s.value
        y=y+w
    
    
    q=ttpq-ttsq   
    con={
        'si':si,'ttpq':ttpq,'q':q,'ttpq':ttq,'w':w,'a':a,'y':y,'cmp':cmp
        } 
    return render(request, 'productcatsummary.html',con) 


def prdctmonthlysummary(request,sk):
    cmp=company.objects.get(id='1')
    si=stock_item.objects.get(id=sk)
    rate=si.rateper
    qty=si.quantity
    val=si.value
    tpq=voucherlist.objects.filter(item_id=si.id,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    tpqo=tpq+qty
    tpv=voucherlist.objects.filter(item_id=si.id,vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    
    tsq=voucherlist.objects.filter(item_id=si.id,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    tsv=voucherlist.objects.filter(item_id=si.id,vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    ttq=tpqo-tsq
    rate=si.rateper
    qty=si.quantity
    val=si.value
    
    a=voucherlist.objects.filter(item_id=si.id,date__gte='2022-04-01',date__lte='2022-04-30',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    b=voucherlist.objects.filter(item_id=si.id,date__gte='2022-04-01',date__lte='2022-04-30',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    c=voucherlist.objects.filter(item_id=si.id,date__gte='2022-04-01',date__lte='2022-04-30',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    d=voucherlist.objects.filter(item_id=si.id,date__gte='2022-04-01',date__lte='2022-04-30',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    ia=a
    ib=b
    oc=c
    od=d
    a=a+qty
    b=b+val
    aa=a-c
    

    e=voucherlist.objects.filter(item_id=sk,date__gte='2022-05-01',date__lte='2022-05-31',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    f=voucherlist.objects.filter(item_id=sk,date__gte='2022-05-01',date__lte='2022-05-31',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    g=voucherlist.objects.filter(item_id=sk,date__gte='2022-05-01',date__lte='2022-05-31',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    h=voucherlist.objects.filter(item_id=sk,date__gte='2022-05-01',date__lte='2022-05-31',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    ie=e
    iv=f
    og=g
    oh=h
    cc=e-g
    cb5=aa+cc
    

    i=voucherlist.objects.filter(item_id=sk,date__gte='2022-06-01',date__lte='2022-06-30',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    j=voucherlist.objects.filter(item_id=sk,date__gte='2022-06-01',date__lte='2022-06-30',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    k=voucherlist.objects.filter(item_id=sk,date__gte='2022-06-01',date__lte='2022-06-30',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    l=voucherlist.objects.filter(item_id=sk,date__gte='2022-06-01',date__lte='2022-06-30',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    iiq=i
    ij=j
    okq=k
    ol=l
    ee=i-k
    cb6=cb5+ee
     
    
    m=voucherlist.objects.filter(item_id=sk,date__gte='2022-07-01',date__lte='2022-07-31',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    n=voucherlist.objects.filter(item_id=sk,date__gte='2022-07-01',date__lte='2022-07-31',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    o=voucherlist.objects.filter(item_id=sk,date__gte='2022-07-01',date__lte='2022-07-31',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    p=voucherlist.objects.filter(item_id=sk,date__gte='2022-07-01',date__lte='2022-07-31',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    im=m
    inv=n
    ooq=o
    op=p
    gg=m-o
    cb7=cb6+gg

    q=voucherlist.objects.filter(item_id=sk,date__gte='2022-08-01',date__lte='2022-08-31',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    r=voucherlist.objects.filter(item_id=sk,date__gte='2022-08-01',date__lte='2022-08-31',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    s=voucherlist.objects.filter(item_id=sk,date__gte='2022-08-01',date__lte='2022-08-31',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    t=voucherlist.objects.filter(item_id=sk,date__gte='2022-08-01',date__lte='2022-08-31',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    iq=q
    ir=r
    os=s
    ot=t
    ii=q-s
    cb8=cb7+ii

    u=voucherlist.objects.filter(item_id=sk,date__gte='2022-09-01',date__lte='2022-09-30',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    v=voucherlist.objects.filter(item_id=sk,date__gte='2022-09-01',date__lte='2022-09-30',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    w=voucherlist.objects.filter(item_id=sk,date__gte='2022-09-01',date__lte='2022-09-30',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    x=voucherlist.objects.filter(item_id=sk,date__gte='2022-09-01',date__lte='2022-09-30',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    iu=u
    ivv=v
    ow=w
    ox=x
    kk=u-w
    cb9=cb8+kk
    
    y=voucherlist.objects.filter(item_id=sk,date__gte='2022-10-01',date__lte='2022-10-31',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    z=voucherlist.objects.filter(item_id=sk,date__gte='2022-10-01',date__lte='2022-10-31',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    a1=voucherlist.objects.filter(item_id=sk,date__gte='2022-10-01',date__lte='2022-10-31',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    b1=voucherlist.objects.filter(item_id=sk,date__gte='2022-10-01',date__lte='2022-10-31',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    iy=y
    iz=z
    oa1=a1
    ob1=b1 
    mm=y-a1
    cb10=cb9+mm

    c1=voucherlist.objects.filter(item_id=sk,date__gte='2022-11-01',date__lte='2022-11-30',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    d1=voucherlist.objects.filter(item_id=sk,date__gte='2022-11-01',date__lte='2022-11-30',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    e1=voucherlist.objects.filter(item_id=sk,date__gte='2022-11-01',date__lte='2022-11-30',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    f1=voucherlist.objects.filter(item_id=sk,date__gte='2022-11-01',date__lte='2022-11-30',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    ic1=c1
    id1=d1
    oe1=e1
    of1=f1
    oo=c1-e1
    cb11=cb10+oo

    g1=voucherlist.objects.filter(item_id=sk,date__gte='2022-12-01',date__lte='2022-12-31',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    h1=voucherlist.objects.filter(item_id=sk,date__gte='2022-12-01',date__lte='2022-12-31',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    i1=voucherlist.objects.filter(item_id=sk,date__gte='2022-12-01',date__lte='2022-12-31',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    j1=voucherlist.objects.filter(item_id=sk,date__gte='2022-12-01',date__lte='2022-12-31',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    ig1=g1
    ih1=h1
    oi1=i1
    oj1=j1
    qq=g1-i1
    cb12=cb11+qq

    k1=voucherlist.objects.filter(item_id=sk,date__gte='2022-01-01',date__lte='2022-01-31',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    l1=voucherlist.objects.filter(item_id=sk,date__gte='2022-01-01',date__lte='2022-01-31',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    m1=voucherlist.objects.filter(item_id=sk,date__gte='2022-01-01',date__lte='2022-01-31',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    n1=voucherlist.objects.filter(item_id=sk,date__gte='2022-01-01',date__lte='2022-01-31',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    ik1=k1
    il1=l1
    om1=m1
    on1=n1
    ss=k1-m1
    cb1=cb12+ss

    o1=voucherlist.objects.filter(item_id=sk,date__gte='2022-02-01',date__lte='2022-02-28',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    p1=voucherlist.objects.filter(item_id=sk,date__gte='2022-02-01',date__lte='2022-02-28',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    q1=voucherlist.objects.filter(item_id=sk,date__gte='2022-02-01',date__lte='2022-02-28',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    r1=voucherlist.objects.filter(item_id=sk,date__gte='2022-02-01',date__lte='2022-02-28',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    io1=o1
    ip1=p1
    oq1=q1
    or1=r1
    uu=o1-q1
    cb2=cb1+uu

    s1=voucherlist.objects.filter(item_id=sk,date__gte='2022-03-01',date__lte='2022-03-31',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    t1=voucherlist.objects.filter(item_id=sk,date__gte='2022-03-01',date__lte='2022-03-31',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    u1=voucherlist.objects.filter(item_id=sk,date__gte='2022-03-01',date__lte='2022-03-31',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    v1=voucherlist.objects.filter(item_id=sk,date__gte='2022-03-01',date__lte='2022-03-31',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']                            
    is1=s1
    it1=t1
    ou1=u1
    ov1=v1
    ww=s1-u1
    cb3=cb2+ww
    
    
    
    
    
    
    
    
    con={
        'si':si,'cmp':cmp,
        'a':a,'b':b,'c':c,'d':d,'e':e,'f':f,'g':g,'h':h,'i':i,'j':j,'k':k,'l':l,'m':m,'n':n,'o':o,'p':p,'q':q,'r':r,'s':s,'t':t,'u':u,'v':v,'w':w,'x':x,'y':y,'z':z ,'a1':a1,
        'b1':b1,'c1':c1,'d1':d1,'e1':e1,'f1':f1,'g1':g1,'h1':h1,'i1':i1,'j1':j1,'k1':k1,'l1':l1,'m1':m1,'n1':n1,'o1':o1,'p1':p1,'q1':q1,'r1':r1,'s1':s1,'t1':t1,'u1':u1,'v1':v1,
        
        'ia':ia,'ib':ib,'oc':oc,'od':od,'ie':ie,'iv':iv,'og':og,'oh':oh,'iiq':iiq,'ij':ij,'okq':okq,'ol':ol,'im':im,'inv':inv,'ooq':ooq,'op':op,'iq':iq,'ir':ir,'os':os,'ot':ot,'iu':iu,'ivv':ivv,'ow':ow,'ox':ox,'iy':iy,'iz':iz ,'oa1':oa1,
        'ob1':ob1,'ic1':ic1,'id1':id1,'oe1':oe1,'of1':of1,'ig1':ig1,'ih1':ih1,'oi1':oi1,'oj1':oj1,'ik1':ik1,'il1':il1,'om1':om1,'on1':on1,'io1':io1,'ip1':ip1,'oq1':oq1,'or1':or1,'is1':is1,'it1':it1,'ou1':ou1,'ov1':ov1,
        
        'aa':aa,'cc':cc,'ee':ee,'gg':gg,'ii':ii,'kk':kk,'mm':mm,'oo':oo,'qq':qq,'ss':ss,'uu':uu,'ww':ww,
        'tpq':tpq,'tsq':tsq,'tpv':tpv,'tsv':tsv,'ttq':ttq,'rate':rate
        ,'qty':qty,'val':val,'cb5':cb5,'cb6':cb6,'cb7':cb7,'cb8':cb8,'cb9':cb9,'cb10':cb10,'cb11':cb11,'cb12':cb12,'cb1':cb1,'cb2':cb2,'cb3':cb3,}
    return render(request, 'prdctmonthlysummary.html',con)


def productcatmonthlysummary(request,sk):
    si=stock_item.objects.get(id=sk)
    rate=si.rateper
    qty=si.quantity
    val=si.value
    tpq=voucherlist.objects.filter(item_id=si.id,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    tpq=tpq+qty
    tpv=voucherlist.objects.filter(item_id=si.id,vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    tpv=tpv+val
    tsq=voucherlist.objects.filter(item_id=si.id,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    tsv=voucherlist.objects.filter(item_id=si.id,vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    ttq=tpq-tsq
    rate=si.rateper
    qty=si.quantity
    val=si.value
    
    a=voucherlist.objects.filter(item_id=si.id,date__gte='2022-04-01',date__lte='2022-04-30',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    b=voucherlist.objects.filter(item_id=si.id,date__gte='2022-04-01',date__lte='2022-04-30',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    c=voucherlist.objects.filter(item_id=si.id,date__gte='2022-04-01',date__lte='2022-04-30',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    d=voucherlist.objects.filter(item_id=si.id,date__gte='2022-04-01',date__lte='2022-04-30',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    a=a+qty
    b=b+val
    aa=a-c
    

    e=voucherlist.objects.filter(item_id=sk,date__gte='2022-05-01',date__lte='2022-05-31',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    f=voucherlist.objects.filter(item_id=sk,date__gte='2022-05-01',date__lte='2022-05-31',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    g=voucherlist.objects.filter(item_id=sk,date__gte='2022-05-01',date__lte='2022-05-31',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    h=voucherlist.objects.filter(item_id=sk,date__gte='2022-05-01',date__lte='2022-05-31',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    cc=e-g
    

    i=voucherlist.objects.filter(item_id=sk,date__gte='2022-06-01',date__lte='2022-06-30',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    j=voucherlist.objects.filter(item_id=sk,date__gte='2022-06-01',date__lte='2022-06-30',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    k=voucherlist.objects.filter(item_id=sk,date__gte='2022-06-01',date__lte='2022-06-30',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    l=voucherlist.objects.filter(item_id=sk,date__gte='2022-06-01',date__lte='2022-06-30',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    ee=i-k
   
     
    
    m=voucherlist.objects.filter(item_id=sk,date__gte='2022-07-01',date__lte='2022-07-31',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    n=voucherlist.objects.filter(item_id=sk,date__gte='2022-07-01',date__lte='2022-07-31',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    o=voucherlist.objects.filter(item_id=sk,date__gte='2022-07-01',date__lte='2022-07-31',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    p=voucherlist.objects.filter(item_id=sk,date__gte='2022-07-01',date__lte='2022-07-31',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    gg=m-o
    

    q=voucherlist.objects.filter(item_id=sk,date__gte='2022-08-01',date__lte='2022-08-31',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    r=voucherlist.objects.filter(item_id=sk,date__gte='2022-08-01',date__lte='2022-08-31',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    s=voucherlist.objects.filter(item_id=sk,date__gte='2022-08-01',date__lte='2022-08-31',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    t=voucherlist.objects.filter(item_id=sk,date__gte='2022-08-01',date__lte='2022-08-31',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    ii=q-s
    
    u=voucherlist.objects.filter(item_id=sk,date__gte='2022-09-01',date__lte='2022-09-30',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    v=voucherlist.objects.filter(item_id=sk,date__gte='2022-09-01',date__lte='2022-09-30',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    w=voucherlist.objects.filter(item_id=sk,date__gte='2022-09-01',date__lte='2022-09-30',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    x=voucherlist.objects.filter(item_id=sk,date__gte='2022-09-01',date__lte='2022-09-30',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    kk=u-w
    
    y=voucherlist.objects.filter(item_id=sk,date__gte='2022-10-01',date__lte='2022-10-31',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    z=voucherlist.objects.filter(item_id=sk,date__gte='2022-10-01',date__lte='2022-10-31',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    a1=voucherlist.objects.filter(item_id=sk,date__gte='2022-10-01',date__lte='2022-10-31',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    b1=voucherlist.objects.filter(item_id=sk,date__gte='2022-10-01',date__lte='2022-10-31',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    mm=y-a1
    
    c1=voucherlist.objects.filter(item_id=sk,date__gte='2022-11-01',date__lte='2022-11-30',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    d1=voucherlist.objects.filter(item_id=sk,date__gte='2022-11-01',date__lte='2022-11-30',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    e1=voucherlist.objects.filter(item_id=sk,date__gte='2022-11-01',date__lte='2022-11-30',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    f1=voucherlist.objects.filter(item_id=sk,date__gte='2022-11-01',date__lte='2022-11-30',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    oo=c1-e1
    
    g1=voucherlist.objects.filter(item_id=sk,date__gte='2022-12-01',date__lte='2022-12-31',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    h1=voucherlist.objects.filter(item_id=sk,date__gte='2022-12-01',date__lte='2022-12-31',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    i1=voucherlist.objects.filter(item_id=sk,date__gte='2022-12-01',date__lte='2022-12-31',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    j1=voucherlist.objects.filter(item_id=sk,date__gte='2022-12-01',date__lte='2022-12-31',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    qq=g1-i1
    
    k1=voucherlist.objects.filter(item_id=sk,date__gte='2022-01-01',date__lte='2022-01-31',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    l1=voucherlist.objects.filter(item_id=sk,date__gte='2022-01-01',date__lte='2022-01-31',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    m1=voucherlist.objects.filter(item_id=sk,date__gte='2022-01-01',date__lte='2022-01-31',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    n1=voucherlist.objects.filter(item_id=sk,date__gte='2022-01-01',date__lte='2022-01-31',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    ss=k1-m1
    
    o1=voucherlist.objects.filter(item_id=sk,date__gte='2022-02-01',date__lte='2022-02-28',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    p1=voucherlist.objects.filter(item_id=sk,date__gte='2022-02-01',date__lte='2022-02-28',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    q1=voucherlist.objects.filter(item_id=sk,date__gte='2022-02-01',date__lte='2022-02-28',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    r1=voucherlist.objects.filter(item_id=sk,date__gte='2022-02-01',date__lte='2022-02-28',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
    uu=o1-q1
    
    s1=voucherlist.objects.filter(item_id=sk,date__gte='2022-03-01',date__lte='2022-03-31',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    t1=voucherlist.objects.filter(item_id=sk,date__gte='2022-03-01',date__lte='2022-03-31',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
    u1=voucherlist.objects.filter(item_id=sk,date__gte='2022-03-01',date__lte='2022-03-31',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
    v1=voucherlist.objects.filter(item_id=sk,date__gte='2022-03-01',date__lte='2022-03-31',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']                            
    ww=s1-u1
    
    
    
    
    
    
    
    
    
    con={
        'si':si,
        'a':a,'b':b,'c':c,'d':d,'e':e,'f':f,'g':g,'h':h,'i':i,'j':j,'k':k,'l':l,'m':m,'n':n,'o':o,'p':p,'q':q,'r':r,'s':s,'t':t,'u':u,'v':v,'w':w,'x':x,'y':y,'z':z ,'a1':a1,
        'b1':b1,'c1':c1,'d1':d1,'e1':e1,'f1':f1,'g1':g1,'h1':h1,'i1':i1,'j1':j1,'k1':k1,'l1':l1,'m1':m1,'n1':n1,'o1':o1,'p1':p1,'q1':q1,'r1':r1,'s1':s1,'t1':t1,'u1':u1,'v1':v1
        
        ,'aa':aa,'cc':cc,'ee':ee,'gg':gg,'ii':ii,'kk':kk,'mm':mm,'oo':oo,'qq':qq,'ss':ss,'uu':uu,'ww':ww,
        'tpq':tpq,'tsq':tsq,'tpv':tpv,'tsv':tsv,'ttq':ttq,'rate':rate
        ,'qty':qty,'val':val,}
    return render(request, 'prdctmonthlysummary.html',con)


def vouchsummary(request,sk,m,n):
    cmp=company.objects.get(id='1')
    si=stock_item.objects.get(id=sk)
    rate=si.rateper
    
    
    if m==4:
        qty=si.quantity
        val=si.value
        v=voucherlist.objects.filter(item_id=sk,date__gte='2022-04-01',date__lte='2022-04-30')
        a=voucherlist.objects.filter(item_id=sk,date__gte='2022-04-01',date__lte='2022-04-30',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte='2022-04-01',date__lte='2022-04-30',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte='2022-04-01',date__lte='2022-04-30',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte='2022-04-01',date__lte='2022-04-30',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        a=a+qty
        b=b+val
        e=a-c
        f=rate
        tq=e
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-04-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-04-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
            
    if m==5:
        qty=n
        val=qty*rate
        v=voucherlist.objects.filter(item_id=sk,date__gte='2022-05-01',date__lte='2022-05-31')
        a=voucherlist.objects.filter(item_id=sk,date__gte='2022-05-01',date__lte='2022-05-31',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte='2022-05-01',date__lte='2022-05-31',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte='2022-05-01',date__lte='2022-05-31',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte='2022-05-01',date__lte='2022-05-31',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        e=a-c
        f=rate
        a=a+n
        b=b+(n*f)
        tq=e+n
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-05-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-05-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
            
    if m==6:
        qty=n
        val=qty*rate
        v=voucherlist.objects.filter(item_id=sk,date__gte='2022-06-01',date__lte='2022-06-30')
        a=voucherlist.objects.filter(item_id=sk,date__gte='2022-06-01',date__lte='2022-06-30',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte='2022-06-01',date__lte='2022-06-30',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte='2022-06-01',date__lte='2022-06-30',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte='2022-06-01',date__lte='2022-06-30',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        a=a
        b=b
        e=a-c
        f=rate
        a=a+n
        b=b+(n*f)
        tq=e+n
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-06-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-06-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
            
    if m==7:
        qty=n
        val=qty*rate
        v=voucherlist.objects.filter(item_id=sk,date__gte='2022-07-01',date__lte='2022-07-31')
        a=voucherlist.objects.filter(item_id=sk,date__gte='2022-07-01',date__lte='2022-07-31',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte='2022-07-01',date__lte='2022-07-31',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte='2022-07-01',date__lte='2022-07-31',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte='2022-07-01',date__lte='2022-07-31',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        e=a-c
        f=rate
        a=a+n
        b=b+(n*f)
        tq=e+n
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-07-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-07-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
            
    if m==8:
        qty=n
        val=qty*rate
        v=voucherlist.objects.filter(item_id=sk,date__gte='2022-08-01',date__lte='2022-08-31')
        a=voucherlist.objects.filter(item_id=sk,date__gte='2022-08-01',date__lte='2022-08-31',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte='2022-08-01',date__lte='2022-08-31',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte='2022-08-01',date__lte='2022-08-31',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte='2022-08-01',date__lte='2022-08-31',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        e=a-c
        f=rate
        a=a+n
        b=b+(n*f)
        tq=e+n
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-08-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-08-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
            
    if m==9:
        qty=n
        val=qty*rate
        v=voucherlist.objects.filter(item_id=sk,date__gte='2022-09-01',date__lte='2022-09-30')
        a=voucherlist.objects.filter(item_id=sk,date__gte='2022-09-01',date__lte='2022-09-30',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte='2022-09-01',date__lte='2022-09-30',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte='2022-09-01',date__lte='2022-09-30',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte='2022-09-01',date__lte='2022-09-30',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        e=a-c
        f=rate
        a=a+n
        b=b+(n*f)
        tq=e+n
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-09-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-09-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
            
    if m==10:
        qty=n
        val=qty*rate
        v=voucherlist.objects.filter(item_id=sk,date__gte='2022-10-01',date__lte='2022-10-31')
        a=voucherlist.objects.filter(item_id=sk,date__gte='2022-10-01',date__lte='2022-10-31',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte='2022-10-01',date__lte='2022-10-31',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte='2022-10-01',date__lte='2022-10-31',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte='2022-10-01',date__lte='2022-10-31',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        e=a-c
        f=rate
        a=a+n
        b=b+(n*f)
        tq=e+n
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-10-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-10-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
            
    if m==11:
        qty=n
        val=qty*rate
        v=voucherlist.objects.filter(item_id=sk,date__gte='2022-11-01',date__lte='2022-11-30')
        a=voucherlist.objects.filter(item_id=sk,date__gte='2022-11-01',date__lte='2022-11-30',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte='2022-11-01',date__lte='2022-11-30',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte='2022-11-01',date__lte='2022-11-30',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte='2022-11-01',date__lte='2022-11-30',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        e=a-c
        f=rate
        a=a+n
        b=b+(n*f)
        tq=e+n
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-11-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-11-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
            
    if m==12:
        qty=n
        val=qty*rate
        v=voucherlist.objects.filter(item_id=sk,date__gte='2022-12-01',date__lte='2022-12-31')
        a=voucherlist.objects.filter(item_id=sk,date__gte='2022-12-01',date__lte='2022-12-31',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte='2022-12-01',date__lte='2022-12-31',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte='2022-12-01',date__lte='2022-12-31',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte='2022-12-01',date__lte='2022-12-31',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        e=a-c
        f=rate
        a=a+n
        b=b+(n*f)
        tq=e+n
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-12-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-12-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
            
    if m==1:
        qty=n
        val=qty*rate
        v=voucherlist.objects.filter(item_id=sk,date__gte='2022-01-01',date__lte='2022-01-31')
        a=voucherlist.objects.filter(item_id=sk,date__gte='2022-01-01',date__lte='2022-01-31',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte='2022-01-01',date__lte='2022-01-31',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte='2022-01-01',date__lte='2022-01-31',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte='2022-01-01',date__lte='2022-01-31',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        e=a-c
        f=rate
        a=a+n
        b=b+(n*f)
        tq=e+n
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-01-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-01-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
            
    if m==2:
        qty=n
        val=qty*rate
        v=voucherlist.objects.filter(item_id=sk,date__gte='2022-02-01',date__lte='2022-02-28')
        a=voucherlist.objects.filter(item_id=sk,date__gte='2022-02-01',date__lte='2022-02-28',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte='2022-02-01',date__lte='2022-02-28',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte='2022-02-01',date__lte='2022-02-28',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte='2022-02-01',date__lte='2022-02-28',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        e=a-c
        f=rate
        a=a+n
        b=b+(n*f)
        tq=e+n
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-02-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-02-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
            
    if m==3:
        qty=n
        val=qty*rate
        v=voucherlist.objects.filter(item_id=sk,date__gte='2022-03-01',date__lte='2022-03-31')
        a=voucherlist.objects.filter(item_id=sk,date__gte='2022-03-01',date__lte='2022-03-31',vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte='2022-03-01',date__lte='2022-03-31',vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte='2022-03-01',date__lte='2022-03-31',vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte='2022-03-01',date__lte='2022-03-31',vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        e=a-c
        f=rate
        a=a+n
        b=b+(n*f)
        tq=e+n
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-03-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-03-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
                                   
    
    con={
        'v':v,
        'si':si,
        'm':m,
        'a':a,
        'b':b,
        'c':c,
        'd':d,
        'e':e,
        'f':f,
        'qty':qty,
        'val':val,
        'fr':fr ,'tq':tq ,'n':n,
        'si':si,'cmp':cmp  
        }
    return render(request, 'vouchersummary.html',con)


def periodvouchsummary(request,sk,m,n):
    cmp=company.objects.get(id='1')
    si=stock_item.objects.get(id=sk)
    rate=si.rateper
    st=request.POST.get('start')
    et=request.POST.get('end')
    
    if m==4:
        qty=si.quantity
        val=si.value
        v=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et)
        a=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        a=a+qty
        b=b+val
        e=a-c
        f=rate
        tq=e
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-04-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-04-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
            
    if m==5:
        qty=n
        val=qty*rate
        v=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et)
        a=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        e=a-c
        f=rate
        a=a+n
        b=b+(n*f)
        tq=e+n
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-05-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-05-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
            
    if m==6:
        qty=n
        val=qty*rate
        v=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et)
        a=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        a=a
        b=b
        e=a-c
        f=rate
        a=a+n
        b=b+(n*f)
        tq=e+n
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-06-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-06-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
            
    if m==7:
        qty=n
        val=qty*rate
        v=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et)
        a=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        e=a-c
        f=rate
        a=a+n
        b=b+(n*f)
        tq=e+n
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-07-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-07-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
            
    if m==8:
        qty=n
        val=qty*rate
        v=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et)
        a=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        e=a-c
        f=rate
        a=a+n
        b=b+(n*f)
        tq=e+n
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-08-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-08-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
            
    if m==9:
        qty=n
        val=qty*rate
        v=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et)
        a=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        e=a-c
        f=rate
        a=a+n
        b=b+(n*f)
        tq=e+n
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-09-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-09-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
            
    if m==10:
        qty=n
        val=qty*rate
        v=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et)
        a=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        e=a-c
        f=rate
        a=a+n
        b=b+(n*f)
        tq=e+n
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-10-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-10-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
            
    if m==11:
        qty=n
        val=qty*rate
        v=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et)
        a=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        e=a-c
        f=rate
        a=a+n
        b=b+(n*f)
        tq=e+n
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-11-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-11-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
            
    if m==12:
        qty=n
        val=qty*rate
        v=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et)
        a=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        e=a-c
        f=rate
        a=a+n
        b=b+(n*f)
        tq=e+n
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-12-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-12-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
            
    if m==1:
        qty=n
        val=qty*rate
        v=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et)
        a=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        e=a-c
        f=rate
        a=a+n
        b=b+(n*f)
        tq=e+n
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-01-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-01-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
            
    if m==2:
        qty=n
        val=qty*rate
        v=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et)
        a=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        e=a-c
        f=rate
        a=a+n
        b=b+(n*f)
        tq=e+n
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-02-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-02-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
            
    if m==3:
        qty=n
        val=qty*rate
        v=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et)
        a=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        b=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='purchase').aggregate(value=Coalesce(Sum('value'),0))['value']
        c=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
        d=voucherlist.objects.filter(item_id=sk,date__gte=st,date__lte=et,vouch_type='sale').aggregate(value=Coalesce(Sum('value'),0))['value']
        e=a-c
        f=rate
        a=a+n
        b=b+(n*f)
        tq=e+n
        fr=tq*f
        for vi in v:
            ed=vi.date
            pur_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-03-01',date__lte=ed,vouch_type='purchase').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            sale_qty=voucherlist.objects.filter(item_id=sk,date__gte='2022-03-01',date__lte=ed,vouch_type='sale').aggregate(quantity=Coalesce(Sum('quantity'),0))['quantity']
            vi.cbalance=qty+(pur_qty-sale_qty)
            vi.cvalue=vi.cbalance*rate
                                   
    
    con={
        'v':v,
        'si':si,
        'm':m,
        'a':a,
        'b':b,
        'c':c,
        'd':d,
        'e':e,
        'f':f,
        'qty':qty,
        'val':val,
        'fr':fr ,'tq':tq ,'n':n,
        'si':si,'cmp':cmp  
        }
    return render(request, 'periodvouchersummary.html',con)


def categorysummary(request):
    return render(request, 'categorysummary.html')


def primarycategory(request):
    return render(request, 'primarycategory.html')

def categorysummarypage(request):
    return render(request, 'categorysummarypage.html')

def secondarycategory(request):
    return render(request, 'secondarycategorypage.html')

def productcategory(request):
    return render(request, 'productcategory.html')


#......................Praveen........................

def list_of_ledger(request):
    led=tally_ledger.objects.all()
    context={'led':led}
    return render(request,'list_of_ledger.html',context)

def list_of_groups(request):
	grup=tally_group.objects.all()
	context={'grup':grup}
	return render(request,'list_of_groups.html',context)

def list_of_voucher_type(request):
    vou=Voucher.objects.all()
    context={'vou':vou}
    return render(request,'list_of_voucher_type.html',context)

def list_of_currency(request):
    curr=currencyAlteration.objects.all()
    context={'curr':curr}
    return render(request,'list_of_currency.html',context)

def companyCreate1(request):
    return render(request,'create_companys.html')

def create_company(request):
    if request.method=='POST':
        dp=request.POST.get('dpath')
        cn=request.POST.get('name')
        mn=request.POST.get('mailing_name')
        ca=request.POST.get('address1')
        cs=request.POST.get('state')
        cc=request.POST.get('country')
        pin=request.POST.get('pincode')
        tel=request.POST.get('telephone')
        mob=request.POST.get('mobile')
        fax=request.POST.get('fax')
        email=request.POST.get('email')
        web=request.POST.get('website')
        fy=request.POST.get('fin_begin')
        bks=request.POST.get('books_begin')
        bc=request.POST.get('currency_symbol')
        fr=request.POST.get('formal_name')
        cmp=Companies.objects.filter(name=cn)
        out=datetime.strptime (fy,'%Y-%m-%d')+timedelta (days=364) 
        print(out)
        a=out.date()
        print(a)
        if cmp:
            messages.info(request,'Company name already exists!!')
        else:
            com=Companies(d_path=dp,
                                name=cn,
                                mailing_name=mn,
                                address=ca,
                                state=cs,
                                country=cc,
                                pincode=pin,
                                telephone=tel,
                                mobile=mob,
                                fax=fax,
                                email=email,
                                website=web,
                                fin_begin=fy,
                                books_begin=bks,
                                currency_symbol=bc,
                                formal_name=fr,
                                fin_end=a,)
            com.save()
            
                        
            return render(request,'company_feature_form.html',{'com':com})
    return render(request,'create_companys.html')

def companies_feature(request):
    return render(request,'company_feature_form.html')

def list_of_companies(request):
    return render(request,'list_of_companies.html')

def select_company1(request):
    comp=Companies.objects.all()
    
    return render(request,'select_company.html',{'comp1':comp})

def shut_company1(request):
	com=Companies.objects.all() 
	return render(request, 'shut_company.html',{'com':com})

def shut2(request,pk):
    c=Companies.objects.get(id=pk)
    c.status=False
    c.save()
    return redirect('shut_company') 

def enable2(request,pk):
    c=Companies.objects.get(id=pk)
    c.status=True
    c.save()
    return redirect('shut_company')

def list_of_cost_centers(request):
    cst=cost_center.objects.all()
    return render(request,'list_of_cost_centers.html',{'cst':cst})

# def shut_card(request):
#     return render(request,'shut_card.html')

def load_ledger_alter(request,pk):
    led=tally_ledger.objects.get(id=pk)
    lga=tally_group.objects.all()
    if request.method=='POST':
        led.name=request.POST.get('name')
        led.alias=request.POST.get('alias')
        led.under=request.POST.get('under')
        led.mname=request.POST.get('mailingname')
        led.address=request.POST.get('address')
        led.state=request.POST.get('state')
        led.country=request.POST.get('country')
        led.pincode=request.POST.get('pincode')
        led.pan_no=request.POST.get('pan_no')
        led.bank_details=request.POST.get('bank_details')
        led.registration_type=request.POST.get('registration_type')
        led.gst_uin=request.POST.get('gst_uin')
        led.opening_blnc=request.POST.get('opening_blnc')

        led.set_odl=request.POST.get('set_odl')
        led.aac_holder_nm=request.POST.get('ac_holder_nm')
        led.acc_no=request.POST.get('acc_no')
        led.ifsc_code=request.POST.get('ifsc_code')
        led.swift_code=request.POST.get('swift_code')
        led.bank_name=request.POST.get('bank_name')
        led.branch=request.POST.get('branch')
        led.SA_cheque_bk=request.POST.get('SA_cheque_bk')
        led.Echeque_p=request.POST.get('Echeque_p')
        led.SA_chequeP_con=request.POST.get('SA_chequeP_con')
        led.save()
        print("added")
        return redirect('/')
    return render(request,'load_ledger_alter.html',{'i':led,'lga':lga})

def load_create_ledger(request):
    lg=tally_group.objects.all()
    if request.method=='POST':
        nm=request.POST.get('name')
        als=request.POST.get('alias')
        under=request.POST.get('under')
        mname=request.POST.get('mailingname')
        adr=request.POST.get('address')
        st=request.POST.get('state')
        cntry=request.POST.get('country')
        pin=request.POST.get('pincode')
        pno=request.POST.get('pan_no')
        bdetls=request.POST.get('bank_details')
        rtype=request.POST.get('registration_type')
        gst_uin=request.POST.get('gst_uin')
        opnbn=request.POST.get('opening_blnc')

        spdl=request.POST.get('set_odl')
        achnm=request.POST.get('ac_holder_nm')
        acno=request.POST.get('acc_no')
        ifsc=request.POST.get('ifsc_code')
        scode=request.POST.get('swift_code')
        bn=request.POST.get('bank_name')
        brnch=request.POST.get('branch')
        sacbk=request.POST.get('SA_cheque_bk')
        ecp=request.POST.get('Echeque_p')
        sacpc=request.POST.get('SA_chequeP_con')
        
        ldr=tally_ledger(name=nm,alias=als,under=under,mname=mname,address=adr,state=st,country=cntry,
						pincode=pin,pan_no=pno,bank_details=bdetls,registration_type=rtype,gst_uin=gst_uin,
						opening_blnc=opnbn,set_odl=spdl,ac_holder_nm=achnm,acc_no=acno,ifsc_code=ifsc,swift_code=scode,
						bank_name=bn,branch=brnch,SA_cheque_bk=sacbk,Echeque_p=ecp,SA_chequeP_con=sacpc)
		
        ldr.save()
        return redirect('/')
    
    return render(request,'load_create_ledger.html',{'lg':lg})

def ledger_gst_details(request):
    return render(request,'ledger_gst_details.html')

def ledger_chequebook(request):
    if request.method=='POST':
        cr=request.POST.get('ccon')
        fnum=request.POST.get('from_no')
        tnum=request.POST.get('to_no')
        nchq=request.POST.get('no_chq')
        nachq=request.POST.get('nm_chq')
        chqbk=ledger_cheque_book(chq_range=cr,
                                from_num=fnum,
                                to_no=tnum,
                                no_chq=nchq,
                                nm_chq=nachq,
                
                                    )
        
        chqbk.save()
        print("added")
        return redirect('ledger_chequebook')
    return render(request,'ledger_cheque_book.html')

def ledger_bank_details(request):
    if request.method=='POST':
        bdt=request.POST['bankde']
        tt=request.POST['trans']
        cu=request.POST['cros']
        an=request.POST['acnt']
        ifs=request.POST['ifs']
        bn=request.POST['bank']
        bd=bank_details(bank_de=bdt,
                        trans_type=tt,
                        cros_using=cu,
                        acnt_no=an,
                        ifs=ifs,
                        bank_name=bn,)
        
        bd.save()
        print("added")
    return render(request,'ledger_bank_details.html')

def load_create_groups(request,pk):
    grup=tally_group.objects.get(id=pk)
    if request.method=='POST':
        grup.group_name=request.POST['gname']
        grup.group_alias=request.POST['alias']
        grup.group_under=request.POST['group']
        grup.nature=request.POST['group_nature']
        grup.gross_profit=request.POST['gorss_profit']
        grup.sub_ledger=request.POST['ledger']
        grup.debit_credit=request.POST['debit/credit']
        grup.calculation=request.POST['calculation']
        grup.invoice=request.POST['invoice']
                 
        grup.save()
        print("added")
        return redirect('/')
    return render(request,'load_create_groups.html',{'i':grup})

def load_alter_groups(request):
    return render(request,'load_create_groups.html')

def load_create_ledger2(request):
    if request.method=='POST':
        gname=request.POST['gname']
        galias=request.POST['alias']
        under=request.POST['group']
        nature=request.POST['group_nature']
        gross=request.POST['gorss_profit']
        ledg=request.POST['ledger']
        cred=request.POST['debit/credit']
        calc=request.POST['calculation']
        invc=request.POST['invoice']
        grp=tally_group(group_name=gname,
                group_alias=galias,
                group_under=under,
                nature=nature,
                gross_profit=gross,
                sub_ledger=ledg,
                debit_credit=cred,
                calculation=calc,
                invoice=invc,
                )          
        grp.save()
        print("added")
        return redirect('/')
    return render(request,'load_create_ledger2.html')

def load_voucher_type(request,pk):
    vou=Voucher.objects.get(id=pk)
    if request.method=='POST':
        vou.voucher_name=request.POST['vname']
        vou.alias=request.POST['valias']
        vou.voucher_type=request.POST['vtype']
        vou.abbreviation=request.POST['vabbre']
        vou.voucherActivate=request.POST['vactive']
        vou.voucherNumber=request.POST['vnum']
        vou.preventDuplicate=request.POST['vprev']
        vou.advance_con=request.POST['advcon'] 
        vou.voucherEffective=request.POST['effct']
        vou.transaction=request.POST['trans']
        vou.make_optional=request.POST['opt']
        vou.voucherNarration=request.POST['narrate']
        vou.provideNarration=request.POST['provide']
        vou.manu_jrnl=request.POST['journal']
        vou.track_purchase=request.POST['purchase']
        vou.enable_acc=request.POST['allocate']
        vou.prnt_VA_save=request.POST['vprint']
        vou.jurisdiction=request.POST['juri']
        vou.pos_invoice=request.POST['pos']
        vou.msg_1=request.POST['msg1']
        vou.msg_2=request.POST['msg2']
        vou.default_bank=request.POST['vbank']
        vou.title_print=request.POST['vtitle']
        vou.setAlter=request.POST['vsetalt']
        
        
        
        vou.save()
        print("added")
        return redirect('/')
    return render(request,'load_voucher_type.html',{'i':vou})

def voucher_type_alteration_secondary(request):
    return render(request,'voucher_type_alteration_secondary.html')

def load_create_voucher(request):
    if request.method=='POST':
        vouchername=request.POST['vname']
        voucheralias=request.POST['valias']
        vouchertype=request.POST['vtype']
        abbreviation=request.POST['vabbre']
        vactive=request.POST['vactive']
        vnumber=request.POST['vnum']
        vprevent=request.POST['vprev']
        vadvcon=request.POST['advcon'] 
        veffective=request.POST['effct']
        vtrans=request.POST['trans']
        voptional=request.POST['opt']
        vnarration=request.POST['narrate']
        vprovide=request.POST['provide']
        vjournal=request.POST['journal']
        vpurchase=request.POST['purchase']
        vallocate=request.POST['allocate']
        vprint=request.POST['vprint']
        vjuri=request.POST['juri']
        vpos=request.POST['pos']
        vmsg1=request.POST['msg1']
        vmsg2=request.POST['msg2']
        vbank=request.POST['vbank']
        vtitle=request.POST['vtitle']
        vsetalt=request.POST['vsetalt']
        
        
        vouch=Voucher(voucher_name=vouchername,
                              alias=voucheralias,
                              voucher_type=vouchertype,
                              abbreviation=abbreviation,
                              voucherActivate=vactive,
                              voucherNumber=vnumber,
                              preventDuplicate=vprevent,
                              advance_con=vadvcon,
                              voucherEffective=veffective,
                              transaction=vtrans,
                              make_optional=voptional,
                              voucherNarration=vnarration,
                              provideNarration=vprovide,
                              journal=vjournal,
                              purchase= vpurchase,
                              allocation=vallocate,
                              printVoucher=vprint,
                              jurisdiction=vjuri,
                              POSInvoice=vpos,
                              message1=vmsg1,
                              message2=vmsg2,
                              defaultBank=vbank,
                              titlePrint=vtitle,
                              setAlter=vsetalt,
                             )
        vouch.save()
        print("added")
        return redirect('/')
    return render(request,'load_create_voucher.html')

def load_currency(request):
    return render(request,'load_currency.html')

def company_feature_form(request,pk):
    id=Companies.objects.get(id=pk)
    print(id)

    if request.method=='POST':
        coname=request.POST['name']
        ma=request.POST['main']
        bw=request.POST['bill']
        ecc=request.POST['cost']
        eic=request.POST['inter']
        mi=request.POST['inven']
        iawi=request.POST['intac']
        empl=request.POST['mulpri']
        eb=request.POST['enbat']
        medb=request.POST['mained']
        ejop=request.POST['ejob']
        ect=request.POST['ecost']
        ejc=request.POST['ejoco']
        udci=request.POST['used']
        usa=request.POST['uact']
        gst=request.POST['gst']
        tds=request.POST['tds']
        tcs=request.POST['tcs']
        vat=request.POST['vat']
        enex=request.POST['exci']
        est=request.POST['extax']
        mp=request.POST['mai']
        # eps=request.POST['enpa']
        ema=request.POST['enad']
        mmv=request.POST['mark']
        fc=Features(co_name=coname,
                          maintain_acconts=ma,
                          bill_wise_entry=bw,
                          cost_centers=ecc,
                          interest_calc=eic,
                          maintain_inventory=mi,
                          integrate_accounts=iawi,
                          multiple_price_level=empl,
                          batches=eb,
                          expirydate_batches=medb,
                          joborder_processing=ejop,
                          cost_tracking=ect,
                          job_costing=ejc,
                          discount_invoices=udci,
                          Billed_Quantity=usa,
                          gst=gst,
                          tds=tds,
                          tcs=tcs,
                          vat=vat,
                          excise=enex,
                          servicetax=est,
                          payroll=mp,
                        #   enb_pay=eps,
                          multiple_addrss=ema,
                          vouchers=mmv,
                          company=id,)
        fc.save()
        print("added")
    return render(request,'company_feature_form.html',{'com':id})

def load_rates_of_exchange(request):
    curcc=currencyAlteration.objects.all()
    rat=rateofexchange.objects.all()
    if request.method=='POST':
        
        curncy=request.POST['curname']
        
        cstdrate=request.POST['stdr']
        csrate=request.POST['sr']
        bsrate=request.POST['sr2']
        raex=rateofexchange(
                          
                          std_rate=cstdrate,
                          sell_specified_rate=csrate,
                          buy_specified_rate=bsrate,
                          currencyName=curncy,)
        raex.save()
        print("added")
        return redirect('/')
    return render(request,'load_rates_of_exchange.html',{'curcc':curcc,'rat':rat})

def create_currency3(request):
    
    
    return render(request,'create_currency.html')

def load_cost_centers(request,pk):
    cst=cost_center.objects.get(id=pk)
    ccst=cost_center.objects.all()
    if request.method=='POST':
        cst.c_name=request.POST['cname']
        cst.cost_alias=request.POST['calias']
        cst.under=request.POST['cunder']
        
        cst.save()
        print("added")
        return redirect('/')
    return render(request,'load_cost_centers.html',{'i':cst,'ccst':ccst})

def alter_cost_create(request):
    ccst=cost_center.objects.all()
    if request.method=='POST':
        cname=request.POST['cname']
        calias=request.POST['calias']
        cunder=request.POST['cunder']
        cost=cost_center(c_name=cname,
                cost_alias=calias,
                under=cunder,
                )
        cost.save()
        print("added")
        return redirect('alter_cost_create')
    return render(request,'alter_cost_create.html',{'ccst':ccst})

def load_alter_currency(request):
    if request.method=='POST':
        casymbol=request.POST['symbol']
        caname=request.POST['name']
        caiso=request.POST['iso']
        canumdec=request.POST['numdec']
        caamount=request.POST['amount']
        casuffix=request.POST['suffix']
        casymam=request.POST['symam']
        caamodec=request.POST['amodec']
        cadecwo=request.POST['decwo']
        ca=currencyAlteration(Symbol=casymbol,
                              FormalName=caname,
                              ISOCurrency=caiso,
                              DecimalPlace=canumdec,
                              showAmount=caamount,
                              suffixSymbol=casuffix,
                              AddSpace=casymam,
                              wordRep=caamodec,
                              DecimalWords=cadecwo)
        ca.save()
        print("hi")
        return redirect('list_of_currency')
    return render(request,'load_alter_currency.html')

def currency_alteraion(request,pk):
    calt=currencyAlteration.objects.get(id=pk)
    if request.method=='POST':
        calt.Symbol=request.POST.get('symbol')
        calt.FormalName=request.POST.get('name')
        calt.ISOCurrency=request.POST.get('iso')
        calt.DecimalPlace=request.POST.get('numdec')
        calt.showAmount=request.POST.get('amount')
        calt.suffixSymbol=request.POST.get('suffix')
        calt.AddSpace=request.POST.get('symam')
        calt.wordRep=request.POST.get('amodec')
        calt.DecimalWords=request.POST.get('decwo')
        

        stadate=request.POST.get('standate')
        starate=request.POST.get('stdrate')
        seldate=request.POST.get('selldate')
        selvrate=request.POST.get('selvrate')
        selrate=request.POST.get('selsrate')
        buydate=request.POST.get('buydate')
        buyvrate=request.POST.get('buyvrate')
        buyrate=request.POST.get('buysrate')

        al=Currency_alt(stddate=stadate,
                        stdrate=starate,
                        selldate=seldate,
                        selvorate=selvrate,
                        sellrate=selrate,
                        buydate=buydate,
                        buyvorate=buyvrate,
                        buyrate=buyrate,
                        currencyAlteration_id=pk,)
       
        
        al.save()
        calt.save()
        print("added")
        return redirect('list_of_currency')
    return render(request,'currency_alteraion.html',{'i':calt})


def gst_details3(request,pk):
    id=Companies.objects.get(id=pk)
    company=Companies.objects.get(id=pk)

    if request.method=='POST':
        cmp=request.POST.get('cmpname')
        state=request.POST.get('cstate')
        reg=request.POST.get('creg')
        gapp=request.POST.get('cgapp')
        uin=request.POST.get('cuin')
        peri=request.POST.get('cperi')
        fl=request.POST.get('cflood')
        apf=request.POST.get('capf')
        grate=request.POST.get('cgrate')
        adr=request.POST.get('cadr')
        rev=request.POST.get('crev')
        gclass=request.POST.get('cgclass')
        lut=request.POST.get('clut')
        tv=request.POST.get('ctv')
        tc=request.POST.get('ctc')
        tp=request.POST.get('ctp')
        eway=request.POST.get('ceway')
        appform=request.POST.get('cappform')
        liin=request.POST.get('cliin')
        thr=request.POST.get('cthr')
        intra=request.POST.get('cintra')
        thre=request.POST.get('cthre')
        ewayb=request.POST.get('cewayb')
        einv=request.POST.get('ceinv')
        appli=request.POST.get('cappli')
        billf=request.POST.get('cbillf')
        dper=request.POST.get('cdper')
        snd=request.POST.get('csnd')
        gd=GST(company_name=cmp,
              state=state,
              reg_type=reg,
              gst_applicable=gapp,
              gstin=uin,
              periodicity=peri,
              flood_cess=fl,
              applicable_form1=apf,
              gst_rate_details=grate,
              advance_receipts=adr,
              reverse_charge=rev,
              gst_classification=gclass,
              bond_details=lut,
              tax_rate=tv,
              tax_calc=tc,
              tax_purchase=tp,
              eway_bill=eway,
              applicable_form=appform,
              threshold_includes=liin,
              threshold_limit=thr,
              intrastate=intra,
              threshold_limit2=thre,
              print_eway=ewayb,
              e_invoice=einv,
              app_form=appli,
              billfrom_place=billf,
              dperiod=dper,
              send_ewaybill=snd,
              company=id,)
        gd.save()
        print("added")
    return render(request,'gst_details.html',{'id':id,'companies':company})

def lutbond(request,pk):
    id=Companies.objects.get(id=pk)
    if request.method=='POST':
        lbn=request.POST.get('lbn')
        afrom=request.POST['application_from']
        ato=request.POST['application_to']
        lb=gst_lutbond(lutbond=lbn,
                        validity_from = afrom,
                        validity_to = ato,
                        company=id,)
        lb.save()

    return render(request,'lutbond.html',{'id':id})

def gst_details_of_company(request):
    if request.method=='POST':

        ta=request.POST.get('gta')
        it=request.POST.get('git')
        ce=request.POST.get('gce')
        fc=request.POST.get('gfc')
        gdc=gst_taxability(Taxability=ta,
                            integrated_tax=it,
                            cess=ce,
                            flood_cess=fc,)
        gdc.save()
        return redirect('gst_details_of_company')
    return render(request,'gst_details_of_company.html')

def tds_detuctor(request,pk):
    id=Companies.objects.get(id=pk)

    if request.method=='POST':
        cmp=request.POST.get('tcmpname')
        tr=request.POST.get('ttr')
        tx=request.POST.get('ttx')
        dr=request.POST.get('tdr')
        drb=request.POST.get('tdrb')
        sad=request.POST.get('tsad')
        ii=request.POST.get('tii')
        at=request.POST.get('tat')
        td=Tds_Details(company_name=cmp,
                tan_regno=tr,
                tan=tx,
                deductor_type=dr,
                deductor_branch=drb,
                person_details=sad,
                ignore_it=ii,
                active_tds=at,
                company=id)
        td.save()
        print("added")
    return render(request,'tds_detuctor.html',{'id':id})

def tds_personal(request,pk):
    id=Companies.objects.get(id=pk)
    if request.method=="POST":
        name=request.POST.get('tpname')
        sd=request.POST.get('tpsd')
        dn=request.POST.get('tpdn')
        pn=request.POST.get('tppn')
        ft=request.POST.get('tpft')
        ps=request.POST.get('tpps')
        st=request.POST.get('spst')
        ln=request.POST.get('spln')
        dt=request.POST.get('spdt')
        se=request.POST.get('tpse')
        pin=request.POST.get('tppin')
        mb=request.POST.get('spmb')
        std=request.POST.get('spstd')
        te=request.POST.get('spte')
        el=request.POST.get('spel')
        tp=tds_person(name=name,
                        son_daughter=sd,
                        designation=dn,
                        pan=pn,
                        flat_no=ft,
                        building=ps,
                        street=st,
                        area=ln,
                        town=dt,
                        state=se,
                        pincode=pin,
                        mobile=mb,
                        std=std,
                        telephone=te,
                        email=el,
                        company=id)
        tp.save()
        messages.info(request,'tds personal details added..!!')
    return render(request,'tds_personal.html',{'id':id})

def ledger_cheque_dimenssion(request):
    
    if request.method == 'POST':
            cc=request.POST.get('ccon')
            cw= request.POST.get('cheque_width')
            ch= request.POST.get('cheque_height')
            sle= request.POST.get('startL_leftEdge')
            slte= request.POST.get('startL_topEdge')
            dlle= request.POST.get('distancel_leftEdge')
            dlte= request.POST.get('distancel_topEdge')
            ds= request.POST.get('date_style')
            dts= request.POST.get('date_seperator')
            sw= request.POST.get('separator_width')
            cd= request.POST.get('character_distance')
            pdle= request.POST.get('Pdistancel_leftEdge')
            pdlte= request.POST.get('Pdistancel_topEdge')
            aw= request.POST.get('area_width')
            sldte= request.POST.get('secondL_DTE')
            sflh= request.POST.get('secondfirstL_height')
            fldte= request.POST.get('firstL_dTE')
            slfle= request.POST.get('sl_fisrtl_LE')
            slsle= request.POST.get('sl_secondl_LE')
            awa= request.POST.get('amount_widtharea')
            cfnmp= request.POST.get('currencyFNM_print')
            dfte= request.POST.get('df_TE')
            sle= request.POST.get('startL_LE')
            amwa= request.POST.get('amt_widtharea')
            csp= request.POST.get('currencyS_print')
            cn= request.POST.get('company_name')
            pcn= request.POST.get('print_CN')
            sfs= request.POST.get('salutation_Fsign')
            sss= request.POST.get('salutation_Ssign')
            tes= request.POST.get('top_Edistance')
            slfl= request.POST.get('startLF_leftE')
            wsa= request.POST.get('width_sign_area')
            hsa= request.POST.get('height_sign_area')

            cld= ledger_cheque_demension(cheque_config=cc,cheque_width=cw,cheque_height=ch,startL_leftEdge=sle,startL_topEdge=slte,distancel_leftEdge=dlle,
                                        distancel_topEdge=dlte,date_style=ds,date_seperator=dts,separator_width=sw,character_distance=cd,
                                        Pdistancel_leftEdge=pdle,Pdistancel_topEdge=pdlte,area_width=aw,secondL_DTE=sldte,secondfirstL_height=sflh,
                                        firstL_dTE=fldte,sl_fisrtl_LE=slfle,sl_secondl_LE=slsle,amount_widtharea=awa,currencyFNM_print=cfnmp,
                                        df_TE=dfte,startL_LE=sle,amt_widtharea=amwa,currencyS_print=csp,company_name=cn,print_CN=pcn,
                                        salutation_Fsign=sfs,salutation_Ssign=sss,top_Edistance=tes,startLF_leftE=slfl,width_sign_area=wsa,
                                        height_sign_area=hsa)

            cld.save()
            return redirect('ledger_cheque_dimenssion')
    return render(request,'ledger_cheque_dimenssion.html')



#......................Riya........................

def index1(request):
    comp=Companies.objects.all()
    return render(request,'index1.html',{'comp':comp})

# def basepage(request):
#     comp=Companies.objects.all()
#     return render(request,'base.html',{'comp':comp})

def company(request):
    com=Companies.objects.all()
    return render(request,'company2.html',{'com':com})

def createcompany(request):
    # st=States.objects.all()
    # country=Countries.objects.all()
    return render(request,'createcompany.html')

def companycreate(request):
    
    if request.method=='POST':
        name=request.POST['name']
        mailing_name=request.POST['mailing_name']
        address=request.POST['address']
        
        s=request.POST['state']
        
        print(s)
        country=request.POST['country']   
        print(country) 
        pincode=request.POST['pincode']
        telephone=request.POST['telephone']
        mobile=request.POST['mobile']
        fax=request.POST['fax']
        email=request.POST['email']
        website=request.POST['website']
        fin_begin=request.POST['fin_begin']
        books_begin=request.POST['books_begin']
        currency_symbol=request.POST['currency_symbol']
        formal_name=request.POST['formal_name']
        end=datetime.strptime(fin_begin,'%Y-%m-%d')+timedelta(days=364)
        a=end.date()
        cmp=Companies.objects.filter(name=name)
        if cmp:
            
            messages.info(request,'Company name already exists!!')
            return redirect('createcompany')
        else:
            ctg=Companies(name=name,mailing_name=mailing_name,address=address,state=s,country=country,
                pincode=pincode,
                telephone=telephone,mobile=mobile,fax=fax,email=email,website=website,fin_begin=fin_begin,
                books_begin=books_begin,currency_symbol=currency_symbol,formal_name=formal_name,fin_end=a)
            ctg.save()
            return render(request,'features.html',{'ctg':ctg})
    return render(request,'createcompany.html')


def group1(request,pk):
    # feature=Features.objects.get(company_id=pk)
    cmp=Companies.objects.get(id=pk)
    return render(request,'group1.html',{'cmp':cmp})

def costcentre(request,pk):
    cmp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        cmp=Companies.objects.get(id=pk)
        cname = request.POST['cname']
        alia = request.POST['alia']
        under = request.POST['under']
        costc=cost_centre.objects.filter(cname=cname)
        if costc:
            # messages.info(request,'Company name already exists!!')
            pass
        else:
            
            data = cost_centre(cname=cname,cost_alias=alia,under=under,company=cmp)
            data.save()
            return redirect('index1')
    ccentre=cost_centre.objects.filter(company_id=cmp)
    return render(request,'costcentre.html',{'cmp':cmp,'ccentre':ccentre})

def costcentre2(request,pk):
    cmp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        cmp=Companies.objects.get(id=pk)
        cname = request.POST['cname']
        alia = request.POST['alia']
        under = request.POST['under']
        costc=cost_centre.objects.filter(cname=cname)
        if costc:
            # messages.info(request,'Company name already exists!!')
            pass
        else:
            
            data = cost_centre(cname=cname,cost_alias=alia,under=under,company=cmp)
            data.save()
            return redirect('index')
    ccentre=cost_centre.objects.filter(company_id=cmp)
    return render(request,'costcentre2.html',{'cmp':cmp,'ccentre':ccentre})

def ratesofexchange(request,pk):
    cmp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        cmp=Companies.objects.get(id=pk)
        
        currencyName = request.POST['cr']
        stdrate = request.POST['stdrate']
        # sell_voucher_rate = request.POST['sell_voucher_rate']
        sell_specified_rate = request.POST['sell_specified_rate']
        # buy_voucher_rate = request.POST['buy_voucher_rate']
        buy_specified_rate = request.POST['buy_specified_rate']
        mdl = rateofexchange(
            currencyName=currencyName,
            stdrate=stdrate,
            # sell_voucher_rate=sell_voucher_rate,
            sell_specified_rate=sell_specified_rate,
            # buy_voucher_rate=buy_voucher_rate,
            buy_specified_rate=buy_specified_rate,
            company = cmp)
        mdl.save()
        return redirect('index')
    cur=currencyAlteration.objects.filter(company_id=cmp)
    return render(request,'ratesofexchange.html',{'cmp':cmp,'curr':cur})


def currency1(request,pk):
    cmp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        cmp=Companies.objects.get(id=pk)
        symbol = request.POST['symbol']
        formal_name = request.POST['formal_name']
        currency_code = request.POST['currency_code']
        decimal_places = request.POST['decimal_places']
        show_in_millions = request.POST['show_in_millions']
        suffix_symbol = request.POST['suffix_symbol']
        symbol_and_amount = request.POST['symbol_and_amount']
        after_decimal = request.POST['after_decimal']
        amount_in_words = request.POST['amount_in_words']
        data = currencyAlteration(Symbol=symbol,FormalName=formal_name,ISOCurrency=currency_code,
                        DecimalPlace=decimal_places,showAmount=show_in_millions,
                        suffixSymbol=suffix_symbol,AddSpace=symbol_and_amount,
                        DecimalWords=after_decimal,wordRep=amount_in_words,company=cmp)
        data.save()
        return redirect('index1')
    return render(request,'currency1.html',{'cmp':cmp})

def creategroup(request,pk):
    cmp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        cmp=Companies.objects.get(id=pk)
        gname = request.POST['gname']
        alia = request.POST['alia']
        under = request.POST['under']
        sub_ledger = request.POST['sub_ledger']
        gross = request.POST['gross']
        nett = request.POST['nee']
        calc = request.POST['cal']
        meth = request.POST['meth']
        nature = request.POST['nature']
        grp=tally_group.objects.filter(group_name=gname)
        if grp:
            # messages.info(request,'Company name already exists!!')
            pass
        else:
            mdl = tally_group(
                group_name=gname,
                group_alias=alia,
                group_under=under,
                sub_ledger=sub_ledger,
                debit_credit=nett,
                calculation=calc,
                invoice=meth,
                nature=nature,
                gross_profit=gross,
                company=cmp
            )
            mdl.save()
            return redirect('index1')
    grup=tally_group.objects.filter(company_id=cmp)
    return render(request,'group1.html',{'cmp':cmp,'grup':grup})

def group2(request,pk):
    cmp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        cmp=Companies.objects.get(id=pk)
        gname = request.POST['gname']
        alia = request.POST['alia']
        under = request.POST['under']
        sub_ledger = request.POST['sub_ledger']
        gross = request.POST['gross']
        nett = request.POST['nee']
        calc = request.POST['cal']
        meth = request.POST['meth']
        nature = request.POST['nature']
        grp=tally_group.objects.filter(group_name=gname)
        if grp:
            # messages.info(request,'Company name already exists!!')
            pass
        else:
            mdl = tally_group(
                group_name=gname,
                group_alias=alia,
                group_under=under,
                sub_ledger=sub_ledger,
                debit_credit=nett,
                calculation=calc,
                invoice=meth,
                nature=nature,
                gross_profit=gross,
                company=cmp
            )
            mdl.save()
            return redirect('index1')
    grup=tally_group.objects.filter(company_id=cmp)
    return render(request,'group2.html',{'cmp':cmp,'grup':grup})


def altercompanyview(request):
    com=Companies.objects.all()
    return render(request,'altercompanyview.html',{'com':com})

def altercompany(request,pk):
    # com=States.objects.all()
    # cntry=Countries.objects.all()
    comp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        comp.name=request.POST['name']
        comp.mailing_name=request.POST['mailing_name']
        comp.address=request.POST['address']
        
        comp.states=request.POST['state']
        comp.country=request.POST['country']
        
        comp.pincode=request.POST['pincode']
        comp.telephone=request.POST['telephone']
        comp.mobile=request.POST['mobile']
        comp.fax=request.POST['fax']
        comp.email=request.POST['email']
        comp.website=request.POST['website']
        comp.fin_begin=request.POST['fin_begin']
        comp.books_begin=request.POST['books_begin']
        comp.currency_symbol=request.POST['currency_symbol']
        comp.formal_name=request.POST['formal_name']
        comp.save()
        return redirect('altercompanyview')
    return render(request,'editcompany.html',{'comp':comp})



def selectcompany(request):
    com=Companies.objects.all()
    return render(request,'selectcompany.html',{'com':com})

def addstate(request):
    if request.method=='POST':
        name=request.POST['name']
        cntryid=request.POST['cname']
        st=States.objects.filter(name=name)
        countr=Countries.objects.filter(name=cntryid)
        if st:
            # messages.info(request,'Company name already exists!!')
            return redirect('createcompany')
        else:
            data=States(name=name, country=countr)
            data.save()
            return redirect('createcompany')
    return render(request,'createcompany.html')

def addstatenew(name):
    return "";

def addcountry(request):
    if request.method=='POST':
        name=request.POST['name']
        con=Countries.objects.filter(name=name)
        if con:
            # messages.info(request,'Company name already exists!!')
            return redirect('createcompany')
        else:
            data=Countries(name=name)
            data.save()
        return redirect('createcompany')
    return render(request,'createcompany.html')

def featurecompany(request,pk):
    comp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        maintain_accounts=request.POST['maintain_accounts']
        ctg=features(maintain_accounts=maintain_accounts, company= comp)
        ctg.save()
    return render(request,'company2.html')

def features1(request, pk):
    feature=Features.objects.get(company_id=pk)
    c=Companies.objects.get(id=pk)
    if request.method == 'POST':
        if request.POST['maintain_accounts'] == 'Yes':
            feature.maintain_accounts= 'True'
        else:
            feature.maintain_accounts= 'False'
        if request.POST['bill_wise_entry'] == 'Yes':
            feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['cost_centres'] == 'Yes':
            feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['interest_calc'] == 'Yes':
            feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['maintain_inventory'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['integrate_accounts'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['multiple_price_level'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['batches'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['expirydate_batches'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['joborder_processing'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        
        if request.POST['cost_tracking'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['job_costing'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['discount_invoices'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['Billed_Quantity'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['gst'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['tds'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['tcs'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['vat'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['excise'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['servicetax'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['payroll'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['multiple_addrss'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        if request.POST['vouchers'] == 'Yes':
                feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        
        feature.save()
    return render(request,'features1.html',{'ctg':c, 'ft':feature})

def shutcompany(request):
    com=Companies.objects.all()
    return render(request,'shutcompany1.html',{'com':com})

def disable(request,pk):
    c=Companies.objects.get(id=pk)
    c.status=False
    c.save()
    return redirect('/')

# def enable(request,pk):
#     c=Companies.objects.get(id=pk)
#     c.status=True
#     c.save()
#     return redirect('shutcompany')

def featurepage(request):
    comp=Companies.objects.all()
    return render(request,'featurepage.html',{'comp':comp})



#......................Neethu.......................

def create(request):
    Country=Countries.objects.all()
    return render(request,'company1.html',{'country':Country})

def companycreate1(request):
    
    if request.method=="POST":
        name=request.POST['companyname']
        print(name)
        mailing_name=request.POST['mailing_name']
        print(mailing_name)
        address=request.POST['address']
        print(address)
        state=request.POST['state']
        print(state)
        country=request.POST['country']
        print(country)
        pincode=request.POST['pincode']
        print(pincode)
        telephone=request.POST['telephone']
        print(telephone)
        mobile=request.POST['mobile']
        print(mobile)
        fax=request.POST['fax']
        print(fax)
        email=request.POST['email1']
        print(email)
        website=request.POST['website']
        print(website)
        fin_begin=request.POST['fyear']
        print(fin_begin)
        books_begin=request.POST['byear']
        print(books_begin)
        currency_symbol=request.POST['currency']
        print(currency_symbol)
        formal_name=request.POST['formal']
        print(formal_name)
        cmp=Companies.objects.filter(name=name)
        
        out=datetime.datetime.strptime (fin_begin,'%Y-%m-%d')+timedelta (days=364) 
        print(out)
        a=out.date()
        print(a)
        if cmp:
            messages.info(request,'Company name already exists!!')
            return redirect('create')
        else:
            ctg=Companies(name=name,mailing_name=mailing_name,address=address,state=state,country=country,
                pincode=pincode,telephone=telephone,mobile=mobile,fax=fax,email=email,website=website,fin_begin=fin_begin,
                books_begin=books_begin,currency_symbol=currency_symbol,formal_name=formal_name,fin_end=a)
                
            ctg.save()
            messages.info(request,'Company created successfully(Enable the features as per your business needs)')
            return render(request,'features2.html',{'ctg':ctg})


def gst_details(request,pk):
    company=Companies.objects.get(id=pk)
    return render(request,'gst_details1.html',{'companies':company})

def add_gstdetails(request,pk):
    id=Companies.objects.get(id=pk)
    comp=Companies.objects.get(id=pk)
    
    if request.method=="POST":
        state=request.POST['state']
        registration_type=request.POST['registration_type']
        assessee=request.POST['assessee']
        fdate=request.POST['fdate']
        gstin=request.POST['gstin']
        periodicity=request.POST['periodicity']
        alter_gst=request.POST['alter_gst']
        tax_liabilityadvance=request.POST['tax_liabilityadvance']
        tax_liability=request.POST['tax_liability']
        gst_classifications=request.POST['gst_classifications']
        bond_details=request.POST['bond_details']
        eway_bill=request.POST['eway_bill']
        applicable_from=request.POST['applicable_from']
        treshold_limit=request.POST['treshold_limit']
        treshold_limit1=request.POST['treshold_limit1']
        intrastate=request.POST['intrastate']
        treshold_limit2=request.POST['treshold_limit2']
        print_ewaybill=request.POST['print_ewaybill']
        e_invoicing=request.POST['e_invoicing']
        applicable_from=request.POST['applicable_from']
        bill_from_place=request.POST['bill_from_place']
        period=request.POST['period']
        send_eway=request.POST['send_eway']
        gst=GST(state= state,reg_type=registration_type,assessee= assessee,gst_applicable= fdate,gstin= gstin,periodicity= periodicity,
                        gst_rate_details= alter_gst,advance_receipts=tax_liabilityadvance,reverse_charge=tax_liability,gst_classification= gst_classifications,
                        bond_details=bond_details,eway_bill= eway_bill,applicable_form=applicable_from,threshold_includes= treshold_limit,
                         threshold_limit=treshold_limit1,intrastate=intrastate,threshold_limit2=treshold_limit2,print_eway=print_ewaybill,e_invoice= e_invoicing,app_from=applicable_from,billfrom_place=bill_from_place,dperiod=period,send_ewaybill=send_eway,company=id)
        gst.save()
        messages.info(request,'Gst details added..!!')
    return redirect(request.META.get('HTTP_REFERER'))    

def tds_deductor(request,pk):
    comp=Companies.objects.get(id=pk)
    return render(request,'tds_deductor.html',{'company':comp})

def person_details(request,pk):
    com=Companies.objects.get(id=pk)
    return render(request,'person_details.html',{'comp':com})  

def add_person(request,pk):
    id=Companies.objects.get(id=pk)
    if request.method=="POST":
        name=request.POST['name']
        fname=request.POST['fname']
        Designation=request.POST['Designation']
        pan=request.POST['pan']
        address=request.POST['address']
        bname=request.POST['bname']
        road=request.POST['road']
        area=request.POST['area']
        city=request.POST['city']
        pin=request.POST['pin']
        state=request.POST['state']
        mobile=request.POST['mobile']
        std=request.POST['std']
        telephone=request.POST['telephone']
        email=request.POST['email']
        
        person=tds_person(name=name,son_daughter=fname,designation=Designation,pan=pan,flat_no=address,building=bname,street=road,area=area,town=city,
                      pincode=pin,state=state,mobile=mobile,std=std,telephone=telephone,email=email,company=id)
        person.save()
        messages.info(request,'Person details added..!!')
    return redirect(request.META.get('HTTP_REFERER'))  

def add_tds(request,pk):
    id=Companies.objects.get(id=pk)
    if(request.method=="POST"):
        tan_number=request.POST['tan_number']
        tan=request.POST['tan']
        deductor=request.POST['deductor']
        branch=request.POST['branch']
        person_details=request.POST['person_details']
        exemption=request.POST['exemption']
        active_tds=request.POST['active_tds']
        tds=Tds_Details(tan_regno=tan_number,tan=tan,deductor_type=deductor,deductor_branch=branch,person_details= person_details,
                        ignore_it=exemption,active_tds=active_tds,company=id)
        tds.save()
        messages.info(request,'TDS details added..!!')
    return redirect(request.META.get('HTTP_REFERER'))    

def features2(request,pk):
    id=Companies.objects.get(id=pk)
    # feature=Features.objects.get(company=pk)
    print(id)
    if request.method == "POST":
        maintain_accounts=request.POST['maintain_accounts']
        bill_wise_entry=request.POST['bill_wise_entry']
        cost_centres=request.POST['cost_centres']
        interest_calc=request.POST['interest_calc']
        maintain_inventory=request.POST['maintain_inventory']
        integrate_accounts=request.POST['integrate_accounts']
        multiple_price_level=request.POST['multiple_price_level']
        batches=request.POST['batches']
        expirydate_batches=request.POST['expirydate_batches']
        joborder_processing=request.POST['joborder_processing']
        cost_tracking=request.POST['cost_tracking']
        job_costing=request.POST['job_costing']
        Discount_coloumn=request.POST['Discount_coloumn']
        billed_quantity=request.POST['billed_quantity']
        gst=request.POST['gst']
        
        tds=request.POST['tds']
        tcs=request.POST['tcs']
        vat=request.POST['vat']
        excise=request.POST['excise']
        service_tax=request.POST['service_tax']
        payroll=request.POST['payroll']
       
        multiple_address=request.POST['multiple_address']
        Modified_vouchers=request.POST['Modified_vouchers']
        feature=Features(maintain_accounts=maintain_accounts,bill_wise_entry=bill_wise_entry, cost_centres= cost_centres,interest_calc=interest_calc,
                         maintain_inventory= maintain_inventory,integrate_accounts=integrate_accounts, multiple_price_level= multiple_price_level,
                          batches= batches, expirydate_batches= expirydate_batches,joborder_processing=joborder_processing,cost_tracking= cost_tracking,
                          job_costing=job_costing,discount_invoices=Discount_coloumn,Billed_Quantity=billed_quantity,gst=gst,tds=tds,tcs=tcs,vat=vat,
                          excise=excise, servicetax=service_tax,payroll=payroll,multiple_addrss=multiple_address,
                           vouchers=Modified_vouchers,company=id)
        feature.save() 
        
        return redirect('dashboard')
    return render(request,'features2.html',{'ctg':id})

def dashboard(request):
    com=Companies.objects.filter(status=True)
    
       
    comp1=Companies.objects.first()
    comp1.status=True
   
    comp1.save()
    return render(request,'dashboard.html',{'comp1':comp1,'com1':com})

# def company_list(request):
#     com=Companies.objects.all()
#     return render(request,'company_list.html',{'comp':com})       

def select_company(request):
    comp=Companies.objects.all()
    
    return render(request,'select_company1.html',{'comp1':comp})

def dash_board(request,pk):
    comp=Companies.objects.get(id=pk)
    comp.status=True
    comp.save()
    com=Companies.objects.filter(status=True)  
    return render(request,'dashboard.html',{'comp1':comp,'com1':com})

def alter_company(request):
    comp=Companies.objects.all()
    return render(request,'alter_company.html',{'comp1':comp})

def edit_page(request,pk):
    country=Countries.objects.all()
    com=Companies.objects.get(id=pk)
    return render(request,'edit_company.html',{'com':com,'country':country})

def edit_companydetails(request,pk):
    com=Companies.objects.get(id=pk)
    if request.method=="POST":
        com.name=request.POST['companyname']
       
        com.mailing_name=request.POST['mailing_name']
       
        com.address=request.POST['address']
        
        com.state=request.POST['state']
      
        com.country=request.POST['country']
       
        com.pincode=request.POST['pincode']
        
        com.telephone=request.POST['telephone']
        
        com.mobile=request.POST['mobile']
        
        com.fax=request.POST['fax']
        
        com.email=request.POST['email']
       
        com.website=request.POST['website']
        
        com.fin_begin=request.POST['fyear']
        com.books_begin=request.POST['byear']
       
        com.currency_symbol=request.POST['currency']
        
        com.formal_name=request.POST['formal']
        com.save()
        return redirect('dashboard')

def change_company1(request):
    com=Companies.objects.filter(status=True) 
    return render(request,'change_company1.html',{'com':com})        

def shut_company(request):
    com=Companies.objects.filter(status=True) 
    return render(request,'shut_company.html',{'com':com})

def shut1(request,pk):
    com=Companies.objects.get(id=pk)
    com.status=False
    com.save()
    comp1=Companies.objects.first()
    com=Companies.objects.filter(status=True) 
    return render(request,'dashboard.html',{'com1':com,'comp1':comp1})

def date_change(request):
    return render(request,'date.html')

def print_config(request):
    return render(request,'print_config.html')

def add_country(request):
    if request.method=="POST":
        print("a")
        country=request.POST['country_name']
        print(country)
        countries=Countries(name=country)
        countries.save()
        return redirect('create') 

def addstates(request):
    
    state=States.objects.filter(country_id=id)
    print(state)
    return render(request,'company1.html',{'state':state})

def state_country(request):
    return render(request,'state_country.html')

def load_cities(request):
    country_id=request.POST['country_id']
    states=States.objects.filter(country_id=country_id)
    return render(request,'company1.html',{'states':states})

def  edit_features(request,pk):
    id=Companies.objects.get(id=pk)
    # feature=Features.objects.get(company=pk)
    print(id)
    if request.method == "POST":
        maintain_accounts=request.POST['maintain_accounts']
        bill_wise_entry=request.POST['bill_wise_entry']
        cost_centres=request.POST['cost_centres']
        interest_calc=request.POST['interest_calc']
        maintain_inventory=request.POST['maintain_inventory']
        integrate_accounts=request.POST['integrate_accounts']
        multiple_price_level=request.POST['multiple_price_level']
        batches=request.POST['batches']
        expirydate_batches=request.POST['expirydate_batches']
        joborder_processing=request.POST['joborder_processing']
        cost_tracking=request.POST['cost_tracking']
        job_costing=request.POST['job_costing']
        Discount_coloumn=request.POST['Discount_coloumn']
        billed_quantity=request.POST['billed_quantity']
        gst=request.POST['gst']
        
        tds=request.POST['tds']
        tcs=request.POST['tcs']
        vat=request.POST['vat']
        excise=request.POST['excise']
        service_tax=request.POST['service_tax']
        payroll=request.POST['payroll']
        
        multiple_address=request.POST['multiple_address']
        Modified_vouchers=request.POST['Modified_vouchers']
        feature=Features(maintain_accounts=maintain_accounts,bill_wise_entry=bill_wise_entry, cost_centres= cost_centres,interest_calc=interest_calc,
                         maintain_inventory= maintain_inventory,integrate_accounts=integrate_accounts, multiple_price_level= multiple_price_level,
                          batches= batches, expirydate_batches= expirydate_batches,joborder_processing=joborder_processing,cost_tracking= cost_tracking,
                          job_costing=job_costing,discount_invoices=Discount_coloumn,Billed_Quantity=billed_quantity,gst=gst,tds=tds,tcs=tcs,vat=vat,
                          excise=excise, servicetax=service_tax,payroll=payroll,multiple_addrss=multiple_address,
                           vouchers=Modified_vouchers,company=id)
        feature.save() 
        
        return redirect('dashboard')
    return render(request,'edit_features.html',{'ctg':id})

def edit_gst_details(request,pk):
    id=Companies.objects.get(id=pk)
    comp=Companies.objects.get(id=pk)
    gst=GST.objects.get(company_id=pk)
    
    return render(request,'edit_gst_details.html',{'gst':gst,'comp':comp})

def add_newgstdetails(request,pk):
    gst=GST.objects.get(company_id=pk)
    if request.method=="POST":
        gst.state=request.POST['state']
        gst.registration_type=request.POST['registration_type']
        gst.assessee=request.POST['assessee']
        gst.fdate=request.POST['fdate']
        gst.gstin=request.POST['gstin']
        gst.periodicity=request.POST['periodicity']
        gst.alter_gst=request.POST['alter_gst']
        gst.tax_liabilityadvance=request.POST['tax_liabilityadvance']
        gst.tax_liability=request.POST['tax_liability']
        gst.gst_classifications=request.POST['gst_classifications']
        gst.bond_details=request.POST['bond_details']
        gst.eway_bill=request.POST['eway_bill']
        gst.applicable_from=request.POST['applicable_from']
        gst.treshold_includes=request.POST['treshold_limit']
        gst.treshold_limit=request.POST['treshold_limit1']
        gst.intrastate=request.POST['intrastate']
        gst.treshold_limit2=request.POST['treshold_limit2']
        gst.print_ewaybill=request.POST['print_ewaybill']
        gst.e_invoicing=request.POST['e_invoicing']
        gst.app_from=request.POST['applicable_from']
        gst.billfrom_place=request.POST['bill_from_place']
        gst.dperiod=request.POST['period']
        gst.send_ewaybill=request.POST['send_eway']
        gst.save()
        messages.info(request,'Gst details updated..!!')
    return redirect(request.META.get('HTTP_REFERER'))

def edit_tds_deductor(request,pk):
    id=Companies.objects.get(id=pk)
    comp=Companies.objects.get(id=pk)
    tds=Tds_Details.objects.get(company_id=pk)
    
    return render(request,'edit_tds_details.html',{'tds':tds,'comp':comp})

def add_newtdsdetails(request,pk):
    tds=Tds_Details.objects.get(company_id=pk)
    if(request.method=="POST"):
        tds.tan_number=request.POST['tan_number']
        tds.tan=request.POST['tan']
        tds.deductor=request.POST['deductor']
        tds.branch=request.POST['branch']
        tds.person_details=request.POST['person_details']
        tds.exemption=request.POST['exemption']
        tds.active_tds=request.POST['active_tds']
        
        tds.save()
        messages.info(request,'TDS details updated..!!')
    return redirect(request.META.get('HTTP_REFERER'))   

def edit_person_details(request,pk):
    id=Companies.objects.get(id=pk)
    comp=Companies.objects.get(id=pk)
    person=tds_person.objects.get(company_id=pk)
    
    return render(request,'editperson_details.html',{'person':person,'comp':comp})

def add_newpersondetails(request,pk):
    person=tds_person.objects.get(company_id=pk)
    if request.method=="POST":
        person.name=request.POST['name']
        person.fname=request.POST['fname']
        person.Designation=request.POST['Designation']
        person.pan=request.POST['pan']
        person.address=request.POST['address']
        person.bname=request.POST['bname']
        person.road=request.POST['road']
        person.area=request.POST['area']
        person.city=request.POST['city']
        person.pin=request.POST['pin']
        person.state=request.POST['state']
        person.mobile=request.POST['mobile']
        person.std=request.POST['std']
        person.telephone=request.POST['telephone']
        person.email=request.POST['email']
        
       
        person.save()
        messages.info(request,'Person details Updated..!!')
    return redirect(request.META.get('HTTP_REFERER'))  

def company_list1(request):
    com=Companies.objects.all()
    return render(request,'company_list1.html',{'comp':com})  



#......................Rafi........................

def stock_group(request):
    und=CreateStockGrp.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under_name=request.POST['under_name']
        quantities=request.POST['quantities']
        stockgrp=CreateStockGrp(name=name,alias=alias,under_name=under_name,quantities=quantities)
        stockgrp.save()
        return redirect('stock_group')
    return render(request,'stock_group.html',{'und':und})

def stock_group_secondary(request):
    und=CreateStockGrp.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under_name=request.POST['under_name']
        quantities=request.POST['quantities']
        stockgrp=CreateStockGrp(name=name,alias=alias,under_name=under_name,quantities=quantities)
        stockgrp.save()
        return redirect('stock_group')
    return render(request,'stock_group(secondary).html',{'und':und})

def stock_category_creation(request):
    und=CreateStockCateg.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under_name=request.POST['under_name']
        stockCateg=CreateStockCateg(name=name,alias=alias,under_name=under_name)
        stockCateg.save()
    return render(request,'stock_category_creation.html',{'und':und})

def stock_category_secondary(request):
    und=CreateStockCateg.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under_name=request.POST['under_name']
        stockCateg=CreateStockCateg(name=name,alias=alias,under_name=under_name)
        stockCateg.save()
        return redirect('stock_category_creation')
    return render(request,'stock_category(secondary).html',{'und':und})

def stock_items(request):
    cat=CreateStockCateg.objects.all()
    grp=CreateStockGrp.objects.all()
    unt=UnitCrt.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under=request.POST['under']
        category=request.POST['category']
        units=request.POST['units']
        batches=request.POST['batches']
        manufacturing_date=request.POST['manufacturing_date']
        expiry_dates=request.POST['expiry_dates']
        rate_of_duty=request.POST['rate_of_duty']
        quantity=request.POST['quantity']
        rate=request.POST['rate']
        per=request.POST['per']
        value=request.POST['value']
        additional=request.POST['additional']
        crt=stock_item_crt(name=name,alias=alias,under=under,category=category,units=units,batches=batches,
                           manufacturing_date=manufacturing_date,expiry_dates=expiry_dates,
                           rate_of_duty=rate_of_duty,quantity=quantity,rate=rate,per=per,value=value,additional=additional)
        crt.save()
    return render(request,'stock_items.html',{'cat':cat,'grp':grp,'unt':unt})


def unit_creation(request):
    unit=UnitCrt.objects.all()
    if request.method=='POST':
        type=request.POST['type']
        symbol=request.POST['symbol']
        formal_name=request.POST['formal_name']
        uqc=request.POST['uqc']
        decimal=request.POST['decimal']
        first_unit=request.POST['first_unit']
        conversion=request.POST['conversion']
        second_unit=request.POST['second_unit']
        crt=UnitCrt(type=type,symbol=symbol,formal_name=formal_name,uqc=uqc,decimal=decimal,first_unit=first_unit,conversion=conversion,second_unit=second_unit)
        crt.save()
    return render(request,'unit1.html',{'unit':unit})

def uqc(request):
    unit=UnitCrt.objects.all()
    if request.method=='POST':
        uqc=request.POST['uqc']
        crt=UnitCrt(uqc=uqc)
        crt.save()
        return redirect('unit_creation')
    return render(request,'uqc.html')

def unit_creation_secondary(request):
    unit=UnitCrt.objects.all()
    if request.method=='POST':
        type=request.POST['type']
        symbol=request.POST['symbol']
        formal_name=request.POST['formal_name']
        uqc=request.POST['uqc']
        decimal=request.POST['decimal']
        first_unit=request.POST['first_unit']
        conversion=request.POST['conversion']
        second_unit=request.POST['second_unit']
        crt=UnitCrt(type=type,symbol=symbol,formal_name=formal_name,uqc=uqc,decimal=decimal,first_unit=first_unit,conversion=conversion,second_unit=second_unit)
        crt.save()
    return render(request,'unit_creation(secondary).html',{'unit':unit})

def uqc_secondary(request):
    unit=UnitCrt.objects.all()
    if request.method=='POST':
        uqc=request.POST['uqc']
        crt=UnitCrt(uqc=uqc)
        crt.save()
        return redirect('unit_creation')
    return render(request,'uqc.html')

def godown_alteration(request):
    gd=CreateGodown.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under_name=request.POST['under_name']
        gdcrt=CreateGodown(name=name,alias=alias,under_name=under_name)
        gdcrt.save()
    return render(request,'godown_alteration.html',{'gd':gd})

def godown_secondary(request):
    gd=CreateGodown.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under_name=request.POST['under_name']
        gdcrt=CreateGodown(name=name,alias=alias,under_name=under_name)
        gdcrt.save()
        return redirect('godown_alteration')
    return render(request,'godown(secondary).html',{'gd':gd})

def employee_group_creation(request):
    emp=CreateEmployeeGrp.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under_name=request.POST['under_name']
        crt=CreateEmployeeGrp(name=name,alias=alias,under_name=under_name)
        crt.save()
    return render(request,'employee_group_creation.html',{'emp':emp})

def emloyee_group_secondary(request):
    emp=CreateEmployeeGrp.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under_name=request.POST['under_name']
        crt=CreateEmployeeGrp(name=name,alias=alias,under_name=under_name)
        crt.save()
    return render(request,'employee_group(secondary).html',{'emp':emp})


def employee_creation(request):
    grp=CreateEmployeeGrp.objects.all()
    emp=employee_crt.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under_name=request.POST['under_name']
        doj=request.POST['doj']
        salary=request.POST['salary']
        empno=request.POST['empno']
        designation=request.POST['designation']
        function_name=request.POST['function_name']
        location=request.POST['location']
        gender=request.POST['gender']
        dob=request.POST['dob']
        bld_grp=request.POST['bld_grp']
        father_mother=request.POST['father_mother']
        spouse=request.POST['spouse']
        address=request.POST['address']
        phn=request.POST['phn']
        email=request.POST['email']
        bank=request.POST['bank']
        incometax=request.POST['incometax']
        adhar=request.POST['adhar']
        uan=request.POST['uan']
        pf=request.POST['pf']
        pr=request.POST['pr']
        esi=request.POST['esi']
        crt=employee_crt(name=name,alias=alias,under_name=under_name,doj=doj,salary=salary,empno=empno,designation=designation,
                         function_name=function_name,location=location,gender=gender,dob=dob,bld_grp=bld_grp,father_mother=father_mother,
                         spouse=spouse,address=address,phn=phn,email=email,bank=bank,incometax=incometax,adhar=adhar,uan=uan,pf=pf,pr=pr,esi=esi)
        crt.save()
        request.session["name"]=name            
    return render(request,'employee_creation.html',{'emp':emp,'grp':grp})
    
def price_levels(request):
    if request.method=="POST":
        number=request.POST['number']
        crt=Price_level_crt(number=number)
        crt.save()
        return redirect('price_levels')
    price=Price_level_crt.objects.all()
    return render(request,'price_levels.html',{"price":price})

def pan_cin(request):
    pc=pancin.objects.all()
    if request.method=='POST':
        pan=request.POST['pan']
        cin=request.POST['cin']
        crt=pancin(pan=pan,cin=cin)
        crt.save()
    return render(request,'pan_cin.html')

def pay_head(request):
    att=attendance_crt.objects.all()
    pay=payhead_crt.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        payhead_type=request.POST['payhead_type']
        under_name=request.POST['under_name']
        net_salary=request.POST['net_salary']
        pay_slip_name1=request.POST['pay_slip_name']
        currency_ledger=request.POST['currency_ledger']
        calculation_type=request.POST['calculation_type']
        attendance_type=request.POST['attendance_type']
        production_type=request.POST['production_type']
        crt=payhead_crt(name=name,alias=alias,payhead_type=payhead_type,under_name=under_name,net_salary=net_salary,pay_slip_name=pay_slip_name1,currency_ledger=currency_ledger,calculation_type=calculation_type
                        ,attendance_type=attendance_type,production_type=production_type)
        crt.save()
    return render(request,'pay_head.html',{'att':att,'pay':pay})


def load(request):
    did=request.GET.get("id")
    obj=payhead_crt.objects.get(name=did)
    return render(request,"load.html",{"obj":obj})

def load_calculation(request):
    did=request.GET.get("id")
    obj=payhead_crt.objects.get(name=did)
    return render(request,"load_calculation.html",{"obj":obj})

def bank(request):
    emp=CreateEmployeeGrp.objects.all()
    if request.method=='POST':
        accno=request.POST['accno']
        ifsc_Code=request.POST['ifsc_Code']
        bank_name=request.POST['bank_name']
        branch=request.POST['branch']
        crt=bank_crt(accno=accno,ifsc_Code=ifsc_Code,bank_name=bank_name,branch=branch)
        crt.save
        return redirect('employee_creation')
    return render(request,'bank_details1.html',{'emp':emp})


def payroll(request):
    if request.method=='POST':
        name=request.POST['name']
        allias=request.POST['allias']
        voucher_type=request.POST['voucher_type']
        abbreviation=request.POST['abbreviation']
        activate_voucher=request.POST['activate_voucher']
        voucher_numbering_method=request.POST['voucher_numbering_method']
        effective_dates=request.POST['effective_dates']
        narration_voucher=request.POST['narration_voucher']
        print_voucher=request.POST['print_voucher']
        classs=request.POST['classs']
        crt=payroll_crt(name=name,allias=allias,voucher_type=voucher_type,abbreviation=abbreviation,activate_voucher=activate_voucher,
                        voucher_numbering_method=voucher_numbering_method,effective_dates=effective_dates,
                        narration_voucher=narration_voucher,
                        print_voucher=print_voucher,classs=classs)
        crt.save()
        
        
    return render(request,'payroll_voucher_type.html')


def attendance(request):
    att=attendance_crt.objects.all()
    unit=UnitCrt.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under_name=request.POST['under_name']
        attendance=request.POST['attendance']
        period=request.POST['period']
        units=request.POST['units']
        crt=attendance_crt(name=name,alias=alias,under_name=under_name,attendance=attendance,period=period,units=units)
        crt.save()
    return render(request,'attendance.html',{'att':att,'unit':unit})

def attendance_seconday(request):
    att=attendance_crt.objects.all()
    unit=UnitCrt.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under_name=request.POST['under_name']
        attendance=request.POST['attendance']
        period=request.POST['period']
        units=request.POST['units']
        crt=attendance_crt(name=name,alias=alias,under_name=under_name,attendance=attendance,period=period,units=units)
        crt.save()
    return render(request,'attendance(secondary).html',{'att':att,'unit':unit})

def salary_details(request):
    pay=payhead_crt.objects.all()
    sal=salary_crt.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        date=request.POST['date']
        pay_head_name=request.POST['pay_head_name']
        rate=request.POST['rate']
        pay_head_type=request.POST['pay_head_type']
        calculation_type=request.POST['calculation_type']
        crt=salary_crt(name=name,alias=alias,date=date,pay_head_name=pay_head_name,pay_head_type=pay_head_type,rate=rate,calculation_type=calculation_type)
        crt.save()
    return render(request,'salary_details.html',{'pay':pay,'sal':sal})

def stock_item_allocations(request):
    gd=CreateGodown.objects.all()
    if request.method=="POST":
        allocate=request.POST['allocate']
        for_allocate=request.POST['for_allocate']
        godown=request.POST['godown']
        quantity=request.POST['quantity']
        rate=request.POST['rate']
        per=request.POST['per']
        amount=request.POST['amount']
        crt=allocate_stock(allocate=allocate,for_allocate=for_allocate,godown=godown,
                           quantity=quantity,rate=rate,per=per,amount=amount)
        crt.save()
        return redirect("stock_items")
    return render(request,'allocation_stock_item.html',{'gd':gd})


#......................Ann........................

def salesregister(request):#ann
    credit=Sales.objects.all().annotate(month=TruncMonth('sales_date')).values('month').annotate(total=Sum('total')).order_by('month').values("month", "total")                 # Select the count of the grouping       
    sales=Sales.objects.all()
    print("hai")
    vol=[];
    s= credit[0]
    for s in  credit:
        # truncate_date = datetime(s["month"])
      print(s['total'])
    vol.append(s["total"])
    for x in vol:
      print(x)            
    total1 = sum(sales.values_list('total', flat=True)) 
    return render(request,'salesregister.html',{'sales':sales,'total1':total1,'credit':credit})   

def purchaseregister(request):#ann
    p=Purchase.objects.all()
    credit=Purchase.objects.all().annotate(month=TruncMonth('purchase_date')).values('month').annotate(total=Sum('total')).order_by('month').values("month", "total")                 # Select the count of the grouping       
    total1 = sum(p.values_list('total', flat=True))  
    return render(request,'purchaseregister.html',{'total1':total1,'credit':credit})  

def listofsalesvouchers(request):#ann
    com=Companies.objects.all()
    grp=Group.objects.all()
    return render(request,'listofsalesvouchers.html')  
 
def journalregister(request):#ann
    p=Particular.objects.all()
    s=Journal.objects.all()
    items=Journal.objects.all().annotate(month=TruncMonth('journal_date')).values('month').annotate(journal_count = Count('id')).values('month','journal_count').order_by('month')
    print(items)
    return render(request,'journal_report.html',{'items':items})

def listofsalesvoucher(request,pk):#ann
   # s=Sales.objects.all()
    m=pk
    s= Sales.objects.filter(sales_date__year='2022', 
                     sales_date__month=m)
 
    total1 = sum(s.values_list('total', flat=True))               
       
    if m==1:
            msg1="1-Jan-22  to 31-jan-22"
    elif m==2:
            msg1="1-Feb-22  to 28-feb-22"
    elif m ==3:
            msg1="1-March-22  to 31-March-22"
    elif m ==4:
        
             msg1="1-April-22 to 30-April-22"
    elif m ==5:
             msg1="1-May-22  to 31-May-22"
    elif m ==6:
            msg1="1-June-22 to 31-May-22"
    elif m ==7:
            msg1="1-july-22  to 31-july-22"
    elif m ==8:
             msg1="1-Aug-22  to 31-Aug-22"  
    elif m==9:
            msg1="1-Sep-22  to 30-Sep-22"
    elif m ==10:
             msg1="1-Oct-22 to 30-Oct-22"
    elif m ==11:
            msg1="1-Nov-22 to 31-Nov-22" 
    elif m ==12:
             msg1="1-Dec-22 to 31-Dec-22"     
    else:
        msg1="July 01 to 31" 
    return render(request,'listofsalesvouchers.html',{'sales':s,'msg1':msg1,'total1':total1})  


def listofpurchasevoucher(request,pk):#ann
    m=pk
    p= Purchase.objects.filter(purchase_date__year='2022', 
                     purchase_date__month=m)   
    total1 = sum(p.values_list('total', flat=True))                             
    if m==1:
            msg1="1-Jan-22  to 31-jan-22"
    elif m==2:
            msg1="1-Feb-22  to 28-feb-22"
    elif m ==3:
            msg1="1-March-22  to 31-March-22"
    elif m ==4:
             msg1="1-April-22 to 30-April-22"
    elif m ==5:
             msg1="1-May-22  to 31-May-22"
    elif m ==6:
            msg1="1-June-22 to 31-May-22"
    elif m ==7:
            msg1="1-july-22  to 31-july-22"
    elif m ==8:
             msg1="1-Aug-22  to 31-Aug-22"  
    elif m==9:
            msg1="1-Sep-22  to 30-Sep-22"
    elif m ==10:
             msg1="1-Oct-22 to 30-Oct-22"
    elif m ==11:
            msg1="1-Nov-22 to 31-Nov-22" 
    elif m ==12:
             msg1="1-Dec-22 to 31-Dec-22"      
    else:
        msg1="July 01 to 31"               
    return render(request,'listofpurchasevouchers.html',{'purchase':p,'msg1':msg1,'total1':total1})

def listjournalvouchers(request,pk):#ann 
    m=pk
    j= Journal.objects.filter(journal_date__year='2022', 
                     journal_date__month=m)   
                          
    if m==1:
            msg1="1-Jan-22  to 31-jan-22"
    elif m==2:
            msg1="1-Feb-22  to 28-feb-22"
    elif m ==3:
            msg1="1-March-22  to 31-March-22"
    elif m ==4:
             msg1="1-April-22 to 30-April-22"
    elif m ==5:
             msg1="1-May-22  to 31-May-22"
    elif m ==6:
            msg1="1-June-22 to 31-May-22"
    elif m ==7:
            msg1="1-july-22  to 31-july-22"
    elif m ==8:
             msg1="1-Aug-22  to 31-Aug-22"  
    elif m==9:
            msg1="1-Sep-22  to 30-Sep-22"
    elif m ==10:
             msg1="1-Oct-22 to 30-Oct-22"
    elif m ==11:
            msg1="1-Nov-22 to 31-Nov-22" 
    elif m ==12:
             msg1="1-Dec-22 to 31-Dec-22"      
    else:
        msg1="July 01 to 31"                        
    return render(request,'listjournalvouchers.html',{'journal':j,'msg1':msg1})