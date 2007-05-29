!
! --- This file was generated automatically by nut_empexp
! --- written by Leonid Petrov ( Leonid.Petrov@lpetrov.net )
! --- File was created at 2006.02.15-16:57:44
! --- It contains nutation expansion of the model heo_08d
! --- Phases, frequencies, accelerations of the arguments as well as amplitudes
! --- of cos and sin components of nutation in longitude and in obliquity
! --- are transformed to the form suitable for computations.
! --- Nutation is considered as a a harmonic variations in polar motion 
! --- Convention: angles of a small rotation are computed as :
! ---             E1 = sum_i {  PMC_i*cos(ARG_i) + PMS_i*sin(ARG_i) }
! ---             E2 = sum_i { -PMC_i*sin(ARG_i) + PMS_i*cos(ARG_i) }
! ---             E3 = 0 
! --- Truncation limit for amplitudes:  1000.00 prad
! --- Units are picoradians for amplitudes 
! --- Frequency range -9.500D-05, -5.000D-05 rad/sec
!
      INTEGER*4   N_NUT_PETB, I_NUT_PETB
      PARAMETER ( N_NUT_PETB = 71 )
      CHARACTER  MODEL_NUT_PETB*40
      REAL*8     PHAS_NUT_PETB(N_NUT_PETB), FREQ_NUT_PETB(N_NUT_PETB),
     .           ACCL_NUT_PETB(N_NUT_PETB)
      REAL*8     PMC_NUT_PETB(N_NUT_PETB),      PMS_NUT_PETB(N_NUT_PETB) 
      REAL*8     EPSILON_0_NUT_PETB
      PARAMETER  ( EPSILON_0_NUT_PETB = 0.4090928041D0 ) ! rad
      PARAMETER  ( MODEL_NUT_PETB = 'heo_08d                                 ' )
      DATA       ( PHAS_NUT_PETB(I_NUT_PETB), FREQ_NUT_PETB(I_NUT_PETB),
     .             ACCL_NUT_PETB(I_NUT_PETB),
     .             PMC_NUT_PETB(I_NUT_PETB), 
     .             PMS_NUT_PETB(I_NUT_PETB), 
     .             I_NUT_PETB=1,10 )         
     .             /                         
     . 4.7725650000D0, -8.089447296823D-05, -1.3484D-23,  & !    1
     .       1412.4D0,        -0.3D0,                     & !
     . 2.5901258000D0, -8.088377600616D-05, -2.0759D-23,  & !    2
     .       2223.0D0,       -17.6D0,                     & !
     . 3.0273748000D0, -7.826596687716D-05,  2.4830D-23,  & !    3
     .       2365.8D0,        -0.5D0,                     & !
     . 0.8449356000D0, -7.825526991509D-05,  1.7555D-23,  & !    4
     .      11296.8D0,       -90.5D0,                     & !
     . 4.9456817000D0, -7.824457295303D-05,  1.0280D-23,  & !    5
     .      17644.5D0,      -137.0D0,                     & !
     . 1.5720735000D0, -7.819956465951D-05, -6.2078D-23,  & !    6
     .       2664.6D0,       -14.0D0,                     & !
     . 4.3518763000D0, -7.785705714459D-05,  1.9681D-23,  & !    7
     .       1137.6D0,        26.0D0,                     & !
     . 2.1694371000D0, -7.784636018253D-05,  1.2405D-23,  & !    8
     .       5783.4D0,       -48.1D0,                     & !
     . 1.0180523000D0, -7.560536989990D-05,  4.1318D-23,  & !    9
     .      -1000.9D0,        21.9D0,                     & !
     . 6.1100686000D0, -7.557105856844D-05, -2.3764D-23,  & !   10
     .      13196.8D0,       -30.5D0                      & !      
     . /
