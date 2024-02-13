"""
This script runs 50 iterations of CFR+ in a Leduc poker game with actions {FOLD, CHECK/CALL, POT-SIZE-BET/RAISE}.

It will store logs and tree files on "logs" folder

The agent bet set is B_5, which means that the agent can only bet the pot size.

"""

from PokerRL.cfr.CFRPlus import CFRPlus
from PokerRL.game import bet_sets
from PokerRL.game.games import DiscretizedNLLeduc
# from PokerRL.game.games import DiscretizedNLHoldem
from PokerRL.rl.base_cls.workers.ChiefBase import ChiefBase

if __name__ == '__main__':
    from PokerRL._.CrayonWrapper import CrayonWrapper

    n_iterations = 50
    name = "CFRplus_agent_2"

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
                  agent_bet_set=bet_sets.B_5,
                  chief_handle=chief)

    for iter_id in range(n_iterations):
        print("Iteration: ", iter_id)
        cfr.iteration()
        crayon.update_from_log_buffer()
        crayon.export_all(iter_nr=iter_id)



# # from PokerRL.eval.br import LocalBRMaster

#     # #Evaluate the agent
#     # lbr_master = LocalBRMaster(None, chief, cfr)
#     # lbr_results = lbr_master.run_evaluation()
#     # print("LBR Evaluation Results:", lbr_results)
