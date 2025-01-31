!=======================================================================
C  MODULE ModuleDefs
C  11/01/2001 CHP Written
C  06/15/2002 CHP Added flood-related data constructs 
C  03/12/2003 CHP Added residue data construct
C  05/08/2003 CHP Added version information
C  09/03/2004 CHP Modified GetPut_Control routine to store entire
C                   CONTROL variable. 
C             CHP Added GETPUT_ISWITCH routine to store ISWITCH.
C             CHP Added TRTNUM to CONTROL variable.
!  06/14/2005 CHP Added FILEX to CONTROL variable.
!  10/24/2005 CHP Put weather variables in constructed variable. 
!             CHP Added PlantStres environmental stress variable
!  11/07/2005 CHP Added KG2PPM conversion variable to SoilType
!  03/03/2006 CHP Tillage variables added to SOILPROP
!                 Added N_ELEMS to CONTROL variable.
!  03/06/2006 CHP Added mulch variable
!  07/13/2006 CHP Add P variables to SwitchType and SoilType TYPES
!  07/14/2006 CHP Added Fertilizer type, Organic Matter Application type
!  07/24/2006 CHP Added mulch/soil albedo (MSALB) and canopy/mulch/soil
!                   albedo (CMSALB) to SOILPROP variable
!  01/12/2007 CHP Changed TRTNO to TRTNUM to avoid conflict with same
!                 variable name (but different meaning) in input module.
!  01/24/2007 CHP Changed GET & PUT routines to more extensible format.
!  01/22/2008 CHP Moved data exchange (GET & PUT routines) to ModuleData
!  04/28/2008 CHP Added option to read CO2 from file 
!  08/08/2008 CHP Use OPSYS to define variables dependant on operating system
!  08/08/2008 CHP Compiler directives for system call library
!  08/21/2008 CHP Add ROTNUM to CONTROL variable
!  11/25/2008 CHP Mauna Loa CO2 is default
!  12/09/2008 CHP Remove METMP
!  11/19/2010 CHP Added "branch" to version to keep track of non-release branches
!  08/08/2017 WP  Version identification moved to CSMVersion.for
!  08/08/2017 WP  Definitions related with OS platform moved to OSDefinitions.for
!=======================================================================

      MODULE ModuleDefs
!     Contains defintion of derived data types and constants which are 
!     used throughout the model.

!=======================================================================
      USE CSMVersion
      USE OSDefinitions
      SAVE
!=======================================================================
!     Global constants
      INTEGER, PARAMETER :: 
     &    NL       = 20,  !Maximum number of soil layers 
     &    TS       = 24,  !Number of hourly time steps per day
     &    NAPPL    = 9000,!Maximum number of applications or operations
     &    NCOHORTS = 300, !Maximum number of cohorts
     &    NELEM    = 3,   !Number of elements modeled (currently N & P)
!            Note: set NELEM to 3 for now so Century arrays will match
     &    NumOfDays = 1000, !Maximum days in sugarcane run (FSR)
     &    NumOfStalks = 42, !Maximum stalks per sugarcane stubble (FSR)
     &    EvaluateNum = 40, !Number of evaluation variables
     &    MaxFiles = 500,   !Maximum number of output files
     &    MaxPest = 500    !Maximum number of pest operations

      REAL, PARAMETER :: 
     &    PI = 3.14159265,
     &    RAD=PI/180.0

      INTEGER, PARAMETER :: 
         !Dynamic variable values
     &    RUNINIT  = 1, 
     &    INIT     = 2,  !Will take the place of RUNINIT & SEASINIT
                         !     (not fully implemented)
     &    SEASINIT = 2, 
     &    RATE     = 3,
     &    EMERG    = 3,  !Used for some plant processes.  
     &    INTEGR   = 4,  
     &    OUTPUT   = 5,  
     &    SEASEND  = 6,
     &    ENDRUN   = 7 

      INTEGER, PARAMETER :: 
         !Nutrient array positions:
     &    N = 1,          !Nitrogen
     &    P = 2,          !Phosphorus
     &    Kel = 3         !Potassium

      CHARACTER(LEN=3)  ModelVerTxt
      CHARACTER(LEN=6)  LIBRARY    !library required for system calls

      CHARACTER*3 MonthTxt(12)
      DATA MonthTxt /'JAN','FEB','MAR','APR','MAY','JUN',
     &               'JUL','AUG','SEP','OCT','NOV','DEC'/

!=======================================================================
!     Data construct for control variables
      TYPE ControlType
        CHARACTER (len=1)  MESIC, RNMODE
        CHARACTER (len=2)  CROP
        CHARACTER (len=8)  MODEL, ENAME
        CHARACTER (len=12) FILEX
        CHARACTER (len=30) FILEIO
        CHARACTER (len=102)DSSATP
        CHARACTER (len=120) :: SimControl = 
     &  "                                                            "//
     &  "                                                            "
        INTEGER   DAS, DYNAMIC, FROP, ErrCode, LUNIO, MULTI, N_ELEMS
        INTEGER   NYRS, REPNO, ROTNUM, RUN, TRTNUM
        INTEGER   YRDIF, YRDOY, YRSIM
      END TYPE ControlType

!=======================================================================
!     Data construct for control switches
      TYPE SwitchType
        CHARACTER (len=1) FNAME
        CHARACTER (len=1) IDETC, IDETD, IDETG, IDETH, IDETL, IDETN
        CHARACTER (len=1) IDETO, IDETP, IDETR, IDETS, IDETW
        CHARACTER (len=1) IHARI, IPLTI, IIRRI, ISIMI
        CHARACTER (len=1) ISWCHE, ISWDIS, ISWNIT
        CHARACTER (len=1) ISWPHO, ISWPOT, ISWSYM, ISWTIL, ISWWAT
        CHARACTER (len=1) MEEVP, MEGHG, MEHYD, MEINF, MELI, MEPHO
        CHARACTER (len=1) MESOM, MESOL, MESEV, MEWTH
        CHARACTER (len=1) METMP !Temperature, EPIC
        CHARACTER (len=1) IFERI, IRESI, ICO2, FMOPT
        INTEGER NSWI
      END TYPE SwitchType