!
      DATA       ( PHAS_NUT_PETB(I_NUT_PETB),
     .             FREQ_NUT_PETB(I_NUT_PETB),
     .             ACCL_NUT_PETB(I_NUT_PETB),
     .             PMC_NUT_PETB(I_NUT_PETB), 
     .             PMS_NUT_PETB(I_NUT_PETB), 
     .             I_NUT_PETB=  11,  20 )    
     .             /                         
     . 3.9276294000D0, -7.556036160638D-05, -3.1039D-23,  & !   11
     .      66902.7D0,      -257.0D0,                     & !
     . 1.7451902000D0, -7.554966464432D-05, -3.8314D-23,  & !   12
     .      -1966.4D0,        12.4D0,                     & !
     . 0.4242469000D0, -7.521785409146D-05,  5.0719D-23,  & !   13
     .       2921.3D0,         7.7D0,                     & !
     . 4.5249930000D0, -7.520715712940D-05,  4.3444D-23,  & !   14
     .      14831.8D0,       -15.8D0,                     & !
     . 2.8193698000D0, -7.351846819899D-05, -1.5870D-24,  & !   15
     .       4555.9D0,         0.1D0,                     & !
     . 0.8579377000D0, -7.334076524787D-05,  1.2425D-23,  & !   16
     .      -2139.4D0,         8.7D0,                     & !
     . 4.9586838000D0, -7.333006828581D-05,  5.1496D-24,  & !   17
     .      -4368.3D0,        30.6D0,                     & !
     . 2.7762446000D0, -7.331937132375D-05, -2.1256D-24,  & !   18
     .     118959.2D0,      -261.1D0,                     & !
     . 1.5850756000D0, -7.328505999229D-05, -6.7208D-23,  & !   19
     .       1317.6D0,        -8.2D0,                     & !
     . 5.6858217000D0, -7.327436303023D-05, -7.4483D-23,  & !   20
     .       4705.0D0,         3.1D0                      & !      
     . /
!
      DATA       ( PHAS_NUT_PETB(I_NUT_PETB),
     .             FREQ_NUT_PETB(I_NUT_PETB),
     .             ACCL_NUT_PETB(I_NUT_PETB),
     .             PMC_NUT_PETB(I_NUT_PETB), 
     .             PMS_NUT_PETB(I_NUT_PETB), 
     .             I_NUT_PETB=  21,  30 )    
     .             /                         
     . 2.2255644000D0, -7.313095239055D-05,  7.8138D-24,  & !   21
     .       2634.8D0,        14.2D0,                     & !
     . 0.0431252000D0, -7.312025542848D-05,  5.3862D-25,  & !   22
     .     159869.3D0,      1218.2D0,                     & !
     . 5.5560474000D0, -7.297686380883D-05,  7.9632D-23,  & !   23
     .      -1414.7D0,        42.6D0,                     & !
     . 4.3648784000D0, -7.294255247737D-05,  1.4550D-23,  & !   24
     .    -417555.0D0,      -120.5D0,                     & !
     . 2.1824392000D0, -7.293185551531D-05,  7.2752D-24,  & !   25
     .   38904910.0D0,      6753.0D0,                     & !
     . 4.1007461000D0, -7.291046159118D-05, -7.2752D-24,  & !   26
     .    5722295.9D0,      -447.1D0,                     & !
     . 1.9183069000D0, -7.289976462912D-05, -1.4550D-23,  & !   27
     .     -17489.7D0,       123.0D0,                     & !
     . 0.7271379000D0, -7.286545329767D-05, -7.9632D-23,  & !   28
     .     -10266.4D0,        64.5D0,                     & !
     . 4.8278840000D0, -7.285475633560D-05, -8.6908D-23,  & !   29
     .       1121.8D0,        23.7D0,                     & !
     . 2.1393140000D0, -7.273275864007D-05,  6.7366D-24,  & !   30
     .       3416.0D0,       -62.8D0                      & !      
     . /
