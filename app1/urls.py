from django.urls import path
from.import views


urlpatterns = [

    path('base',views.base,name='base'),

#.........................jisha..........................
    

    path('ledgers/<int:pk>',views.ledgers,name='ledgers'),

    path('vouchers/<int:pk>',views.vouchers,name='vouchers'),

    path('groups',views.groups,name='groups'),

    path('group_alt',views.group_alt,name='group_alt'),

    path('cost_alt',views.cost_alt,name='cost_alt'),

    path('currency/<int:pk>',views.currency,name='currency'),

    path('c_create/<int:pk>',views.c_create,name='c_create'),

    path('c_alter/<int:pk>',views.c_alter,name='c_alter'),

    path('cost/<int:pk>',views.cost,name='cost'),
    
    path('rates/<int:pk>',views.rates,name='rates'),

    path('change_company',views.change_company,name='change_company'),

    path('company_list',views.company_list,name='company_list'),

    path('select_c',views.select_c,name='select_c'),

    path('create_cmpny',views.create_cmpny,name='create_cmpny'),
    
    path('features',views.features,name='features'),

    path('tally_gst/<int:pk>',views.tally_gst,name='tally_gst'),

    path('create_gst/<int:pk>',views.create_gst,name='create_gst'),

    path('gst_tax/<int:pk>',views.gst_tax,name='gst_tax'),

    path('lut_bond',views.lut_bond,name='lut_bond'),

    path('create_gsttax/<int:pk>',views.create_gsttax,name='create_gsttax'),

    path('create_lutbond',views.create_lutbond,name='create_lutbond'),

    path('tds/<int:pk>',views.tds,name='tds'),

    path('create_tds/<int:pk>',views.create_tds,name='create_tds'),

    path('person_tds/<int:pk>',views.person_tds,name='person_tds'),

    path('person/<int:pk>',views.person,name='person'),

    path('bank_details',views.bank_details,name='bank_details'),

    path('bankname',views.bankname,name='bankname'),

    path('shut_cmpny',views.shut_cmpny,name='shut_cmpny'),

    path('shut/<int:pk>',views.shut,name='shut'),

    path('enable/<int:pk>',views.enable,name='enable'),

    path('c_rates',views.c_rates,name='c_rates'),

    path('b_name',views.b_name,name='b_name'),

    path('cheque',views.cheque,name='cheque'),

    path('ledger_gst',views.ledger_gst,name='ledger_gst'),

    path('vouch_advance/<int:pk>',views.vouch_advance,name='vouch_advance'),

    path('ledger_chequed',views.ledger_chequed,name='ledger_chequed'),

    path('create_group',views.create_group,name='create_group'),

    path('create_currency/<int:pk>',views.create_currency,name='create_currency'),

    path('alter_currency/<int:pk>',views.alter_currency,name='alter_currency'),

    path('load_centre',views.load_centre,name='load_centre'),

    path('ledger_taxgst',views.ledger_taxgst,name='ledger_taxgst'),

    path('create_voucher/<int:pk>',views.create_voucher,name='create_voucher'),

    path('create_ROE/<int:pk>',views.create_ROE,name='create_ROE'),

    path('create_ledger/<int:pk>',views.create_ledger,name='create_ledger'),

    path('create_ledgerdimension',views.create_ledgerdimension,name='create_ledgerdimension'),

    path('company_create',views.company_create,name='company_create'),

    path('company_feature/<int:cf>',views.company_feature,name='company_feature'),

    path('create_bankdetails/<int:pk>',views.create_bankdetails,name='create_bankdetails'),

    path('create_chequebk/<int:pk>',views.create_chequebk,name='create_chequebk'),

    path('create_ledger_gst/<int:pk>',views.create_ledger_gst,name='create_ledger_gst'),

    path('create_voucher_advance/<int:pk>',views.create_voucher_advance,name='create_voucher_advance'),

    path('create_ledger_taxgst/<int:pk>',views.create_ledger_taxgst,name='create_ledger_taxgst'),

#.........................Ajmy..........................

    path('index',views.index,name='index'),
    path('group',views.group,name='group'),
    path('branch',views.branch,name='branch'),
    path('ledger',views.ledger,name='ledger'),
    path('primary',views.primary,name='primary'),
    path('costcat',views.costcat,name='costcat'),
    # path('costcentr',views.costcentr,name='costcentr'),
    path('voucher',views.voucher,name='voucher'),
    path('vouchpage',views.vouchpage,name='vouchpage'),

    path('catgroupsummary',views.catgroupsummary,name='catgroupsummary'),
    path('groupsummarypage',views.groupsummarypage,name='groupsummarypage'),
    path('creategroups',views.creategroups,name='creategroups'),
    path('primarygrpsummary/<int:sk>',views.primarygrpsummary,name='primarygrpsummary'),
    path('secondarygrpsummary/<int:sk>',views.secondarygrpsummary,name='secondarygrpsummary'),
    path('productsummary/<int:sk>',views.productsummary,name='productsummary'),
    path('prdctmonthlysummary/<int:sk>',views.prdctmonthlysummary,name='prdctmonthlysummary'),
    path('vouchsummary/<int:sk>/<int:m>/<int:n>',views.vouchsummary,name='vouchsummary'),
    path('periodvouchsummary/<int:sk>/<int:m>/<int:n>',views.periodvouchsummary,name='periodvouchsummary'),
    
    path('categorysummary',views.categorysummary,name='categorysummary'),
    path('createcategory',views.createcategory,name='createcategory'),
    path('primarycatsummary/<int:sk>',views.primarycatsummary,name='primarycatsummary'),
    path('secondarycatsummary/<int:sk>',views.secondarycatsummary,name='secondarycatsummary'),
    path('prcatsummary/<int:sk>',views.prcatsummary,name='prcatsummary'),
    path('productcatmonthlysummary/<int:sk>',views.productcatmonthlysummary,name='productcatmonthlysummary'),

    path('savestockgroup',views.savestockgroup,name='savestockgroup'),
    path('savestockcategory',views.savestockcategory,name='savestockcategory'),


#......................Praveen........................

    path('list_of_groups',views.list_of_groups,name='list_of_groups'),
    path('load_create_groups/<int:pk>',views.load_create_groups,name='load_create_groups'),

    path('load_alter_groups',views.load_alter_groups,name="load_alter_groups"),
    # path('branch',views.branch,name='branch'),
    # path('ledger',views.ledger,name='ledger'),
    path('list_of_ledger',views.list_of_ledger,name='list_of_ledger'),
    path('load_ledger_alter/<int:pk>',views.load_ledger_alter,name='load_ledger_alter'),

    path('ledger_gst_details',views.ledger_gst_details,name='ledger_gst_details'),
    path('load_create_ledger',views.load_create_ledger,name='load_create_ledger'),
    path('ledger_chequebook',views.ledger_chequebook,name='ledger_chequebook'),
    path('ledger_bank_details',views.ledger_bank_details,name='ledger_bank_details'),
    path('ledger_cheque_dimenssion',views.ledger_cheque_dimenssion,name='ledger_cheque_dimenssion'),

    path('load_create_ledger2',views.load_create_ledger2,name='load_create_ledger2'),
    path('list_of_currency',views.list_of_currency,name='list_of_currency'),
    path('load_currency',views.load_currency,name='load_currency'),
    path('list_of_companies',views.list_of_companies,name='list_of_companies'),
    path('create_company',views.create_company,name='create_company'),
    path('company_feature_form/<int:pk>',views.company_feature_form,name='company_feature_form'),
    path('companies_feature',views.companies_feature,name='companies_feature'),
    path('companyCreate1',views.companyCreate1,name='companyCreate1'),
    path('create_company',views.create_company,name='create_company'),
    path('select_company1',views.select_company1,name='select_company1'),
    path('shut_company1',views.shut_company1,name='shut_company1'),
    path('shut2/<int:pk>',views.shut2,name="shut2"),
    path('enable2/<int:pk>',views.enable2,name="enable2"),
    # path('shut_card',views.shut_card,name='shut_card'),

    path('load_rates_of_exchange',views.load_rates_of_exchange,name='load_rates_of_exchange'),
    path('create_currency3',views.create_currency3,name='create_currency3'),
    path('load_alter_currency',views.load_alter_currency,name='load_alter_currency'),
    path('currency_alteraion/<int:pk>',views.currency_alteraion,name='currency_alteraion'),

    path('gst_details3/<int:pk>',views.gst_details3,name='gst_details3'),
    path('gst_details_of_company',views.gst_details_of_company,name='gst_details_of_company'),
    path('lutbond/<int:pk>',views.lutbond,name='lutbond'),


    path('tds_detuctor/<int:pk>',views.tds_detuctor,name='tds_detuctor'),
    path('tds_personal/<int:pk>',views.tds_personal,name='tds_personal'),

    # path('primary',views.primary,name='primary'),
    # path('costcat',views.costcat,name='costcat'),
    # path('costcentr',views.costcentr,name='costcentr'),
    # path('voucher',views.voucher,name='voucher'),
    path('list_of_voucher_type',views.list_of_voucher_type,name='list_of_voucher_type'),
    path('load_voucher_type/<int:pk>',views.load_voucher_type,name='load_voucher_type'),
    path('voucher_type_alteration_secondary',views.voucher_type_alteration_secondary,name='voucher_type_alteration_secondary'),
    path('load_create_voucher',views.load_create_voucher,name='load_create_voucher'),
    # path('vouchpage',views.vouchpage,name='vouchpage'),

    path('list_of_cost_centers',views.list_of_cost_centers,name='list_of_cost_centers'),
    path('load_cost_centers/<int:pk>',views.load_cost_centers,name="load_cost_centers"),
    path('alter_cost_create',views.alter_cost_create,name="alter_cost_create"),


#......................Riya........................

    path('',views.index1,name='index1'),
    # path('basepage',views.basepage,name='basepage'),
    path('company',views.company,name='company'),
    path('createcompany',views.createcompany,name='createcompany'),
    path('companycreate',views.companycreate,name='companycreate'),
    path('group1/<int:pk>',views.group1,name='group1'),
    path('costcentre/<int:pk>',views.costcentre,name='costcentre'),
    path('costcentre2/<int:pk>',views.costcentre2,name='costcentre2'),
    path('group2/<int:pk>',views.group2,name='group2'),
    path('currency1/<int:pk>',views.currency1,name='currency1'),
    path('features1/<int:pk>',views.features1,name='features1'),
    path('creategroup/<int:pk>',views.creategroup,name='creategroup'),
    path('altercompanyview',views.altercompanyview,name='altercompanyview'),
    path('selectcompany',views.selectcompany,name='selectcompany'),
    path('shutcompany',views.shutcompany,name='shutcompany'),
    path('addstate',views.addstate,name='addstate'),
    path('addstatenew',views.addstatenew,name='addstatenew'),
    path('addcountry',views.addcountry,name='addcountry'),
    path('altercompany/<int:pk>',views.altercompany,name='altercompany'),
    path('ratesofexchange/<int:pk>',views.ratesofexchange,name='ratesofexchange'),
    path('featurecompany/<int:pk>',views.featurecompany,name='featurecompany'),
    path('disable/<int:pk>',views.disable,name='disable'),
    path('enable/<int:pk>',views.enable,name='enable'),
    path('featurepage',views.featurepage,name='featurepage'),


#......................Neethu........................

    path('create',views.create,name="create"),
    path('companycreate1',views.companycreate1,name="companycreate1"),
    path('gst_details/<int:pk>',views.gst_details,name="gst_details"),
    path('add_gstdetails/<int:pk>',views.add_gstdetails,name="add_gstdetails"),
    path('tds_deductor/<int:pk>',views.tds_deductor,name="tds_deductor"),
    path('person_details/<int:pk>',views.person_details,name="person_details"),
    path('add_person/<int:pk>',views.add_person,name="add_person"),
    path('add_tds/<int:pk>',views.add_tds,name="add_tds"),
    path('features2/<int:pk>',views.features2,name="features2"),
    path('edit_features/<int:pk>',views.edit_features,name="edit_features"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('company_list1',views.company_list1,name="company_list1"),
    path('select_company',views.select_company,name="select_company"),
    path('dash_board/<int:pk>',views.dash_board,name="dash_board"),
    path('alter_company',views.alter_company,name="alter_company"),
    path('edit_page/<int:pk>',views.edit_page,name="edit_page"),
    path('edit_companydetails/<int:pk>',views.edit_companydetails,name="edit_companydetails"),
    path('change_company1',views.change_company1,name="change_company1"),
    path('shut_company',views.shut_company,name="shut_company"),
    
    path('shut1/<int:pk>',views.shut1,name="shut1"),
    path('date_change',views.date_change,name="date_change"),
    path('print_config',views.print_config,name="print_config"),
    path('add_country',views.add_country,name="add_country"),
   
    path('addstates',views.addstates,name="addstates"),
    path('state_country',views.state_country,name="state_country"),
    path('load_cities',views.load_cities,name="load_cities"),
    path('edit_gst_details/<int:pk>',views.edit_gst_details,name="edit_gst_details"),
    path('add_newgstdetails/<int:pk>',views.add_newgstdetails,name="add_newgstdetails"),
    path('edit_tds_deductor/<int:pk>',views.edit_tds_deductor,name="edit_tds_deductor"),
    path('add_newtdsdetails/<int:pk>',views.add_newtdsdetails,name="add_newtdsdetails"),
    path('edit_person_details/<int:pk>',views.edit_person_details,name="edit_person_details"),
    path('add_newpersondetails/<int:pk>',views.add_newpersondetails,name="add_newpersondetails"),


#......................Rafi........................

    path('attendance',views.attendance,name='attendance'),
    path('attendance_seconday',views.attendance_seconday,name='attendance_seconday'),
    
    path('stock_group',views.stock_group,name='stock_group'),
    path('stock_group_secondary',views.stock_group_secondary,name='stock_group_secondary'),
    
    path('stock_category_creation',views.stock_category_creation,name='stock_category_creation'),
    path('stock_category_secondary',views.stock_category_secondary,name='stock_category_secondary'),
    
    path('stock_items',views.stock_items,name='stock_items'),
    path('stock_item_allocations',views.stock_item_allocations,name='stock_item_allocations'),
    
    path('unit_creation',views.unit_creation,name='unit_creation'),
    path('uqc',views.uqc,name='uqc'),
    path('unit_creation_secondary',views.unit_creation_secondary,name='unit_creation_secondary'),
    path('uqc_secondary',views.uqc_secondary,name='uqc_secondary'),
    

    path('price_levels',views.price_levels,name='price_levels'),
    
    path('godown_alteration',views.godown_alteration,name='godown_alteration'),
    path('godown_secondary',views.godown_secondary,name='godown_secondary'),
    
    path('employee_creation',views.employee_creation,name='employee_creation'),
    
    path('employee_group_creation',views.employee_group_creation,name='employee_group_creation'),
    path('emloyee_group_secondary',views.emloyee_group_secondary,name='emloyee_group_secondary'), 

    path('pan_cin',views.pan_cin,name='pan_cin'),
    path('pay_head',views.pay_head,name='pay_head'),
    
    path('salary_details',views.salary_details,name='salary_details'),
    
    path('payroll',views.payroll,name='payroll'),
    
    path('load/',views.load,name="load"),
    path('load_calculation/',views.load_calculation,name='load_calculation'),
    
    path('bank',views.bank,name='bank'),
    
    path('stock_item_allocations',views.stock_item_allocations,name='stock_item_allocations'),

#......................Ann........................

    path('disp_more_reports',views.disp_more_reports,name='disp_more_reports'),#ann
    path('listofpurchasevoucher/<int:pk>',views.listofpurchasevoucher,name='listofpurchasevoucher'),#ann,#listofpurchasevouchers
    path('listjournalvouchers/<int:pk>',views.listjournalvouchers,name='listjournalvouchers'),#ann,#listofjournalvouchers
    path('salesregister',views.salesregister,name='salesregister'),#ann
    path('purchaseregister',views.purchaseregister,name='purchaseregister'),#ann
    path('journalregister',views.journalregister,name='journalregister'),#ann
    path('listofsalesvoucher/<int:pk>',views.listofsalesvoucher,name='listofsalesvoucher'),#ann

#......................Niyas........................

    path('liststockviews',views.liststockviews,name='liststockviews'),
    path('liststockgroupviews',views.liststockgroupviews,name='liststockgroupviews'),
    # path('singlestockgroupanalysisview',views.singlestockgroupanalysisview,name='singlestockgroupanalysisview'),
    
    # path('querystockview',views.querystockview,name='querystockview'),

    # path('salevoucheranalysisview',views.salevoucheranalysisview,name='salevoucheranalysisview'),
    # path('purchasevoucheranalysisview',views.purchasevoucheranalysisview,name='purchasevoucheranalysisview'),
    path('itemmovementanalysisview',views.itemmovementanalysisview,name='itemmovementanalysisview'),
    path('stockgroupanalysisview',views.stockgroupanalysisview,name='stockgroupanalysisview'),
    # path('stockgroupcreateview',views.stockgroupcreateview,name='stockgroupcreateview'),
    path('stockitmecreateview',views.stockitmecreateview,name='stockitmecreateview'),

#......................Jerin........................

    path('savestockgroup1',views.savestockgroup1,name='savestockgroup1'),
    path('savestockitem',views.savestockitem,name='savestockitem'),

    path('querystockview/<int:pk>',views.querystockview,name='querystockview'),
    path('singlestockgroupanalysisview/<int:pk>',views.singlestockgroupanalysisview,name='singlestockgroupanalysisview'),
    path('purchasevoucheranalysisview/<int:pk>',views.purchasevoucheranalysisview,name='purchasevoucheranalysisview'),
    path('salevoucheranalysisview/<int:pk>',views.salevoucheranalysisview,name='salevoucheranalysisview'),
    # path('itemmovementanalysisview/<int:pk>',views.itemmovementanalysisview,name='itemmovementanalysisview'),


    path('receivabl',views.receivabl,name='receivabl'),
    path('payabl',views.payabl,name='payabl'),
    path('creategroup',views.creategroup,name='creategroup'),
    path('create_group',views.create_group,name='create_group'),
    path('grcreate',views.grcreate,name='grcreate'),
    path('createledger',views.createledger,name='createledger'),
    path('credit',views.credit,name='credit'),
    path('debi',views.debi,name='debi'),
    path('ledgercreations',views.ledgercreations,name='ledgercreations'),
    path('ledgerlist',views.ledgerlist,name='ledgerlist'),
    path('nw',views.nw,name='nw')



]