!Other switches and methods used by model:
! MELI, IOX - not used
! IDETH - only used in MgmtOps
! MEWTH - only used in WEATHR

!=======================================================================
!     Data construct for weather variables
      TYPE WeatherType
        SEQUENCE

!       Weather station information
        REAL REFHT, WINDHT, XLAT, XLONG, XELEV

!       Daily weather data.
        REAL CLOUDS, CO2, DAYL, DCO2, PAR, RAIN, RHUM, SNDN, SNUP, 
     &    SRAD, TAMP, TA, TAV, TAVG, TDAY, TDEW, TGROAV, TGRODY,      
     &    TMAX, TMIN, TWILEN, VAPR, WINDRUN, WINDSP, VPDF, VPD_TRANSP

!       Hourly weather data
        REAL, DIMENSION(TS) :: AMTRH, AZZON, BETA, FRDIFP, FRDIFR, PARHR
        REAL, DIMENSION(TS) :: RADHR, RHUMHR, TAIRHR, TGRO, WINDHR

      END TYPE WeatherType

!=======================================================================
!     Data construct for soil variables
      TYPE SoilType
        INTEGER NLAYR
        CHARACTER (len=5) SMPX
        CHARACTER (len=10) SLNO
        CHARACTER (len=12) TEXTURE(NL)
        CHARACTER (len=17) SOILLAYERTYPE(NL)
        CHARACTER*50 SLDESC, TAXON
        
        LOGICAL COARSE(NL)
        
        REAL ALES, DMOD, SLPF         !DMOD was SLNF
        REAL CMSALB, MSALB, SWALB, SALB      !Albedo 
        REAL, DIMENSION(NL) :: BD, CEC, CLAY, DLAYR, DS, DUL
        REAL, DIMENSION(NL) :: KG2PPM, LL, OC, PH, PHKCL, POROS
        REAL, DIMENSION(NL) :: SAND, SAT, SILT, STONES, SWCN
        
      !Residual water content
        REAL, DIMENSION(NL) :: WCR

      !vanGenuchten parameters
        REAL, DIMENSION(NL) :: alphaVG, mVG, nVG

      !Second tier soils data:
        REAL, DIMENSION(NL) :: CACO3, EXTP, ORGP, PTERMA, PTERMB
        REAL, DIMENSION(NL) :: TOTP, TOTBAS, EXCA, EXK, EXNA

      !Soil analysis data 
        REAL, DIMENSION(NL) :: SASC   !stable organic C

      !Variables added with new soil format:
        REAL ETDR, PONDMAX, SLDN, SLOPE
!       REAL, DIMENSION(NL) :: RCLPF, RGIMPF

      !Variables deleted with new soil format:
      !Still needed for Ritchie hydrology
        REAL CN, SWCON, U
        REAL, DIMENSION(NL) :: ADCOEF, TOTN, TotOrgN, WR

      !Text describing soil layer depth data
      !1-9 describe depths for layers 1-9
      !10 depths for layers 10 thru NLAYR (if NLAYR > 9)
      !11 depths for layers 5 thru NLAYR (if NLAYR > 4)
        CHARACTER*8 LayerText(11)

      !These variables could be made available if needed elsewhere.
      !  They are currently read by SOILDYN module.
      !  CHARACTER*5 SLTXS
      !  CHARACTER*11 SLSOUR
      !  CHARACTER*50 SLDESC, TAXON

      !Second tier soils data that could be used:
!        REAL, DIMENSION(NL) :: EXTAL, EXTFE, EXTMN, 
!        REAL, DIMENSION(NL) :: EXMG, EXTS, SLEC

      END TYPE SoilType

