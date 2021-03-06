# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: DisappTrks/SignalMC/python/charginoParticleGun_cfi.py -s GEN,SIM --conditions auto:mc --mc --datatier GEN-SIM --eventcontent RAWSIM -n 5 --no_exec --fileout charginoPartGun_GEN_SIM.root
import FWCore.ParameterSet.Config as cms
import sys 

# The particle type may be specified as an additional argument, e.g.:
# $ cmsRun exoticParticleGun_cfi_py_GEN_SIM.py stau 
particleType = "chargino"
if len(sys.argv) > 2:
    particleType = sys.argv[2]  

process = cms.Process('SIM')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.Geometry.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedNominalCollision2015_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(5)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('DisappTrks/SignalMC/python/charginoParticleGun_cfi.py nevts:5'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('exoticPartGun_' + particleType + '.root'), 
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:mc', '')

process.generator = cms.EDProducer("FlatRandomPtGunProducer",
#				   pythiaPylistVerbosity = cms.untracked.int32(0),
#				   slhaFile = cms.untracked.string('Configuration/Generator/data/AMSB_chargino_100GeV_Isajet780.slha'),
				   slhaFile = cms.untracked.string(''),   
				   particleFile = cms.untracked.string('DisappTrks/SignalMC/data/geant4_AMSB_chargino_test.slha'),
				   filterEfficiency = cms.untracked.double(1.0),
				   pythiaHepMCVerbosity = cms.untracked.bool(False),
				   processFile = cms.untracked.string('SimG4Core/CustomPhysics/data/RhadronProcessList.txt'),
				   useregge = cms.bool(False),
				   comEnergy = cms.double(8000.0),
				   maxEventsToPrint = cms.untracked.int32(0),
				   hscpFlavor = cms.untracked.string('stau'),
				   massPoint = cms.untracked.int32(150),
    AddAntiParticle = cms.bool(False),
    PGunParameters = cms.PSet(
        MaxEta = cms.double(2.5),
        MaxPhi = cms.double(3.14159265359),
        MaxPt = cms.double(100.01),
        MinEta = cms.double(-2.5),
        MinPhi = cms.double(-3.14159265359),
        MinPt = cms.double(99.99),
        PartID = cms.vint32(1000024)
    ),
    Verbosity = cms.untracked.int32(0),
    firstRun = cms.untracked.uint32(1),
    psethack = cms.string('chargino pt 100')
)


# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)

process.genParticlePlusGeant = cms.EDProducer("GenPlusSimParticleProducer",
					      src = cms.InputTag("g4SimHits"), # use "famosSimHits" for FAMOS
					      setStatus = cms.int32(8), # set status = 8 for GEANT GPs
					      filter = cms.vstring("pt > 0.0"), # just for testing (optional)
					      genParticles = cms.InputTag("genParticles") # original genParticle list
					      )
process.simulation_step = cms.Path(process.psim + process.genParticlePlusGeant)
process.RAWSIMoutput.outputCommands.extend( [
		"keep *_genParticlePlusGeant_*_*",
		] )

#process.simulation_step = cms.Path(process.psim)

process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)
# filter all path with the production filter sequence
for path in process.paths:
        getattr(process,path)._seq = process.generator * getattr(process,path)._seq 

if particleType == "chargino":
    process.generator.PGunParameters.PartID = cms.vint32(1000024) 
    process.generator.particleFile = cms.untracked.string('DisappTrks/SignalMC/data/geant4_AMSB_chargino_test.slha') 
elif particleType == "antichargino":
    process.generator.PGunParameters.PartID = cms.vint32(-1000024) 
    process.generator.particleFile = cms.untracked.string('DisappTrks/SignalMC/data/geant4_AMSB_chargino_test.slha') 
elif particleType == "stau":
    process.generator.PGunParameters.PartID = cms.vint32(1000015) 
    process.generator.particleFile = cms.untracked.string('Configuration/Generator/data/particles_stau_100_GeV.txt') 
elif particleType == "HIP2":
    process.generator.PGunParameters.PartID = cms.vint32(17) 
    process.generator.particleFile = cms.untracked.string('Configuration/Generator/data/particles_HIP3_stau_500_GeV.txt') 
elif particleType == "HIP6":
    process.generator.PGunParameters.PartID = cms.vint32(17) 
    process.generator.particleFile = cms.untracked.string('Configuration/Generator/data/particles_HIP6_stau_500_GeV.txt') 
elif particleType == "gluino":
    process.generator.PGunParameters.PartID = cms.vint32(1000021) 
    process.generator.particleFile = cms.untracked.string('Configuration/Generator/data/particles_gluino_500_GeV.txt') 
    process.generator.hscpFlavor = cms.untracked.string('gluino') 
elif particleType == "stop":
    process.generator.PGunParameters.PartID = cms.vint32(1000006) 
    process.generator.particleFile = cms.untracked.string('Configuration/Generator/data/particles_stop_500_GeV.txt') 
    process.generator.hscpFlavor = cms.untracked.string('stop') 
else:  
    print "ERROR:  Unrecognized particleType = ", particleType, " Will now exit." 
    sys.exit(0)  

from SimG4Core.CustomPhysics.Exotica_HSCP_SIM_cfi import customise
process = customise(process)

# process.MessageLogger = cms.Service("MessageLogger",
#                                     destinations = cms.untracked.vstring(
#                                             'detailedInfo'
#                                             ,'critical'
#                                             ,'cerr'
#                                     ),
#                                     debugModules = cms.untracked.vstring('CustomPhysics'),
#                                     critical = cms.untracked.PSet(
#                                             threshold = cms.untracked.string('ERROR')
#                                     ),
#                                     detailedInfo = cms.untracked.PSet(
#                                             threshold = cms.untracked.string('INFO')
#                                     ),
#                                     cerr = cms.untracked.PSet(
#                                             threshold = cms.untracked.string('WARNING')
#                                     )
#                             )

# Dump config file:
outfile = open('dumpedConfig_GEN_SIM.py','w'); print >> outfile,process.dumpPython(); outfile.close()



