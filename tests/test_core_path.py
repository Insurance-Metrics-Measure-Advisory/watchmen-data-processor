from watchmen.pipeline.service.pipeline_data_extracter import extract_topic_relationship_from_pipeline
from watchmen.pipeline.single.pipeline_service import run_pipeline
from watchmen.pipeline.storage.pipeline_storage import load_pipeline_by_topic_id
from watchmen.topic.storage.topic_data_storage import save_topic_instance
from watchmen.topic.storage.topic_schema_storage import get_topic


def test_save_topic_instance():
    data = {"AdjustedPremium": 0, "AgentCode": "SC001", "BeforeVatPremium": 0, "BusinessCateCode": "1", "BusinessObjectId": 373361609, "Commission": 0, "DuePremium": 0, "EffectiveDate": "2020-04-15", "ExpiryDate": "2021-04-14T23:59:59", "GrossPremium": 0, "IsPremiumCalcSuccess": "Y", "IsRenewable": "Y", "IsTakeUpPolicy": "N", "IssueDate": "2020-04-15T14:48:41", "POIRate": 1, "PolicyCommissionRateList": [{"BusinessObjectId": 316589, "PolicyElementId": 856373402, "PolicyId": 856373401, "PolicyStatus": 2, "Rate": 0.1, "SequenceNumber": 1}], "PolicyCustomerList": [{"Address": "1", "BusinessObjectId": 1000000290, "City": "107", "ConsentData": "", "ConsentEmail": "", "CustomerName": "sam1010", "CustomerType": "Individual", "DateOfBirth": "2001-04-01", "Email": "11@11.com", "Gender": 1, "IdNo": "sam1010", "IdType": "1", "IsInsured": "N", "IsOrgParty": "N", "IsPep": "", "IsPolicyHolder": "Y", "Mobile": "11", "PolicyElementId": 856373403, "PolicyId": 856373401, "PolicyStatus": 2, "PostCode": "1", "SequenceNumber": 1, "State": "15"}], "PolicyElementId": 856373401, "PolicyId": 856373401, "PolicyLobList": [{"AdjustedPremium": 0, "BeforeVatPremium": 0, "BusinessObjectId": 373361615, "Commission": 0, "DuePremium": 0, "GrossPremium": 0, "InsuredCount": 1, "PolicyElementId": 856373404, "PolicyId": 856373401, "PolicyRiskList": [{"AdjustedPremium": 0, "Age": 19, "AgeInDays": 6954, "AgeLevel": 0, "BeforeVatPremium": 0, "BusinessObjectId": 373361627, "Commission": 0, "DateOfBirth": "2001-04-01", "DuePremium": 0, "GenderCode": "1", "GrossPremium": 0, "HasSocialInsurance": "Y", "IdNo": "sam1010", "IdType": "1", "InsuredName": "sam1010", "OccupationCode": "0001001", "PolicyCoverageList": [{"AgeLevelRatio": 1, "AgeRatio": 0.5, "AgeRatioTable": "AgeRatioByRange", "BaseRate": 0.5, "BeforeVatPremium": 0, "BusinessObjectId": 373361631, "GenderRatio": 1, "GrossPremium": 0, "IsCopyLimitDedFromModelToDyna": "Y", "IsFinalLevelCt": "Y", "POIRate": 1, "PolicyElementId": 856373406, "PolicyId": 856373401, "PolicyStatus": 2, "ProductElementCode": "MTN", "ProductElementId": 373362664, "SequenceNumber": 1, "ShortRatio": 0.001, "ShortRatioTable": "ShortPeriodRatioByRange", "SumInsured": 0}], "PolicyElementId": 856373405, "PolicyHolderInsuredRelaCode": "1", "PolicyId": 856373401, "PolicyStatus": 2, "ProductElementCode": "R10007", "ProductElementId": 373362658, "SequenceNumber": 1, "SumInsured": 0, "Vat": 0}], "PolicyStatus": 2, "ProductCode": "FHI001", "ProductElementCode": "FHI001", "ProductElementId": 373362648, "ProductId": 373362647, "ProductLobId": 373362648, "SequenceNumber": 1, "SumInsured": 0, "TechProductCode": "HL_TECH", "TechProductId": 373273834, "Vat": 0}], "PolicyNo": "POFHI00100000001", "PolicyPaymentInfoList": [{"BusinessObjectId": 520259, "ExpiryDate": "2021-04-14T23:59:59", "InstallmentList": [{"BeforeVatPremium": 0, "BeforeVatPremiumLocal": 0, "BusinessObjectId": 200001394, "Commission": 0, "CommissionLocal": 0, "DuePremium": 0, "FeeSeq": 1, "InstallmentAmount": 0, "InstallmentAmountLocal": 0, "InstallmentDate": "2020-04-15", "InstallmentPeriodSeq": 1, "PolicyElementId": 856373408, "PolicyId": 856373401, "PolicyStatus": 2, "PremiumInterest": 0, "PremiumInterestLocal": 0, "SequenceNumber": 1, "TaxInterest": 0, "TaxInterestLocal": 0, "TotalInterest": 0, "TotalInterestLocal": 0, "Vat": 0, "VatLocal": 0}, {"BeforeVatPremium": 0, "BeforeVatPremiumLocal": 0, "BusinessObjectId": 200001394, "Commission": 0, "CommissionLocal": 0, "DuePremium": 0, "FeeSeq": 1, "InstallmentAmount": 0, "InstallmentAmountLocal": 0, "InstallmentDate": "2020-05-15", "InstallmentPeriodSeq": 2, "PolicyElementId": 856373409, "PolicyId": 856373401, "PolicyStatus": 2, "PremiumInterest": 0, "PremiumInterestLocal": 0, "SequenceNumber": 2, "TaxInterest": 0, "TaxInterestLocal": 0, "TotalInterest": 0, "TotalInterestLocal": 0, "Vat": 0, "VatLocal": 0}, {"BeforeVatPremium": 0, "BeforeVatPremiumLocal": 0, "BusinessObjectId": 200001394, "Commission": 0, "CommissionLocal": 0, "DuePremium": 0, "FeeSeq": 1, "InstallmentAmount": 0, "InstallmentAmountLocal": 0, "InstallmentDate": "2020-06-15", "InstallmentPeriodSeq": 3, "PolicyElementId": 856373410, "PolicyId": 856373401, "PolicyStatus": 2, "PremiumInterest": 0, "PremiumInterestLocal": 0, "SequenceNumber": 3, "TaxInterest": 0, "TaxInterestLocal": 0, "TotalInterest": 0, "TotalInterestLocal": 0, "Vat": 0, "VatLocal": 0}, {"BeforeVatPremium": 0, "BeforeVatPremiumLocal": 0, "BusinessObjectId": 200001394, "Commission": 0, "CommissionLocal": 0, "DuePremium": 0, "FeeSeq": 1, "InstallmentAmount": 0, "InstallmentAmountLocal": 0, "InstallmentDate": "2020-07-15", "InstallmentPeriodSeq": 4, "PolicyElementId": 856373411, "PolicyId": 856373401, "PolicyStatus": 2, "PremiumInterest": 0, "PremiumInterestLocal": 0, "SequenceNumber": 4, "TaxInterest": 0, "TaxInterestLocal": 0, "TotalInterest": 0, "TotalInterestLocal": 0, "Vat": 0, "VatLocal": 0}, {"BeforeVatPremium": 0, "BeforeVatPremiumLocal": 0, "BusinessObjectId": 200001394, "Commission": 0, "CommissionLocal": 0, "DuePremium": 0, "FeeSeq": 1, "InstallmentAmount": 0, "InstallmentAmountLocal": 0, "InstallmentDate": "2020-08-15", "InstallmentPeriodSeq": 5, "PolicyElementId": 856373412, "PolicyId": 856373401, "PolicyStatus": 2, "PremiumInterest": 0, "PremiumInterestLocal": 0, "SequenceNumber": 5, "TaxInterest": 0, "TaxInterestLocal": 0, "TotalInterest": 0, "TotalInterestLocal": 0, "Vat": 0, "VatLocal": 0}, {"BeforeVatPremium": 0, "BeforeVatPremiumLocal": 0, "BusinessObjectId": 200001394, "Commission": 0, "CommissionLocal": 0, "DuePremium": 0, "FeeSeq": 1, "InstallmentAmount": 0, "InstallmentAmountLocal": 0, "InstallmentDate": "2020-09-15", "InstallmentPeriodSeq": 6, "PolicyElementId": 856373413, "PolicyId": 856373401, "PolicyStatus": 2, "PremiumInterest": 0, "PremiumInterestLocal": 0, "SequenceNumber": 6, "TaxInterest": 0, "TaxInterestLocal": 0, "TotalInterest": 0, "TotalInterestLocal": 0, "Vat": 0, "VatLocal": 0}, {"BeforeVatPremium": 0, "BeforeVatPremiumLocal": 0, "BusinessObjectId": 200001394, "Commission": 0, "CommissionLocal": 0, "DuePremium": 0, "FeeSeq": 1, "InstallmentAmount": 0, "InstallmentAmountLocal": 0, "InstallmentDate": "2020-10-15", "InstallmentPeriodSeq": 7, "PolicyElementId": 856373414, "PolicyId": 856373401, "PolicyStatus": 2, "PremiumInterest": 0, "PremiumInterestLocal": 0, "SequenceNumber": 7, "TaxInterest": 0, "TaxInterestLocal": 0, "TotalInterest": 0, "TotalInterestLocal": 0, "Vat": 0, "VatLocal": 0}, {"BeforeVatPremium": 0, "BeforeVatPremiumLocal": 0, "BusinessObjectId": 200001394, "Commission": 0, "CommissionLocal": 0, "DuePremium": 0, "FeeSeq": 1, "InstallmentAmount": 0, "InstallmentAmountLocal": 0, "InstallmentDate": "2020-11-15", "InstallmentPeriodSeq": 8, "PolicyElementId": 856373415, "PolicyId": 856373401, "PolicyStatus": 2, "PremiumInterest": 0, "PremiumInterestLocal": 0, "SequenceNumber": 8, "TaxInterest": 0, "TaxInterestLocal": 0, "TotalInterest": 0, "TotalInterestLocal": 0, "Vat": 0, "VatLocal": 0}, {"BeforeVatPremium": 0, "BeforeVatPremiumLocal": 0, "BusinessObjectId": 200001394, "Commission": 0, "CommissionLocal": 0, "DuePremium": 0, "FeeSeq": 1, "InstallmentAmount": 0, "InstallmentAmountLocal": 0, "InstallmentDate": "2020-12-15", "InstallmentPeriodSeq": 9, "PolicyElementId": 856373416, "PolicyId": 856373401, "PolicyStatus": 2, "PremiumInterest": 0, "PremiumInterestLocal": 0, "SequenceNumber": 9, "TaxInterest": 0, "TaxInterestLocal": 0, "TotalInterest": 0, "TotalInterestLocal": 0, "Vat": 0, "VatLocal": 0}, {"BeforeVatPremium": 0, "BeforeVatPremiumLocal": 0, "BusinessObjectId": 200001394, "Commission": 0, "CommissionLocal": 0, "DuePremium": 0, "FeeSeq": 1, "InstallmentAmount": 0, "InstallmentAmountLocal": 0, "InstallmentDate": "2021-01-15", "InstallmentPeriodSeq": 10, "PolicyElementId": 856373417, "PolicyId": 856373401, "PolicyStatus": 2, "PremiumInterest": 0, "PremiumInterestLocal": 0, "SequenceNumber": 10, "TaxInterest": 0, "TaxInterestLocal": 0, "TotalInterest": 0, "TotalInterestLocal": 0, "Vat": 0, "VatLocal": 0}, {"BeforeVatPremium": 0, "BeforeVatPremiumLocal": 0, "BusinessObjectId": 200001394, "Commission": 0, "CommissionLocal": 0, "DuePremium": 0, "FeeSeq": 1, "InstallmentAmount": 0, "InstallmentAmountLocal": 0, "InstallmentDate": "2021-02-15", "InstallmentPeriodSeq": 11, "PolicyElementId": 856373418, "PolicyId": 856373401, "PolicyStatus": 2, "PremiumInterest": 0, "PremiumInterestLocal": 0, "SequenceNumber": 11, "TaxInterest": 0, "TaxInterestLocal": 0, "TotalInterest": 0, "TotalInterestLocal": 0, "Vat": 0, "VatLocal": 0}, {"BeforeVatPremium": 0, "BeforeVatPremiumLocal": 0, "BusinessObjectId": 200001394, "Commission": 0, "CommissionLocal": 0, "DuePremium": 0, "FeeSeq": 1, "InstallmentAmount": 0, "InstallmentAmountLocal": 0, "InstallmentDate": "2021-03-15", "InstallmentPeriodSeq": 12, "PolicyElementId": 856373419, "PolicyId": 856373401, "PolicyStatus": 2, "PremiumInterest": 0, "PremiumInterestLocal": 0, "SequenceNumber": 12, "TaxInterest": 0, "TaxInterestLocal": 0, "TotalInterest": 0, "TotalInterestLocal": 0, "Vat": 0, "VatLocal": 0}], "InstallmentPeriodCount": 12, "InstallmentType": "1", "IsInstallment": "Y", "PayModeCode": "30", "PayRate": 1, "PolicyElementId": 856373407, "PolicyId": 856373401, "PolicyStatus": 2, "SequenceNumber": 1}], "PolicyStatus": 2, "PolicyType": "1", "PremiumCurrencyCode": "CNY", "PremiumInterest": 0, "ProductCode": "FHI001", "ProductId": 373362647, "ProductVersion": "1.0", "ProposalNo": "PFHI0010000000001", "ProposalStatus": "3", "SPEOAUserID": "17312387", "SequenceNumber": 1, "SumInsured": 0, "TaxInterest": 0, "TechProductCode": "HL_TECH", "TechProductId": 373273834, "TotalInterest": 0, "TotalPremium": "0", "Vat": 0}

    # save_topic_instance("raw_gi_policy", data)
    topic = get_topic("raw_gi_policy")
    # # TODO validate data with topic schema
    #
    pipeline_list = load_pipeline_by_topic_id(topic.topicId)

    for pipeline in pipeline_list:
         run_pipeline(pipeline, data)


def test_save_gi_policy():
    data={"duePremium":1000,"orgCode":"AA"}

    topic = get_topic("gi_policy")
    pipeline_list = load_pipeline_by_topic_id(topic.topicId)

    for pipeline in pipeline_list:
         run_pipeline(pipeline, data)


def test_build_pipeline_topic_relation():
    topic = get_topic("raw_gi_policy")
    pipeline_list = load_pipeline_by_topic_id(topic.topicId)
    for pipeline in pipeline_list:
        print(extract_topic_relationship_from_pipeline(pipeline))



