

# Copyright (c) 2019 Eric Steinberger


"""
This script runs 150 iterations of CFR+ in a Leduc poker game with actions {FOLD, CHECK/CALL, POT-SIZE-BET/RAISE}.


It will store logs and tree files on "logs" folder
The agent bet set is POT_ONLY, which means that the agent can only bet the pot size.

"""

from PokerRL.cfr.CFRPlus import CFRPlus
from PokerRL.game import bet_sets
from PokerRL.game.games import DiscretizedNLLeduc
from PokerRL.rl.base_cls.workers.ChiefBase import ChiefBase

if __name__ == '__main__':
    from PokerRL._.CrayonWrapper import CrayonWrapper

    n_iterations = 150
    name = "CFRplus_EXAMPLE_2024_02_13_example1"

    # Passing None for t_prof will is enough for ChiefBase. We only use it to log; This CFR impl is not distributed.
    chief = ChiefBase(t_prof=None)
    crayon = CrayonWrapper(name=name,
                           path_log_storage="logs/",
                           chief_handle=chief,
                           runs_distributed=False,
                           runs_cluster=False)
    cfr = CFRPlus(name=name,
                  game_cls=DiscretizedNLLeduc,
                  delay=0,
                  agent_bet_set=bet_sets.POT_ONLY,
                  chief_handle=chief)

    for iter_id in range(n_iterations):
        print("Iteration: ", iter_id)
        cfr.iteration()
        crayon.update_from_log_buffer()
        crayon.export_all(iter_nr=iter_id)



# """
# This script runs 150 iterations of Linear CFR in a No-Limit Texas Hold'em poker game with actions {FOLD, CHECK/CALL, POT-SIZE-BET/RAISE}.
# It will store logs and tree files on your C: drive.

# """

# from PokerRL.cfr.LinearCFR import LinearCFR
# from PokerRL.game import bet_sets
# from PokerRL.game.games import DiscretizedNLHoldem
# from PokerRL.rl.base_cls.workers.ChiefBase import ChiefBase

# # from PokerRL.eval.br import LocalBRMaster


# if __name__ == '__main__':
#     from PokerRL._.CrayonWrapper import CrayonWrapper

#     n_iterations = 150
#     name = "LinCFR_EXAMPLE_2024_02_13"

#     # Passing None for t_prof will is enough for ChiefBase. We only use it to log; This CFR impl is not distributed.
#     chief = ChiefBase(t_prof=None)
#     crayon = CrayonWrapper(name=name,
#                            path_log_storage=None,
#                            chief_handle=chief,
#                            runs_distributed=False,
#                            runs_cluster=False)
#     cfr = LinearCFR(name=name,
#                     game_cls=DiscretizedNLHoldem,
#                     agent_bet_set=bet_sets.POT_ONLY,
#                     chief_handle=chief)

#     for iter_id in range(n_iterations):
#         print("Iteration: ", iter_id)
#         cfr.iteration()
#         crayon.update_from_log_buffer()
#         crayon.export_all(iter_nr=iter_id)

#     # #Evaluate the agent
#     # lbr_master = LocalBRMaster(None, chief, cfr)
#     # lbr_results = lbr_master.run_evaluation()
#     # print("LBR Evaluation Results:", lbr_results)