!
      DATA       ( PHAS_NUT_PETB(I_NUT_PETB),
     .             FREQ_NUT_PETB(I_NUT_PETB),
     .             ACCL_NUT_PETB(I_NUT_PETB),
     .             PMC_NUT_PETB(I_NUT_PETB), 
     .             PMS_NUT_PETB(I_NUT_PETB), 
     .             I_NUT_PETB=  31,  40 )    
     .             /                         
     . 6.2400601000D0, -7.272206167801D-05, -5.3862D-25,  & !   31
     .    -124517.4D0,       136.5D0,                     & !
     . 1.3676267000D0, -7.271134569592D-05, -4.6109D-24,  & !   32
     .       1080.4D0,        69.3D0,                     & !
     . 0.5973636000D0, -7.256795407626D-05,  7.4483D-23,  & !   33
     .      -4486.8D0,         0.0D0,                     & !
     . 3.5069407000D0, -7.252294578275D-05,  2.1256D-24,  & !   34
     .    2658993.2D0,     -2481.7D0,                     & !
     . 1.3245015000D0, -7.251224882068D-05, -5.1496D-24,  & !   35
     .     -29076.5D0,       -19.4D0,                     & !
     . 5.4252476000D0, -7.250155185862D-05, -1.2425D-23,  & !   36
     .       2051.8D0,         6.4D0,                     & !
     . 3.4638155000D0, -7.232384890751D-05,  1.5870D-24,  & !   37
     .     104244.7D0,       -79.0D0,                     & !
     . 3.4206903000D0, -7.212475203227D-05,  1.0484D-24,  & !   38
     .       3188.6D0,        -6.1D0,                     & !
     . 3.9406315000D0, -7.064585693916D-05, -3.6169D-23,  & !   39
     .      -3409.2D0,        -2.5D0,                     & !
     . 1.7581923000D0, -7.063515997710D-05, -4.3444D-23,  & !   40
     .     -15418.5D0,        -1.4D0                      & !      
     . /
!
      DATA       ( PHAS_NUT_PETB(I_NUT_PETB),
     .             FREQ_NUT_PETB(I_NUT_PETB),
     .             ACCL_NUT_PETB(I_NUT_PETB),
     .             PMC_NUT_PETB(I_NUT_PETB), 
     .             PMS_NUT_PETB(I_NUT_PETB), 
     .             I_NUT_PETB=  41,  50 )    
     .             /                         
     . 4.5379951000D0, -7.029265246218D-05,  3.8314D-23,  & !   41
     .     -14139.1D0,        14.0D0,                     & !
     . 2.3555559000D0, -7.028195550011D-05,  3.1039D-23,  & !   42
     .     -70175.6D0,        25.3D0,                     & !
     . 0.1731167000D0, -7.027125853805D-05,  2.3764D-23,  & !   43
     .       2016.4D0,         2.0D0,                     & !
     . 5.2651330000D0, -7.023694720660D-05, -4.1318D-23,  & !   44
     .     -24765.4D0,        -5.0D0,                     & !
     . 3.0826938000D0, -7.022625024453D-05, -4.8594D-23,  & !   45
     .      -4584.8D0,        -1.2D0,                     & !
     . 5.8624966000D0, -6.988374272961D-05,  3.3164D-23,  & !   46
     .      -5776.2D0,       -18.9D0,                     & !
     . 3.6800574000D0, -6.987304576755D-05,  2.5889D-23,  & !   47
     .      -1291.5D0,       -21.7D0,                     & !
     . 0.0130021000D0, -6.800665388603D-05, -5.1301D-24,  & !   48
     .       1391.4D0,       -30.6D0,                     & !
     . 4.1137482000D0, -6.799595692396D-05, -1.2405D-23,  & !   49
     .      -6421.6D0,       -18.4D0,                     & !
     . 1.3806287000D0, -6.779684102870D-05, -9.7410D-24,  & !   50
     .       1437.1D0,        12.9D0                      & !      
     . /
!
      DATA       ( PHAS_NUT_PETB(I_NUT_PETB),
     .             FREQ_NUT_PETB(I_NUT_PETB),
     .             ACCL_NUT_PETB(I_NUT_PETB),
     .             PMC_NUT_PETB(I_NUT_PETB), 
     .             PMS_NUT_PETB(I_NUT_PETB), 
     .             I_NUT_PETB=  51,  60 )    
     .             /                         
     . 4.7111118000D0, -6.764275244698D-05,  6.2078D-23,  & !   51
     .      -2945.8D0,       -37.1D0,                     & !
     . 1.3375036000D0, -6.759774415346D-05, -1.0280D-23,  & !   52
     .     456637.2D0,       646.9D0,                     & !
     . 5.4382497000D0, -6.758704719140D-05, -1.7555D-23,  & !   53
     .      85978.3D0,       140.5D0,                     & !
     . 3.2558105000D0, -6.757635022934D-05, -2.4830D-23,  & !   54
     .      -2594.6D0,         9.2D0,                     & !
     . 1.2943784000D0, -6.739864727823D-05, -1.0818D-23,  & !   55
     .      -1512.0D0,        18.0D0,                     & !
     . 1.9348672000D0, -6.724453967648D-05,  6.4203D-23,  & !   56
     .      -1304.9D0,         6.7D0,                     & !
     . 3.0956958000D0, -6.531174557731D-05, -5.3724D-23,  & !   57
     .      11940.7D0,        36.4D0,                     & !
     . 0.9132566000D0, -6.530104861525D-05, -6.0999D-23,  & !   58
     .       2216.4D0,        14.7D0,                     & !
     . 3.6930595000D0, -6.495854110033D-05,  2.0759D-23,  & !   59
     .      60423.2D0,       162.6D0,                     & !
     . 1.5106203000D0, -6.494784413827D-05,  1.3484D-23,  & !   60
     .      11364.0D0,        46.1D0                      & !      
     . /
