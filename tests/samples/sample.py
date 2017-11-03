# coding=utf-8

sample0 = '''
Hepatitis (viral, acute), Type C, Probable previous 52 weeks maximum
Hepatitis (viral, acute), Type C, Probable cummulative for 2017
Hepatitis (viral, acute), Type C, Probable cummulative for 2016

tab delimited data:
UNITED STATES	8	44	134	1,770	2,398	3	18	80	690	830
NEW ENGLAND	-	5	14	179	422	-	1	4	40	110
Conn.	-	0	1	6	16	-	0	0	-	-
Maine	-	0	2	15	17	-	0	1	5	10
Mass.	-	4	14	154	384	-	1	4	35	100
N.H.	-	0	0	-	-	-	0	0	-	-
R.I.	-	0	0	-	-	-	0	0	-	-
etwert
wert
we
w'''


sample1=u'''
TABLE II. (Part 7)  Provisional cases of selected notifiable diseases (>= 1,000 cases reported during the preceding year), and selected* low frequency diseases, United States and U.S. territories, week ending October 21, 2017 (WEEK 42)

column labels in same order that data fields appears in each record below:
Reporting Area
Hepatitis (viral, acute), Type C, Confirmed current week
Hepatitis (viral, acute), Type C, Confirmed previous 52 weeks median
Hepatitis (viral, acute), Type C, Confirmed previous 52 weeks maximum
Hepatitis (viral, acute), Type C, Confirmed cummulative for 2017
Hepatitis (viral, acute), Type C, Confirmed cummulative for 2016
Hepatitis (viral, acute), Type C, Probable current week
Hepatitis (viral, acute), Type C, Probable previous 52 weeks median
Hepatitis (viral, acute), Type C, Probable previous 52 weeks maximum
Hepatitis (viral, acute), Type C, Probable cummulative for 2017
Hepatitis (viral, acute), Type C, Probable cummulative for 2016

tab delimited data:
UNITED STATES	8	44	134	1,770	2,398	3	18	80	690	830
NEW ENGLAND	-	5	14	179	422	-	1	4	40	110
Conn.	-	0	1	6	16	-	0	0	-	-
Maine	-	0	2	15	17	-	0	1	5	10
Mass.	-	4	14	154	384	-	1	4	35	100
N.H.	-	0	0	-	-	-	0	0	-	-
R.I.	-	0	0	-	-	-	0	0	-	-
Vt.	-	0	1	4	5	-	0	0	-	-
MID. ATLANTIC	5	7	19	293	439	2	0	4	35	17
N.J.	-	1	6	56	102	-	0	0	-	-
N.Y. (Upstate)	2	3	9	116	146	1	0	3	16	17
N.Y. City	-	0	3	7	3	-	0	0	-	-
Pa.	3	3	12	114	188	1	0	3	19	-
E.N. CENTRAL	2	9	19	356	460	-	3	10	143	129
Ill.	-	0	3	27	18	-	0	2	9	2
Ind.	-	2	10	105	128	-	1	5	46	27
Mich.	1	2	6	101	84	-	1	4	41	33
Ohio	1	3	7	102	151	-	1	5	47	67
Wis.	-	0	4	21	79	-	0	0	-	-
W.N. CENTRAL	-	2	6	88	88	-	0	2	7	3
Iowa	-	0	0	-	-	-	0	0	-	-
Kans.	-	0	2	12	10	-	0	1	2	1
Minn.	-	1	3	27	39	-	0	1	2	1
Mo.	-	1	3	35	18	-	0	0	-	-
Nebr.	-	0	0	-	2	-	0	1	1	-
N. Dak.	-	0	1	2	1	-	0	1	1	-
S. Dak.	-	0	2	12	18	-	0	1	1	1
S. ATLANTIC	1	10	20	431	504	-	4	11	151	213
Del.	-	0	0	-	-	-	0	0	-	-
D.C.	-	0	0	-	-	-	0	0	-	-
Fla.	-	5	10	239	204	-	1	5	50	48
Ga.	-	1	6	43	77	-	0	4	17	23
Md.	-	0	3	23	32	-	0	2	9	8
N.C.	-	0	4	6	71	-	0	4	10	82
S.C.	-	0	1	2	10	-	0	1	1	1
Va.	1	1	4	45	35	-	0	5	18	21
W. Va.	-	2	6	73	75	-	1	5	46	30
E.S. CENTRAL	-	4	9	155	232	1	5	12	194	254
Ala.	-	0	3	15	29	-	0	4	17	43
Ky.	-	1	8	46	75	-	3	8	118	134
Miss.	-	0	0	-	-	-	0	0	-	-
Tenn.	-	2	7	94	128	1	1	5	59	77
W.S. CENTRAL	-	1	17	37	55	-	0	23	32	37
Ark.	-	0	0	-	-	-	0	0	-	-
La.	-	0	1	2	5	-	0	2	3	11
Okla.	-	0	12	8	17	-	0	23	11	26
Tex.	-	0	5	27	33	-	0	3	18	-
MOUNTAIN	-	2	8	86	132	-	1	4	55	50
Ariz.	-	0	0	-	-	-	0	0	-	-
Colo.	-	0	2	10	28	-	0	2	15	5
Idaho	-	0	1	6	6	-	0	1	5	2
Mont.	-	0	2	11	14	-	0	1	2	-
Nev.	-	0	3	22	11	-	0	1	2	12
N. Mex.	-	0	2	8	16	-	0	2	9	14
Utah	-	1	4	29	57	-	0	2	22	17
Wyo.	-	0	0	-	-	-	0	0	-	-
PACIFIC	-	3	62	145	66	-	1	33	33	17
Alaska	-	0	0	-	-	-	0	0	-	-
Calif.	-	1	6	81	52	-	0	2	17	13
Hawaii	-	0	0	-	-	-	0	0	-	-
Oreg.	-	0	3	28	14	-	0	1	4	4
Wash.	-	0	62	36	-	-	0	33	12	-
Amer. Samoa	-	0	0	-	-	-	0	0	-	-
C.N.M.I.	-	-	-	-	-	-	-	-	-	-
Guam	-	0	0	-	-	-	0	0	-	-
P.R.	-	0	0	-	-	-	0	0	-	-
V.I.	-	0	0	-	-	-	0	0	-	-

C.N.M.I.: Commonwealth of Northern Mariana Islands.
U: Unavailable.
-: No reported cases.
N: Not reportable.
NN: Not Nationally Notifiable
NP: Nationally notifiable but not published.
Cumulative: year-to-date counts.

* Three low incidence conditions, rubella, rubella congenital, and tetanus, are in
Table II to facilitate case count verification with reporting jurisdictions.

 Case counts for reporting year 2017 are provisional and subject to change.
For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf.

Data for tuberculosis are displayed quarterly.

§ Based on the CSTE Position Statement 15-ID-03: Revision of the Case Definition of Hepatitis C for National Notification, acute hepatitis C is now reported by case classification status.

National Notifiable Diseases Surveillance System (NNDSS) at http://wwwn.cdc.gov/nndss/

MMWR web application provided by CDC WONDER; http://wonder.cdc.gov

'''


