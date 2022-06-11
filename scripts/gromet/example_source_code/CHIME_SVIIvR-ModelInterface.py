from gromet import *

variables = \
    [
        # -- parameters --

        # i_day                 : UidJunction("J:main.i_day")
        UidVariable("V:i_day"),
        # n_days                : UidJunction("J:main.n_days")
        UidVariable("V:n_days"),
        # N_p                   : UidJunction("J:main.N_p")
        UidVariable("V:N_p"),

        # Removed from CHIME_SIR_Base
        # # infections_days       : UidJunction("J:main.infections_days")
        # UidVariable("V:infections_days"),

        # CHIME_SVIIvR
        # infections_days_unvaccinated  : UidJunction("J:main.infections_days_unvaccinated")
        UidVariable("V:infections_days_unvaccinated"),

        # CHIME_SVIIvR
        # infections_days_vaccinated    : UidJunction("J:main.infections_days_vaccinated")
        UidVariable("V:infections_days_vaccinated"),

        # CHIME_SVIIvR
        # vaccination_rate              : UidJunction("J:main.vaccination_rate")
        UidVariable("V:vaccination_rate"),

        # CHIME_SVIIvR
        # vaccine_efficacy              : UidJunction("J:main.vaccine_efficacy")
        UidVariable("V:vaccine_efficacy"),

        # relative_contact_rate : UidJunction("J:main.relative_contact_rate")
        UidVariable("V:relative_contact_rate"),

        # -- initial conditions --

        # s_n                   : UidJunction("J:main.s_n")
        UidVariable("V:s_n"),

        # CHIME_SVIIvR
        # v_n                   : UidJuncxtion("J:main.v_n")
        UidVariable("V:v_n"),

        # i_n                   : UidJunction("J:main.i_n")
        UidVariable("V:i_n"),

        # CHIME_SVIIvR
        # i_v_n                 : UidJunction("J:main.i_v_n")
        UidVariable("V:i_v_n"),

        # r_n                   : UidJunction("J:main.r_n")
        UidVariable("V:r_n"),

        # -- typical measurements --

        # out S                 : UidPort("P:main.out.S")
        UidVariable("V:S"),

        # CHIME_SVIIvR
        # out V                 : UidPort("P:main.out.V")
        UidVariable("V:V"),

        # out I                 : UidPort("P:main.out.I")
        UidVariable("V:I"),

        # CHIME_SVIIvR
        # out Iv                : UidPort("P:main.out.Iv")
        UidVariable("V:Iv"),

        # out R                 : UidPort("P:main.out.R")
        UidVariable("V:R"),

        # out E                 : UidPort("P:main.out.E")
        UidVariable("V:E"),
    ],
parameters = \
    [
        # i_day                 : UidJunction("J:main.i_day")
        UidVariable("V:i_day"),
        # n_days                : UidJunction("J:main.n_days")
        UidVariable("V:n_days"),
        # N_p                   : UidJunction("J:main.N_p")
        UidVariable("V:N_p"),

        # REMOVE_CHIME_SIR_Base
        # infections_days       : UidJunction("J:main.infections_days")
        # UidVariable("V:infections_days"),

        # CHIME_SVIIvR
        # infections_days_unvaccinated  : UidJunction("J:main.infections_days_unvaccinated")
        UidVariable("V:infections_days_unvaccinated"),

        # CHIME_SVIIvR
        # infections_days_vaccinated    : UidJunction("J:main.infections_days_vaccinated")
        UidVariable("V:infections_days_vaccinated"),

        # CHIME_SVIIvR
        # vaccination_rate              : UidJunction("J:main.vaccination_rate")
        UidVariable("V:vaccination_rate"),

        # CHIME_SVIIvR
        # vaccine_efficacy              : UidJunction("J:main.vaccine_efficacy")
        UidVariable("V:vaccine_efficacy"),

        # relative_contact_rate : UidJunction("J:main.relative_contact_rate")
        UidVariable("V:relative_contact_rate"),
    ],
initial_conditions = \
    [
        # s_n                   : UidJunction("J:main.s_n")
        UidVariable("V:s_n"),
        # i_n                   : UidJunction("J:main.i_n")
        UidVariable("V:i_n"),
        # r_n                   : UidJunction("J:main.r_n")
        UidVariable("V:r_n"),

        # CHIME_SVIIvR
        # v_n                   : UidJuncxtion("J:main.v_n")
        UidVariable("V:v_n"),

        # CHIME_SVIIvR
        # i_v_n                 : UidJunction("J:main.i_v_n")
        UidVariable("V:i_v_n"),
    ]