!
      DATA       ( PHAS_NUT_PETB(I_NUT_PETB),
     .             FREQ_NUT_PETB(I_NUT_PETB),
     .             ACCL_NUT_PETB(I_NUT_PETB),
     .             PMC_NUT_PETB(I_NUT_PETB), 
     .             PMS_NUT_PETB(I_NUT_PETB), 
     .             I_NUT_PETB=  61,  65 )    
     .             /                         
     . 5.4512517000D0, -6.267254252418D-05, -2.2685D-23,  & !   61
     .       7751.7D0,        34.3D0,                     & !
     . 3.2688125000D0, -6.266184556212D-05, -2.9960D-23,  & !   62
     .       1445.7D0,        -2.1D0,                     & !
     . 6.0486154000D0, -6.231933804720D-05,  5.1798D-23,  & !   63
     .       6226.7D0,        35.8D0,                     & !
     . 3.8661762000D0, -6.230864108513D-05,  4.4523D-23,  & !   64
     .       1170.6D0,         4.9D0,                     & !
     . 1.5236223000D0, -6.003333947105D-05,  8.3538D-24,  & !   65
     .       1539.1D0,        17.7D0                      & !
     . /
!
      DATA       ( PHAS_NUT_PETB(I_NUT_PETB),
     .             FREQ_NUT_PETB(I_NUT_PETB),
     .             ACCL_NUT_PETB(I_NUT_PETB),
     .             PMC_NUT_PETB(I_NUT_PETB), 
     .             PMS_NUT_PETB(I_NUT_PETB), 
     .             I_NUT_PETB=  66,  71 )    
     .             /                         
!
!MHB2000:
!     & 0.0862503605D0, -7.331935230383D-05,  1.0772D-24,  & !  763
!     &       1651.7D0,        -3.4D0,                     & !
!     & 2.7331194407D0, -7.312027444785D-05, -2.6643D-24,  & !  890
!     &      -2442.8D0,       -21.3D0,                     & !
!     & 3.5931910467D0, -7.292113953393D-05,  3.2029D-24,  & ! 1310
!     &      -6494.1D0,         0.0D0,                     & !
!     & 0.0293981665D0, -7.292092541121D-05,  1.0628D-24,  & ! 1327
!     &        696.6D0,      1157.0D0,                     & !
!     & 3.5500658664D0, -7.272204265864D-05,  2.6643D-24,  & ! 1716
!     &     -44064.9D0,        42.7D0,                     & !
!     & 6.1969349467D0, -7.252296480266D-05, -1.0772D-24,  & ! 1841
!     &      -1570.2D0,         1.5D0                      & !
!     & /
!
!
!
!
!REN:
     . 0.0862503544D0, -7.331935230372D-05,  1.0772D-24,   & !  619
     .       1511.1D0,         0.0D0,                      & !
     . 2.7331194368D0, -7.312027444851D-05, -2.6643D-24,   & !  722
     .      -1838.6D0,         2.9D0,                      & !
     . 3.5931910475D0, -7.292113953322D-05,  3.2029D-24,   & ! 1105
     .      -6494.0D0,         0.0D0,                      & !
     . 0.0293981700D0, -7.292092541091D-05,  1.0628D-24,   & ! 1121
     .        696.6D0,      1157.0D0,                      & !
     . 3.5500658704D0, -7.272204265798D-05,  2.6643D-24,   & ! 1460
     .     -42936.8D0,         2.9D0,                      & !
     . 6.1969349528D0, -7.252296480277D-05, -1.0772D-24,   & ! 1573
     .      -1528.0D0,         0.0D0                       & !
     . /