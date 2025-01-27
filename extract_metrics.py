import m5
from m5.objects import *

def extract_metrics(stats_file, results):
    # Load statistics from the stats file
    stats = m5.stats.stats.parse(stats_file)
    
    # Extract  metrics
    sim_seconds = stats.system.simSeconds.value
    sim_ticks = stats.system.simTicks.value
    final_tick = stats.system.finalTick.value
    sim_freq = stats.system.simFreq.value
    host_seconds = stats.system.hostSeconds.value
    host_tick_rate = stats.system.hostTickRate.value
    host_memory = stats.system.hostMemory.value
    sim_insts = stats.system.simInsts.value
    sim_ops = stats.system.simOps.value
    host_inst_rate = stats.system.hostInstRate.value
    host_op_rate = stats.system.hostOpRate.value
    clk_domain_clock = stats.system.clk_domain.clock.value
    voltage_domain_voltage = stats.system.clk_domain.voltage_domain.voltage.value
    
with open(results, 'w') as f:
        f.write("simSeconds: {}\n".format(sim_seconds))
        f.write("simTicks: {}\n".format(sim_ticks))
        f.write("finalTick:{}\n".format(final_tick))
        f.write("simFreq:{}\n".format(sim_freq))
        f.write("hostSeconds:{}\n".format(host_seconds)
        f.write("hostTickRate: {}\n".format(host_tick_rate))
        f.write("hostMemory: {}\n".format(host_memory))
        f.write("simInsts:{}\n".format(sim_insts))
        f.write("simOps:{}\n".format(sim_Ops))"
        f.write("hostInstRate: {}\n".format(host_inst_rate))
        f.write("hostOpRate: {}\n".format(host_ops_rate))
        f.write("clkDomainClock:{}\n".format(clk_domain_clock))
        f.write("voltage_domain_voltage:{}\n".format(voltage_domain_voltage))"    

if __name__ == "__main__":
 
    stats_file = "m5out/stats.txt"  

    extract_metrics(stats_file)
