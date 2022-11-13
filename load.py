import pm4py
permitLog = pm4py.read_xes('data/original/PermitLog.xes_')
internationalDeclarations = pm4py.read_xes('data/original/InternationalDeclarations.xes_')
domesticDeclarations = pm4py.read_xes('data/original/DomesticDeclarations.xes_')
prepayTravelCost = pm4py.read_xes('data/original/PrepayTravelCost.xes_')
requestForPayment = pm4py.read_xes('data/original/RequestForPayment.xes_')
requestForPaymentDF = pm4py.convert_to_dataframe(requestForPayment)
internationalDeclarationsDF = pm4py.convert_to_dataframe(internationalDeclarations)
domesticDeclarationsDF = pm4py.convert_to_dataframe(domesticDeclarations)
requestForPaymentDF
domesticDeclarationsDF
len(domesticDeclarationsDF)
len(internationalDeclarationsDF)
len(requestForPaymentDF)