sample2= u'''
TABLE II. (Part 7)  Provisional cases of selected* notifiable diseases (>= 1,000 cases reported during the preceding year), and selected low frequency diseases, United States and U.S. territories, week ending May 21, 2016 (WEEK 20)

column labels in same order that data fields appears in each record below:
Reporting Area
Invasive Pneumococcal, All Ages Disease current week
Invasive Pneumococcal, All Ages previous 52 weeks median
Invasive Pneumococcal, All Ages previous 52 weeks maximum
Invasive Pneumococcal, All Ages cummulative for 2016
Invasive Pneumococcal, All Ages cummulative for 2015
Invasive Pneumococcal, Age <5 years current week
Invasive Pneumococcal, Age <5 years previous 52 weeks median
Invasive Pneumococcal, Age <5 years previous 52 weeks maximum
Invasive Pneumococcal, Age <5 years cummulative for 2016
Invasive Pneumococcal, Age <5 years cummulative for 2015
Legionellosis current week
Legionellosis previous 52 weeks median
Legionellosis previous 52 weeks maximum
Legionellosis cummulative for 2016
Legionellosis cummulative for 2015

tab delimited data:
UNITED STATES	172	292	724	7,259	8,115	8	21	36	432	536	30	98	274	1,022	1,527
NEW ENGLAND	8	20	39	520	564	-	0	4	29	30	-	5	15	44	59
Conn.	2	4	10	105	130	-	0	1	6	4	-	1	4	6	9
Maine	4	3	9	70	68	-	0	2	6	2	-	0	2	6	4
Mass.	-	9	20	240	257	-	0	3	14	15	-	2	8	24	34
N.H.	1	1	6	45	51	-	0	1	1	5	-	0	5	3	3
R.I.	-	1	6	28	25	-	0	1	1	1	-	0	6	3	6
Vt.	1	1	5	32	33	-	0	1	1	3	-	0	3	2	3
MID. ATLANTIC	44	45	129	1,022	1,256	1	3	8	43	53	5	19	127	215	289
N.J.	-	5	20	2	285	-	0	4	-	7	-	2	13	2	50
N.Y. (Upstate)	24	17	71	426	385	1	1	4	22	20	2	6	26	93	108
N.Y. City	16	13	23	318	340	-	0	3	9	16	1	5	85	74	67
Pa.	4	10	23	276	246	-	0	3	12	10	2	6	23	46	64
E.N. CENTRAL	27	55	127	1,378	1,390	-	3	9	66	74	7	18	103	187	242
Ill.	N	0	0	N	N	-	0	2	-	1	-	4	48	43	47
Ind.	-	11	30	261	302	-	0	3	5	18	-	2	12	21	29
Mich.	-	14	46	343	375	-	1	4	17	22	-	2	14	17	39
Ohio	18	20	41	552	506	-	1	5	31	23	7	6	74	95	103
Wis.	9	8	25	222	207	-	1	2	13	10	-	2	7	11	24
W.N. CENTRAL	5	15	29	279	508	-	1	4	15	47	-	4	25	45	62
Iowa	N	0	0	N	N	N	0	0	N	N	-	0	3	4	11
Kans.	-	4	9	90	88	-	0	2	6	11	-	0	4	5	7
Minn.	-	5	19	-	258	-	0	2	-	20	-	1	5	12	9
Mo.	N	0	1	N	N	-	0	2	-	9	-	2	22	22	25
Nebr.	3	3	8	86	71	-	0	2	8	4	-	0	2	1	7
N. Dak.	-	1	6	32	37	-	0	1	1	3	-	0	1	1	1
S. Dak.	2	2	9	71	54	N	0	0	N	N	-	0	2	-	2
S. ATLANTIC	28	51	109	1,321	1,376	1	4	11	91	102	9	18	36	237	314
Del.	2	1	5	34	40	-	0	1	-	2	-	0	3	5	5
D.C.	N	0	0	N	N	-	0	1	-	4	N	0	0	N	N
Fla.	8	9	59	351	211	-	1	4	26	28	2	5	13	90	112
Ga.	12	17	36	438	527	1	1	5	32	29	1	2	7	34	32
Md.	5	8	20	225	226	-	0	3	15	12	2	2	9	29	38
N.C.	N	0	0	N	N	N	0	0	N	N	-	3	9	41	64
S.C.	1	6	18	180	250	-	0	2	4	12	1	1	3	10	21
Va.	-	0	2	10	8	-	0	2	10	8	3	2	9	25	31
W. Va.	-	4	12	83	114	-	0	2	4	7	-	0	3	3	11
E.S. CENTRAL	17	30	70	784	837	3	2	6	41	52	1	5	15	72	110
Ala.	1	5	18	157	151	1	0	5	13	17	-	1	4	19	26
Ky.	-	4	11	111	119	-	0	2	1	2	-	1	7	16	23
Miss.	1	5	12	113	108	1	0	2	9	9	-	0	4	4	17
Tenn.	15	15	35	403	459	1	1	3	18	24	1	2	6	33	44
W.S. CENTRAL	21	39	244	1,069	1,084	1	4	16	90	95	5	7	22	59	118
Ark.	-	5	24	119	153	-	0	3	10	14	-	1	4	8	8
La.	1	5	16	161	182	-	0	3	14	11	-	0	3	6	20
Okla.	N	0	0	N	N	-	0	2	5	7	-	0	9	1	6
Tex.	20	27	217	789	749	1	3	14	61	63	5	5	21	44	84
MOUNTAIN	20	30	65	799	1,025	1	2	6	53	77	3	4	10	51	97
Ariz.	13	9	37	443	390	1	1	4	28	28	3	1	5	29	45
Colo.	-	4	21	-	237	-	0	2	-	16	-	0	7	-	18
Idaho	N	0	0	N	N	-	0	1	4	4	-	0	1	7	6
Mont.	6	1	5	49	33	-	0	1	2	-	-	0	2	2	1
Nev.	-	2	10	40	87	-	0	1	2	7	-	0	2	-	10
N. Mex.	1	5	15	170	162	-	0	4	7	12	-	0	2	4	4
Utah	-	3	8	78	101	-	0	2	9	9	-	0	2	9	13
Wyo.	-	0	3	19	15	-	0	1	1	1	-	0	2	-	-
PACIFIC	2	3	11	87	75	1	0	1	4	6	-	7	69	112	236
Alaska	2	2	10	50	44	1	0	1	4	4	-	0	0	-	-
Calif.	N	0	0	N	N	N	0	0	N	N	-	6	18	90	214
Hawaii	-	1	6	37	31	-	0	1	-	2	-	0	1	2	5
Oreg.	N	0	0	N	N	N	0	0	N	N	-	1	3	7	17
Wash.	N	0	0	N	N	N	0	0	N	N	-	0	56	13	-
Amer. Samoa	N	0	0	N	N	-	0	0	-	-	N	0	0	N	N
C.N.M.I.	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-
Guam	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-
P.R.	-	0	0	-	-	-	0	0	-	-	-	0	2	3	6
V.I.	-	0	0	-	-	-	0	0	-	-	-	0	0	-	-

C.N.M.I.: Commonwealth of Northern Mariana Islands.
U: Unavailable.
-: No reported cases.
N: Not reportable.
NN: Not Nationally Notifiable
NP: Nationally notifiable but not published.
Cum: Cumulative year-to-date counts.
Med: Median.
Max: Maximum.

* Three low incidence conditions, rubella, rubella congenital, and tetanus, are in
Table II to facilitate case count verification with reporting jurisdictions.

 Case counts for reporting years 2015 and 2016 are provisional and subject to change.
For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf.
Data for TB are displayed in Table IV, which appears quarterly.

 Includes drug resistant and susceptible cases of Invasive Pneumococcal Disease. This condition was
previously named Streptococcus pneumoniae invasive disease and cases were reported to CDC using different event
codes to specify whether the cases were drug resistant or in a defined age group, such as <5 Years.




National Notifiable Diseases Surveillance System (NNDSS) at http://wwwn.cdc.gov/nndss/


MMWR web application provided by CDC WONDER; http://wonder.cdc.gov


'''



sample3= u'''
TABLE II. (Part 7)  Provisional cases of selected* notifiable diseases (>= 1,000 cases reported during the preceding year), and selected low frequency diseases, United States and U.S. territories, week ending May 21, 2016 (WEEK 20)

column labels in same order that data fields appears in each record below:
Reporting Area
Invasive Pneumococcal, All Ages Disease current week
Invasive Pneumococcal, All Ages previous 52 weeks median
Invasive Pneumococcal, All Ages previous 52 weeks maximum
Invasive Pneumococcal, All Ages cummulative for 2016
Invasive Pneumococcal, All Ages cummulative for 2015
Invasive Pneumococcal, Age <5 years current week
Invasive Pneumococcal, Age <5 years previous 52 weeks median
Invasive Pneumococcal, Age <5 years previous 52 weeks maximum
Invasive Pneumococcal, Age <5 years cummulative for 2016
Invasive Pneumococcal, Age <5 years cummulative for 2015
Legionellosis current week
Legionellosis previous 52 weeks median
Legionellosis previous 52 weeks maximum
Legionellosis cummulative for 2016
Legionellosis cummulative for 2015

tab delimited data:
No records found

'''