!=======================================================================
!     Data construct for mulch layer
      TYPE MulchType
        REAL MULCHMASS    !Mass of surface mulch layer (kg[dry mat.]/ha)
        REAL MULCHALB     !Albedo of mulch layer
        REAL MULCHCOVER   !Coverage of mulch layer (frac. of surface)
        REAL MULCHTHICK   !Thickness of mulch layer (mm)
        REAL MULCHWAT     !Water content of mulch (mm3/mm3)
        REAL MULCHEVAP    !Evaporation from mulch layer (mm/d)
        REAL MULCHSAT     !Saturation water content of mulch (mm3/mm3)
        REAL MULCHN       !N content of mulch layer (kg[N]/ha)
        REAL MULCHP       !P content of mulch layer (kg[P]/ha)
        REAL NEWMULCH     !Mass of new surface mulch (kg[dry mat.]/ha)
        REAL NEWMULCHWAT  !Water content of new mulch ((mm3/mm3)
        REAL MULCH_AM     !Area covered / dry weight of residue (ha/kg)
        REAL MUL_EXTFAC   !Light extinction coef. for mulch layer
        REAL MUL_WATFAC   !Saturation water content (mm[water] ha kg-1)
      END TYPE MulchType

!=======================================================================
!     Data construct for tillage operations
      TYPE TillType
        INTEGER NTIL      !Total number of tillage events in FILEX
        INTEGER TILDATE   !Date of current tillage event

!       Maximum values for multiple events in a single day
        REAL TILDEP, TILMIX, TILRESINC

!       Irrigation amount which affects tilled soil properties 
!          expressed in units of equivalent rainfall depth
        REAL TIL_IRR   

!       Allows multiple tillage passes in a day
        INTEGER NTil_today !number of tillage events today (max 3)
        INTEGER, DIMENSION(NAPPL) :: NLYRS
        REAL, DIMENSION(NAPPL) :: CNP, TDEP
        REAL, DIMENSION(NAPPL,NL) :: BDP, DEP, SWCNP
      END TYPE TillType

!=======================================================================
!     Data construct for oxidation layer
      TYPE OxLayerType
        INTEGER IBP
        REAL    OXU, OXH4, OXN3   
        REAL    OXLT, OXMIN4, OXMIN3
        REAL    DLTOXU, DLTOXH4, DLTOXN3
        REAL    ALGACT
        LOGICAL DailyCalc
      END TYPE OxLayerType

!======================================================================
!     Fertilizer application data
      TYPE FertType
        CHARACTER*7 AppType != 'UNIFORM', 'BANDED ' or 'HILL   '
        INTEGER FERTDAY, FERTYPE
        INTEGER, DIMENSION(NELEM) :: NAPFER
        REAL FERDEPTH, FERMIXPERC
        REAL ADDFNH4, ADDFNO3, ADDFUREA
        REAL ADDOXU, ADDOXH4, ADDOXN3
        REAL, DIMENSION(NELEM) :: AMTFER
        REAL, DIMENSION(NL) :: ADDSNH4, ADDSNO3, ADDUREA
        REAL, DIMENSION(NL) :: ADDSPi
        REAL, DIMENSION(NL) :: ADDSKi
        LOGICAL UNINCO
      END TYPE FertType

!=======================================================================
!   Data construct for residue (harvest residue, senesced matter, etc.)
      TYPE ResidueType
        REAL, DIMENSION(0:NL) :: ResWt        !kg[dry matter]/ha/d
        REAL, DIMENSION(0:NL) :: ResLig       !kg[lignin]/ha/d
        REAL, DIMENSION(0:NL,NELEM) :: ResE   !kg[E]/ha/d (E=N,P,K,..)
        REAL  CumResWt                        !cumul. kg[dry matter]/ha
        REAL, DIMENSION(NELEM) :: CumResE     !cumulative kg[E]/ha
      END TYPE ResidueType

!======================================================================
!     Organic Matter Application data
      TYPE OrgMatAppType
        INTEGER NAPRes, ResDat, ResDepth
        CHARACTER (len=5) RESTYPE
        REAL ResMixPerc   !Percent mixing rate for SOM module

        REAL, DIMENSION(0:NL) :: ResWt        !kg[dry matter]/ha/d
        REAL, DIMENSION(0:NL) :: ResLig       !kg[lignin]/ha/d
        REAL, DIMENSION(0:NL,NELEM) :: ResE   !kg[E]/ha/d (E=N, P, ..)
        REAL  CumResWt                        !cumul. kg[dry matter]/ha
        REAL, DIMENSION(NELEM) :: CumResE     !cumulative kg[E]/ha
      END TYPE OrgMatAppType

!======================================================================
!     Plant stresses for environmental stress summary
      Type PlStresType
        INTEGER NSTAGES   !# of stages (max 5)
        CHARACTER(len=23) StageName(0:5)
        REAL W_grow, W_phot, N_grow, N_phot
        REAL P_grow, P_phot
        LOGICAL ACTIVE(0:5)
      End Type PlStresType

!======================================================================
!     Array of output files, aliases, unit numbers, etc.
      Type OutputType
        INTEGER NumFiles
        CHARACTER*16, DIMENSION(MaxFiles) :: FileName
        CHARACTER*2,  DIMENSION(MaxFiles) :: OPCODE
        CHARACTER*50, DIMENSION(MaxFiles) :: Description
        CHARACTER*10, DIMENSION(MaxFiles) :: ALIAS
        INTEGER, DIMENSION(MaxFiles) :: LUN
      End Type OutputType


!======================================================================
!      CONTAINS
!
!!----------------------------------------------------------------------
!      SUBROUTINE SETOP ()
!      IMPLICIT NONE
!
!      WRITE(ModelVerTxt,'(I2.2,I1)') Version%Major, Version%Minor
!
!      END SUBROUTINE SETOP

!======================================================================
      END MODULE ModuleDefs
!======================================================================



!======================================================================
!     Paddy Managment routines.
!======================================================================
      MODULE FloodModule
!=======================================================================
!     Data construct for flood data. 
      Type FloodWatType
        !From IRRIG
        LOGICAL BUNDED        
        INTEGER NBUND         
        REAL ABUND            
        REAL PUDPERC, PERC
        REAL PLOWPAN    !Depth of puddling (m) (ORYZA)

        !From Paddy_Mgmt
        INTEGER YRDRY, YRWET  
        REAL FLOOD, FRUNOFF   
        REAL TOTBUNDRO        
        LOGICAL PUDDLED       

        REAL CEF, EF          !From SPAM
        REAL INFILT, RUNOFF   !From WATBAL
      End Type FloodWatType

      Type FloodNType
        INTEGER NDAT
        REAL    ALGFON                        !Algae kill or dry-up
        REAL    FLDH4C, FLDN3C                !Flood N concentrations
        REAL    FLDU, FLDN3, FLDH4            !Flood N mass (kg/ha)
        REAL    FRNH4U, FRNO3U                !Flood N uptake (kg/ha)
        REAL    DLTFUREA, DLTFNH4, DLTFNO3    !Flood N flux (kg/ha)
      End Type FloodNType

      END MODULE FloodModule
!======================================================================

!=======================================================================
!  MODULE ModuleData
!  01/22/2008 CHP Written
!=======================================================================

      MODULE ModuleData
!     Data storage and retrieval module.
!     Defines data structures that hold information that can be 
!       stored or accessed by query.  

!     A call to the GET routine will return the value of variable 
!       requested.  The procedure is "overloaded", i.e., the procedure 
!       executed will depend on the type of variable(s) in the argument 
!       list.  A request for a "real" data type will invoke the GET_Real
!       procedure, for example.  

!     Similarly, a call to the PUT routine will store the data sent.
!       It is also an overloaded procedure including several different
!       types of data which can be stored.

!     The SAVE_data variable is used to store all information.

!     To add a variable for storage and retrieval: 
!     1.  Add the variable to one of the Type constructs based on the 
!         module that "owns" the variable, for example SPAMType, Planttype 
!         or MgmtType.
!     2.  For a real data type, add a line of code in both the GET_Real and
!         PUT_Real subroutines.  
!     3.  For an integer data type, add a line of code in both the 
!         GET_Integer and PUT_Integer subroutines.  
!     4.  All routines accessing GET or PUT procedures must include a 
!         "USE ModuleData" statement.
!     5.  A call to the PUT routine must be used to store data prior to
!         a call to the GET routine to retrive the data.

      USE ModuleDefs
      SAVE

!======================================================================
!     Data transferred from hourly energy balance 
      Type SPAMType
        REAL AGEFAC, PG                   !photosynthese
        REAL CEF, CEM, CEO, CEP, CES, CET !Cumulative ET - mm
        REAL  EF,  EM,  EO,  EP,  ES,  ET !Daily ET - mm/d
        REAL  EOP, EVAP                   !Daily mm/d
        REAL, DIMENSION(NL) :: UH2O       !Root water uptake
        !ASCE reference ET with FAO-56 dual crop coefficient (KRT)
        REAL REFET, SKC, KCBMIN, KCBMAX, KCB, KE, KC
      End Type SPAMType

!     Data transferred from CROPGRO routine 
      TYPE PlantType
        REAL CANHT, CANWH, DXR57, EXCESS,
     &    PLTPOP, RNITP, SLAAD, XPOD
        REAL BIOMAS
        INTEGER NR5, iSTAGE, iSTGDOY
        CHARACTER*10 iSTNAME
      END TYPE PlantType

!     Data transferred from management routine 
      Type MgmtType
        REAL DEPIR, EFFIRR, FERNIT, IRRAMT, TOTIR, TOTEFFIRR
        REAL V_AVWAT(20)    ! Create vectors to save growth stage based irrigation
        REAL V_IMDEP(20)
        REAL V_ITHRL(20)
        REAL V_ITHRU(20)
        INTEGER V_IRON(20)
        REAL V_IRAMT(20)
        REAL V_IREFF(20)
        INTEGER V_IFREQ(20)
        INTEGER GSIRRIG
        CHARACTER*5 V_IRONC(20)
      End Type MgmtType

!     Data transferred from Soil water routine
      Type WatType
        REAL DRAIN, RUNOFF, SNOW
      End Type WatType

!     Data transferred from Soil Inorganic Nitrogen routine
      Type NiType
        REAL TNOXD, TLeachD    !, TN2OD     ! added N2O PG
      End Type NiType

!     Data transferred from Organic C routines
      Type OrgCType
        REAL TOMINFOM, TOMINSOM, TOMINSOM1, TOMINSOM2
        REAL TOMINSOM3, TNIMBSOM
        REAL MULCHMASS
      End Type OrgCType

!     Data from weather
      Type WeathType
        Character*8 WSTAT
      End Type WeathType

      TYPE PDLABETATYPE
        REAL PDLA
        REAL BETALS
      END TYPE PDLABETATYPE

!     Data which can be transferred between modules
      Type TransferType
        Type (ControlType) CONTROL
        Type (SwitchType)  ISWITCH
        Type (OutputType)  OUTPUT
        Type (PlantType)   PLANT
        Type (MgmtType)    MGMT
        Type (NiType)      NITR
        Type (OrgCType)    ORGC
        Type (SoilType)    SOILPROP
        Type (SPAMType)    SPAM
        Type (WatType)     WATER
        Type (WeathType)   WEATHER
        TYPE (PDLABETATYPE) PDLABETA
      End Type TransferType

!     The variable SAVE_data contains all of the components to be 
!     stored and retrieved.
      Type (TransferType) SAVE_data

!======================================================================
!     GET and PUT routines are differentiated by argument type.  All of 
!       these procedures can be accessed with a CALL GET(...)
      INTERFACE GET
         MODULE PROCEDURE GET_Control
     &                  , GET_ISWITCH 
     &                  , GET_Output 
     &                  , GET_SOILPROP
!     &                  , GET_Weather
     &                  , GET_Real 
     &                  , GET_Real_Array_NL
     &                  , GET_Integer
     &                  , GET_Char
      END INTERFACE

      INTERFACE PUT
         MODULE PROCEDURE PUT_Control
     &                  , PUT_ISWITCH 
     &                  , PUT_Output 
     &                  , PUT_SOILPROP
!     &                  , PUT_Weather
     &                  , PUT_Real 
     &                  , PUT_Real_Array_NL
     &                  , PUT_Integer
     &                  , PUT_Char
      END INTERFACE

      CONTAINS

!----------------------------------------------------------------------
      Subroutine Get_CONTROL (CONTROL_arg)
!     Retrieves CONTROL variable
      IMPLICIT NONE
      Type (ControlType) Control_arg
      Control_arg = SAVE_data % Control
      Return
      End Subroutine Get_CONTROL

!----------------------------------------------------------------------
      Subroutine Put_CONTROL (CONTROL_arg)
!     Stores CONTROL variable
      IMPLICIT NONE
      Type (ControlType) Control_arg
      SAVE_data % Control = Control_arg
      Return
      End Subroutine Put_CONTROL

!----------------------------------------------------------------------
      Subroutine Get_ISWITCH (ISWITCH_arg)
!     Retrieves ISWITCH variable
      IMPLICIT NONE
      Type (SwitchType) ISWITCH_arg
      ISWITCH_arg = SAVE_data % ISWITCH
      Return
      End Subroutine Get_ISWITCH

!----------------------------------------------------------------------
      Subroutine Put_ISWITCH (ISWITCH_arg)
!     Stores ISWITCH variable
      IMPLICIT NONE
      Type (SwitchType) ISWITCH_arg
      SAVE_data % ISWITCH = ISWITCH_arg
      Return
      End Subroutine Put_ISWITCH

!----------------------------------------------------------------------
      SUBROUTINE GET_OUTPUT(OUTPUT_ARG)
!     Retrieves OUTPUT variable as needed
      IMPLICIT NONE
      TYPE (OutputType) OUTPUT_ARG
      OUTPUT_ARG = SAVE_data % OUTPUT
      RETURN
      END SUBROUTINE GET_OUTPUT

!----------------------------------------------------------------------
      SUBROUTINE PUT_OUTPUT(OUTPUT_ARG)
!     Stores OUTPUT variable 
      IMPLICIT NONE
      TYPE (OutputType) OUTPUT_ARG
      SAVE_data % OUTPUT = OUTPUT_ARG
      RETURN
      END SUBROUTINE PUT_OUTPUT

!----------------------------------------------------------------------
      SUBROUTINE GET_SOILPROP(SOIL_ARG)
!     Retrieves SOILPROP variable as needed
      IMPLICIT NONE
      TYPE (SoilType) SOIL_ARG
      SOIL_ARG = SAVE_data % SOILPROP
      RETURN
      END SUBROUTINE GET_SOILPROP

!----------------------------------------------------------------------
      SUBROUTINE PUT_SOILPROP(SOIL_ARG)
!     Stores SOILPROP variable 
      IMPLICIT NONE
      TYPE (SoilType) SOIL_ARG
      SAVE_data % SOILPROP = SOIL_ARG
      RETURN
      END SUBROUTINE PUT_SOILPROP

!!----------------------------------------------------------------------
!      SUBROUTINE GET_WEATHER(WEATHER_ARG)
!!     Retrieves WEATHER variable as needed
!      IMPLICIT NONE
!      TYPE (WeathType) WEATHER_ARG
!      WEATHER_ARG = SAVE_data % WEATHER
!      RETURN
!      END SUBROUTINE GET_WEATHER
!
!!----------------------------------------------------------------------
!      SUBROUTINE PUT_WEATHER(WEATHER_ARG)
!!     Stores WEATHER variable 
!      IMPLICIT NONE
!      TYPE (WeathType) WEATHER_ARG
!      SAVE_data % WEATHER = WEATHER_ARG
!      RETURN
!      END SUBROUTINE PUT_WEATHER

!----------------------------------------------------------------------
      Subroutine GET_Real(ModuleName, VarName, Value)
!     Retrieves real variable from SAVE_data.  Variable must be
!         included as a component of SAVE_data. 
      IMPLICIT NONE
      Character*(*) ModuleName, VarName
!      Character*78 MSG(2)
      Real Value
      Logical ERR

!     The following *_tmp variables are introduced to get around a bug in OFP 
!     that causes it to choke on RHS expressions of the form X % Y % Z
      
      Type (SPAMType) SPAM_tmp
      Type (PlantType) Plant_tmp
      Type (MgmtType) Mgmt_tmp
      Type (WatType) Wat_tmp
      Type (NiType) Ni_tmp
      Type (OrgCType) OrgC_tmp
      Type (PDLABETATYPE) PDLABETA_tmp

      Value = 0.0
      ERR = .FALSE.

      SELECT CASE (ModuleName)
      Case ('SPAM')
        SPAM_tmp = SAVE_data % SPAM
        SELECT CASE (VarName)
        Case ('AGEFAC'); Value = SPAM_tmp % AGEFAC
        Case ('PG');     Value = SPAM_tmp % PG
        Case ('CEF');    Value = SPAM_tmp % CEF
        Case ('CEM');    Value = SPAM_tmp % CEM
        Case ('CEO');    Value = SPAM_tmp % CEO
        Case ('CEP');    Value = SPAM_tmp % CEP
        Case ('CES');    Value = SPAM_tmp % CES
        Case ('CET');    Value = SPAM_tmp % CET
        Case ('EF');     Value = SPAM_tmp % EF
        Case ('EM');     Value = SPAM_tmp % EM
        Case ('EO');     Value = SPAM_tmp % EO
        Case ('EP');     Value = SPAM_tmp % EP
        Case ('ES');     Value = SPAM_tmp % ES
        Case ('ET');     Value = SPAM_tmp % ET
        Case ('EOP');    Value = SPAM_tmp % EOP
        Case ('EVAP');   Value = SPAM_tmp % EVAP
        Case ('REFET');  Value = SPAM_tmp % REFET
        Case ('SKC');    Value = SPAM_tmp % SKC
        Case ('KCBMIN'); Value = SPAM_tmp % KCBMIN
        Case ('KCBMAX'); Value = SPAM_tmp % KCBMAX
        Case ('KCB');    Value = SPAM_tmp % KCB
        Case ('KE');     Value = SPAM_tmp % KE
        Case ('KC');     Value = SPAM_tmp % KC
        Case DEFAULT; ERR = .TRUE.
        END SELECT

      Case ('PLANT')
         Plant_tmp = SAVE_data % PLANT
        SELECT CASE (VarName)
        Case ('BIOMAS'); Value = Plant_tmp % BIOMAS
        Case ('CANHT') ; Value = Plant_tmp % CANHT
        Case ('CANWH') ; Value = Plant_tmp % CANWH
        Case ('DXR57') ; Value = Plant_tmp % DXR57
        Case ('EXCESS'); Value = Plant_tmp % EXCESS
        Case ('PLTPOP'); Value = Plant_tmp % PLTPOP
        Case ('RNITP') ; Value = Plant_tmp % RNITP
        Case ('SLAAD') ; Value = Plant_tmp % SLAAD
        Case ('XPOD')  ; Value = Plant_tmp % XPOD
        Case DEFAULT; ERR = .TRUE.
        END SELECT

      Case ('MGMT')
         Mgmt_tmp = SAVE_data % MGMT
        SELECT CASE (VarName)
        Case ('EFFIRR'); Value = Mgmt_tmp % EFFIRR
        Case ('TOTIR');  Value = Mgmt_tmp % TOTIR
        Case ('TOTEFFIRR');Value=Mgmt_tmp % TOTEFFIRR
        Case ('DEPIR');  Value = Mgmt_tmp % DEPIR
        Case ('IRRAMT'); Value = Mgmt_tmp % IRRAMT
        Case ('FERNIT'); Value = Mgmt_tmp % FERNIT
        Case DEFAULT; ERR = .TRUE.
        END SELECT

      Case ('WATER')
         Wat_tmp = SAVE_data % WATER
        SELECT CASE (VarName)
        Case ('DRAIN'); Value = Wat_tmp % DRAIN
        Case ('RUNOFF');Value = Wat_tmp % RUNOFF
        Case ('SNOW');  Value = Wat_tmp % SNOW
        Case DEFAULT; ERR = .TRUE.
        END SELECT

      Case ('NITR')
         Ni_tmp = SAVE_data % NITR
        SELECT CASE (VarName)
        Case ('TNOXD'); Value = Ni_tmp % TNOXD
       Case ('TLCHD'); Value = Ni_tmp % TLeachD
!       Case ('TN2OD'); Value = Ni_tmp % TN2OD
        Case DEFAULT; ERR = .TRUE.
        END SELECT

      Case ('ORGC')
         OrgC_tmp = SAVE_data % ORGC
        SELECT CASE (VarName)
        Case ('MULCHMASS');Value = OrgC_tmp % MULCHMASS
        Case ('TOMINFOM'); Value = OrgC_tmp % TOMINFOM
        Case ('TOMINSOM'); Value = OrgC_tmp % TOMINSOM
        Case ('TOMINSOM1');Value = OrgC_tmp % TOMINSOM1
        Case ('TOMINSOM2');Value = OrgC_tmp % TOMINSOM2
        Case ('TOMINSOM3');Value = OrgC_tmp % TOMINSOM3
        Case ('TNIMBSOM'); Value = OrgC_tmp % TNIMBSOM
        Case DEFAULT; ERR = .TRUE.
        END SELECT

      Case ('SOIL')
         OrgC_tmp = SAVE_data % ORGC
        SELECT CASE (VarName)
        Case ('TOMINFOM'); Value = OrgC_tmp % TOMINFOM
        Case ('TOMINSOM'); Value = OrgC_tmp % TOMINSOM
        Case ('TOMINSOM1'); Value = OrgC_tmp % TOMINSOM1
        Case ('TOMINSOM2'); Value = OrgC_tmp % TOMINSOM2
        Case ('TOMINSOM3'); Value = OrgC_tmp % TOMINSOM3
        Case ('TNIMBSOM'); Value = OrgC_tmp % TNIMBSOM
        Case DEFAULT; ERR = .TRUE.
        END SELECT

      CASE ('PDLABETA')
         PDLABETA_tmp = SAVE_data % PDLABETA
        SELECT CASE(VarName)
        CASE('PDLA'); Value = PDLABETA_tmp % PDLA
        CASE('BETA'); Value = PDLABETA_tmp % BETALS
        CASE DEFAULT; ERR = .TRUE.
        END SELECT
            
      Case DEFAULT; ERR = .TRUE.
      END SELECT

!      IF (ERR) THEN
!        MSG(1) = "Error transferring variable: " // Trim(VarName) // " in " // Trim(ModuleName)
!        WRITE(MSG(1),'("Error transferring variable: ",A, " in ",A)')
!     &      Trim(VarName), Trim(ModuleName)
!        MSG(2) = 'Value set to zero.'
!        CALL WARNING(2,'GET_REAL',MSG)
!      ENDIF

      RETURN
      END SUBROUTINE GET_Real

!----------------------------------------------------------------------
      SUBROUTINE PUT_Real(ModuleName, VarName, Value)
!     Stores real variable SAVE_data.  
      IMPLICIT NONE
      Character*(*) ModuleName, VarName
!      Character*78 MSG(2)
      Real Value
      Logical ERR

!     The following *_tmp variables are introduced to get around a bug in OFP 
!     that causes it to choke on RHS expressions of the form X % Y % Z
      
      Type (SPAMType) SPAM_tmp
      Type (PlantType) Plant_tmp
      Type (MgmtType) Mgmt_tmp
      Type (WatType) Wat_tmp
      Type (NiType) Ni_tmp
      Type (OrgCType) OrgC_tmp
      Type (PDLABETATYPE) PDLABETA_tmp

      ERR = .FALSE.

      SELECT CASE (ModuleName)
      Case ('SPAM')
        SPAM_tmp = SAVE_data % SPAM
        SELECT CASE (VarName)
        Case ('AGEFAC'); SPAM_tmp % AGEFAC = Value
        Case ('PG');     SPAM_tmp % PG     = Value
        Case ('CEF');    SPAM_tmp % CEF    = Value
        Case ('CEM');    SPAM_tmp % CEM    = Value
        Case ('CEO');    SPAM_tmp % CEO    = Value
        Case ('CEP');    SPAM_tmp % CEP    = Value
        Case ('CES');    SPAM_tmp % CES    = Value
        Case ('CET');    SPAM_tmp % CET    = Value
        Case ('EF');     SPAM_tmp % EF     = Value
        Case ('EM');     SPAM_tmp % EM     = Value
        Case ('EO');     SPAM_tmp % EO     = Value
        Case ('EP');     SPAM_tmp % EP     = Value
        Case ('ES');     SPAM_tmp % ES     = Value
        Case ('ET');     SPAM_tmp % ET     = Value
        Case ('EOP');    SPAM_tmp % EOP    = Value
        Case ('EVAP');   SPAM_tmp % EVAP   = Value
        Case ('REFET');  SPAM_tmp % REFET  = Value
        Case ('SKC');    SPAM_tmp % SKC    = Value
        Case ('KCBMIN'); SPAM_tmp % KCBMIN = Value
        Case ('KCBMAX'); SPAM_tmp % KCBMAX = Value
        Case ('KCB');    SPAM_tmp % KCB    = Value
        Case ('KE');     SPAM_tmp % KE     = Value
        Case ('KC');     SPAM_tmp % KC     = Value
        Case DEFAULT; ERR = .TRUE.
        END SELECT

      Case ('PLANT')
        Plant_tmp = SAVE_data % PLANT
        SELECT CASE (VarName)
        Case ('BIOMAS'); PLANT_tmp % BIOMAS = Value
        Case ('CANHT');  PLANT_tmp % CANHT  = Value
        Case ('CANWH');  PLANT_tmp % CANWH  = Value
        Case ('DXR57');  PLANT_tmp % DXR57  = Value
        Case ('EXCESS'); PLANT_tmp % EXCESS = Value
        Case ('PLTPOP'); PLANT_tmp % PLTPOP = Value
        Case ('RNITP');  PLANT_tmp % RNITP  = Value
        Case ('SLAAD');  PLANT_tmp % SLAAD  = Value
        Case ('XPOD');   PLANT_tmp % XPOD   = Value
        Case DEFAULT; ERR = .TRUE.
        END SELECT

      Case ('MGMT')
        Mgmt_tmp = SAVE_data % MGMT
        SELECT CASE (VarName)
        Case ('EFFIRR'); MGMT_tmp % EFFIRR = Value
        Case ('TOTIR');  MGMT_tmp % TOTIR  = Value
        Case ('TOTEFFIRR'); MGMT_tmp % TOTEFFIRR=Value
        Case ('DEPIR');  MGMT_tmp % DEPIR  = Value
        Case ('IRRAMT'); MGMT_tmp % IRRAMT = Value
        Case ('FERNIT'); MGMT_tmp % FERNIT = Value
        Case DEFAULT; ERR = .TRUE.
        END SELECT

      Case ('WATER')
        Wat_tmp = SAVE_data % WATER
        SELECT CASE (VarName)
        Case ('DRAIN'); Wat_tmp % DRAIN  = Value
        Case ('RUNOFF');Wat_tmp % RUNOFF = Value
        Case ('SNOW');  Wat_tmp % SNOW   = Value
        Case DEFAULT; ERR = .TRUE.
        END SELECT

      Case ('NITR')
        Ni_tmp = SAVE_data % NITR
        SELECT CASE (VarName)
        Case ('TNOXD'); Ni_tmp % TNOXD = Value
        Case ('TLCHD'); Ni_tmp % TLeachD = Value
!       Case ('TN2OD'); SAVE_data % NITR % TN2OD = Value
        Case DEFAULT; ERR = .TRUE.
        END SELECT

      Case ('ORGC')
        OrgC_tmp = SAVE_data % ORGC
        SELECT CASE (VarName)
        Case ('MULCHMASS');OrgC_tmp % MULCHMASS = Value
        Case ('TOMINFOM'); OrgC_tmp % TOMINFOM  = Value
        Case ('TOMINSOM'); OrgC_tmp % TOMINSOM  = Value
        Case ('TOMINSOM1');OrgC_tmp % TOMINSOM1 = Value
        Case ('TOMINSOM2');OrgC_tmp % TOMINSOM2 = Value
        Case ('TOMINSOM3');OrgC_tmp % TOMINSOM3 = Value
        Case ('TNIMBSOM'); OrgC_tmp % TNIMBSOM  = Value
        Case DEFAULT; ERR = .TRUE.
        END SELECT

      CASE ('PDLABETA')
        PDLABETA_tmp = SAVE_data % PDLABETA
        SELECT CASE(VarName)
        CASE('PDLA'); PDLABETA_tmp % PDLA = Value
        CASE('BETA'); PDLABETA_tmp % BETALS = Value
        CASE DEFAULT; ERR = .TRUE.
        END SELECT
            
      Case DEFAULT; ERR = .TRUE.
      END SELECT

!      IF (ERR) THEN
!        MSG(1) = "Error transferring variable: " // Trim(VarName) // " in " // Trim(ModuleName)
!        WRITE(MSG(1),'("Error transferring variable: ",A, "in ",A)')
!     &      Trim(VarName), Trim(ModuleName)
!        MSG(2) = 'Value not saved! Errors may result.'
!        CALL WARNING(2,'PUT_REAL',MSG)
!      ENDIF

      RETURN
      END SUBROUTINE PUT_Real

!----------------------------------------------------------------------
      SUBROUTINE GET_Real_Array_NL(ModuleName, VarName, Value)
!     Retrieves array of dimension(NL) 
      IMPLICIT NONE
      Character*(*) ModuleName, VarName
!      Character*78 MSG(2)
      REAL, DIMENSION(NL) :: Value
      Logical ERR
      Type (SPAMType) SPAM_tmp

      Value = 0.0
      ERR = .FALSE.

      SELECT CASE (ModuleName)

      CASE ('SPAM')
        SELECT CASE (VarName)
        CASE ('UH2O');
           SPAM_tmp = SAVE_data % SPAM
           Value = SPAM_tmp % UH2O
        CASE DEFAULT; ERR = .TRUE.
        END SELECT

        CASE DEFAULT; ERR = .TRUE.
      END SELECT

!      IF (ERR) THEN
!        MSG(1) = "Error transferring variable: " // Trim(VarName) // " in " // Trim(ModuleName)
!        WRITE(MSG(1),'("Error transferring variable: ",A, "in ",A)')
!     &      Trim(VarName), Trim(ModuleName)
!        MSG(2) = 'Value set to zero.'
!        CALL WARNING(2,'GET_Real_Array_NL',MSG)
!      ENDIF

      RETURN
      END SUBROUTINE GET_Real_Array_NL

!----------------------------------------------------------------------
      SUBROUTINE PUT_Real_Array_NL(ModuleName, VarName, Value)
!     Stores array of dimension NL
      IMPLICIT NONE
      Character*(*) ModuleName, VarName
!      Character*78 MSG(2)
      REAL, DIMENSION(NL) :: Value
      Logical ERR

      ERR = .FALSE.

      SELECT CASE (ModuleName)
      Case ('SPAM')
        SELECT CASE (VarName)
        Case ('UH2O'); SAVE_data % SPAM % UH2O = Value
        Case DEFAULT; ERR = .TRUE.
        END SELECT

      Case DEFAULT; ERR = .TRUE.
      END SELECT

!      IF (ERR) THEN
!        MSG(1) = "Error transferring variable: " // Trim(VarName) // " in " // Trim(ModuleName)
!        WRITE(MSG(1),'("Error transferring variable: ",A, "in ",A)')
!     &      Trim(VarName), Trim(ModuleName)
!        MSG(2) = 'Value not saved! Errors may result.'
!        CALL WARNING(2,'PUT_Real_Array_NL',MSG)
!      ENDIF

      RETURN
      END SUBROUTINE PUT_Real_Array_NL

!----------------------------------------------------------------------
      Subroutine GET_Integer(ModuleName, VarName, Value)
!     Retrieves Integer variable as needed
      IMPLICIT NONE
      Character*(*) ModuleName, VarName
!      Character*78  MSG(2)
      Integer Value
      Logical ERR
      Type (PlantType) Plant_tmp

      Value = 0
      ERR = .FALSE.

      SELECT CASE (ModuleName)
      Case ('PLANT')
         Plant_tmp = SAVE_data % PLANT
        SELECT CASE (VarName)
        Case ('NR5');  Value = Plant_tmp % NR5
        Case ('iSTAGE');  Value = Plant_tmp % iSTAGE
        Case ('iSTGDOY'); Value = Plant_tmp % iSTGDOY
        Case DEFAULT; ERR = .TRUE.
        END SELECT

      Case Default; ERR = .TRUE.
      END SELECT

!      IF (ERR) THEN
!        MSG(1) = "Error transferring variable: " // Trim(VarName) // " in " // Trim(ModuleName)
!        WRITE(MSG(1),'("Error transferring variable: ",A, "in ",A)')
!     &      Trim(VarName), Trim(ModuleName)
!        MSG(2) = 'Value set to zero.'
!        CALL WARNING(2,'GET_INTEGER',MSG)
!      ENDIF

      RETURN
      END SUBROUTINE GET_Integer

!----------------------------------------------------------------------
      SUBROUTINE PUT_Integer(ModuleName, VarName, Value)
!     Stores Integer variable
      IMPLICIT NONE
      Character*(*) ModuleName, VarName
!      Character*78 MSG(2)
      Integer Value
      Logical ERR
      Type (PlantType) Plant_tmp

      ERR = .FALSE.

      SELECT CASE (ModuleName)
      Case ('PLANT')
        Plant_tmp = SAVE_data % PLANT
        SELECT CASE (VarName)
        Case ('NR5');  PLANT_tmp % NR5  = Value
        Case ('iSTAGE');  PLANT_tmp % iSTAGE  = Value
        Case ('iSTGDOY'); PLANT_tmp % iSTGDOY = Value
        Case DEFAULT; ERR = .TRUE.
        END SELECT

      Case DEFAULT; ERR = .TRUE.
      END SELECT

!      IF (ERR) THEN
!        MSG(1) = "Error transferring variable: " // Trim(VarName) // " in " // Trim(ModuleName)
!        WRITE(MSG(1),'("Error transferring variable: ",A, "in ",A)')
!     &      Trim(VarName), Trim(ModuleName)
!        MSG(2) = 'Value not saved! Errors may result.'
!        CALL WARNING(2,'PUT_Integer',MSG)
!      ENDIF

      RETURN
      END SUBROUTINE PUT_Integer

!----------------------------------------------------------------------
      Subroutine GET_Char(ModuleName, VarName, Value)
!     Retrieves Integer variable as needed
      IMPLICIT NONE
      Character*(*) ModuleName, VarName, Value
!      Character*78  MSG(2)
      Logical ERR
      Type (PlantType) Plant_tmp
      Type (WeathType) Weath_tmp

      Value = ' '
      ERR = .FALSE.

      SELECT CASE (ModuleName)
      Case ('WEATHER')
        SELECT CASE (VarName)
        Case ('WSTA');
           Weath_tmp = SAVE_data % WEATHER
           Value = Weath_tmp % WSTAT
        Case DEFAULT; ERR = .TRUE.
        END SELECT

      Case ('PLANT')
        SELECT CASE (VarName)
        Case ('iSTNAME');
           Plant_tmp = SAVE_data % PLANT
           Value = Plant_tmp % iSTNAME
        Case DEFAULT; ERR = .TRUE.
        END SELECT

      Case Default; ERR = .TRUE.
      END SELECT

!      IF (ERR) THEN
!        MSG(1) = "Error transferring variable: " // Trim(VarName) // " in " // Trim(ModuleName)
!        WRITE(MSG(1),'("Error transferring variable: ",A, "in ",A)')
!     &      Trim(VarName), Trim(ModuleName)
!        MSG(2) = 'Value set to zero.'
!        CALL WARNING(2,'GET_INTEGER',MSG)
!      ENDIF

      RETURN
      END SUBROUTINE GET_Char

!----------------------------------------------------------------------
      SUBROUTINE PUT_Char(ModuleName, VarName, Value)
!     Stores Character variable
      IMPLICIT NONE
      Character*(*) ModuleName, VarName, Value
!      Character*78 MSG(2)
      Logical ERR
      Type (PlantType) Plant_tmp
      Type (WeathType) Weath_tmp

      ERR = .FALSE.

      SELECT CASE (ModuleName)
      Case ('WEATHER')
        SELECT CASE (VarName)
        Case ('WSTA');  
          Weath_tmp = SAVE_data % WEATHER
          Weath_tmp % WSTAT  = Value
        Case DEFAULT; ERR = .TRUE.
        END SELECT

      Case ('PLANT')
        SELECT CASE (VarName)
        Case ('iSTNAME');
          Plant_tmp = SAVE_data % PLANT
          PLANT_tmp % iSTNAME = Value
        Case DEFAULT; ERR = .TRUE.
        END SELECT

      Case DEFAULT; ERR = .TRUE.
      END SELECT

!      IF (ERR) THEN
!        MSG(1) = "Error transferring variable: " // Trim(VarName) // " in " // Trim(ModuleName)
!        WRITE(MSG(1),'("Error transferring variable: ",A, "in ",A)')
!     &      Trim(VarName), Trim(ModuleName)
!        MSG(2) = 'Value not saved! Errors may result.'
!        CALL WARNING(2,'PUT_Integer',MSG)
!      ENDIF

      RETURN
      END SUBROUTINE PUT_Char

!======================================================================
      END MODULE ModuleData
!======================================================================
