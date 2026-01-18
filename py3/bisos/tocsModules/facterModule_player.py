# -*- coding: utf-8 -*-

""" #+begin_org
* ~[Summary]~ :: A =CS-Unit= as equivalent of facter in py and remotely with rpyc.
#+end_org """

####+BEGIN: b:py3:cs:file/dblockControls :classification "cs-u"
""" #+begin_org
* [[elisp:(org-cycle)][| /Control Parameters Of This File/ |]] :: dblk ctrls classifications=cs-u
#+BEGIN_SRC emacs-lisp
(setq-local b:dblockControls t) ; (setq-local b:dblockControls nil)
(put 'b:dblockControls 'py3:cs:Classification "cs-u") ; one of cs-mu, cs-u, cs-lib, bpf-lib, pyLibPure
#+END_SRC
#+RESULTS:
: cs-u
#+end_org """
####+END:

####+BEGIN: b:prog:file/proclamations :outLevel 1
""" #+begin_org
* *[[elisp:(org-cycle)][| Proclamations |]]* :: Libre-Halaal Software --- Part Of BISOS ---  Poly-COMEEGA Format.
** This is Libre-Halaal Software. © Neda Communications, Inc. Subject to AGPL.
** It is part of BISOS (ByStar Internet Services OS)
** Best read and edited  with Blee in Poly-COMEEGA (Polymode Colaborative Org-Mode Enhance Emacs Generalized Authorship)
#+end_org """
####+END:

####+BEGIN: b:prog:file/particulars :authors ("./inserts/authors-mb.org")
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars |]]* :: Authors, version
** This File: /bisos/git/bxRepos/bisos-pip/facter/py3/bisos/facter/facter_csu.py
** Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
#+end_org """
####+END:

####+BEGIN: b:py3:file/particulars-csInfo :status "inUse"
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars-csInfo |]]*
#+end_org """
import typing
csInfo: typing.Dict[str, typing.Any] = { 'moduleName': ['facter_csu'], }
csInfo['version'] = '202403270908'
csInfo['status']  = 'inUse'
csInfo['panel'] = 'facter_csu-Panel.org'
csInfo['groupingType'] = 'IcmGroupingType-pkged'
csInfo['cmndParts'] = 'IcmCmndParts[common] IcmCmndParts[param]'
####+END:

""" #+begin_org
* [[elisp:(org-cycle)][| ~Description~ |]] :: [[file:/bisos/git/auth/bxRepos/blee-binders/bisos-core/COMEEGA/_nodeBase_/fullUsagePanel-en.org][BISOS COMEEGA Panel]]
This a =Cs-Unit= for running the equivalent of facter in py and remotely with rpyc.
With BISOS, it is used in CMDB remotely.

** Relevant Panels:
** Status: In use with BISOS
** /[[elisp:(org-cycle)][| Planned Improvements |]]/ :
*** TODO complete fileName in particulars.
#+end_org """

####+BEGIN: b:prog:file/orgTopControls :outLevel 1
""" #+begin_org
* [[elisp:(org-cycle)][| Controls |]] :: [[elisp:(delete-other-windows)][(1)]] | [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[file:Panel.org][Panel]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
** /Version Control/ ::  [[elisp:(call-interactively (quote cvs-update))][cvs-update]]  [[elisp:(vc-update)][vc-update]] | [[elisp:(bx:org:agenda:this-file-otherWin)][Agenda-List]]  [[elisp:(bx:org:todo:this-file-otherWin)][ToDo-List]]

#+end_org """
####+END:

####+BEGIN: b:py3:file/workbench :outLevel 1
""" #+begin_org
* [[elisp:(org-cycle)][| Workbench |]] :: [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pyclbr %s" (bx:buf-fname))))][pyclbr]] || [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pydoc ./%s" (bx:buf-fname))))][pydoc]] || [[elisp:(python-check (format "/bisos/pipx/bin/pyflakes %s" (bx:buf-fname)))][pyflakes]] | [[elisp:(python-check (format "/bisos/pipx/bin/pychecker %s" (bx:buf-fname))))][pychecker (executes)]] | [[elisp:(python-check (format "/bisos/pipx/bin/pycodestyle %s" (bx:buf-fname))))][pycodestyle]] | [[elisp:(python-check (format "/bisos/pipx/bin/flake8 %s" (bx:buf-fname))))][flake8]] | [[elisp:(python-check (format "/bisos/pipx/bin/pylint %s" (bx:buf-fname))))][pylint]]  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: b:py3:cs:orgItem/basic :type "=PyImports= "  :title "*Py Library IMPORTS*" :comment "-- Framework and External Packages Imports"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =PyImports=  [[elisp:(outline-show-subtree+toggle)][||]] *Py Library IMPORTS* -- Framework and External Packages Imports  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

# import os
import collections
# import pathlib
# import invoke

####+BEGIN: b:py3:cs:framework/imports :basedOn "classification"
""" #+begin_org
** Imports Based On Classification=cs-u
#+end_org """
from bisos import b
from bisos.b import cs
from bisos.b import b_io
from bisos.common import csParam

import collections
####+END:

import pathlib

from bisos.uploadAsCs import uploadAsCs_csu
from bisos.uploadAsCs import abstractLoader

from bisos.csPlayer import csxuFps_csu

from bisos.b import cmndsSeed
import logging
log = logging.getLogger(__name__)

####+BEGIN: b:py3:cs:orgItem/basic :type "=Executes=  "  :title "CSU-Lib Executions" :comment "-- cs.invOutcomeReportControl"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =Executes=   [[elisp:(outline-show-subtree+toggle)][||]] CSU-Lib Executions -- cs.invOutcomeReportControl  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: b:py3:cs:orgItem/section :title "Common Parameters Specification" :comment "based on cs.param.CmndParamDict -- As expected from CSU-s"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    [[elisp:(outline-show-subtree+toggle)][||]] *Common Parameters Specification* based on cs.param.CmndParamDict -- As expected from CSU-s  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: b:py3:cs:func/typing :funcName "commonParamsSpecify" :comment "~CSU Specification~" :funcType "ParSpc" :deco ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-ParSpc [[elisp:(outline-show-subtree+toggle)][||]] /commonParamsSpecify/  ~CSU Specification~  [[elisp:(org-cycle)][| ]]
#+end_org """
def commonParamsSpecify(
####+END:
        csParams: cs.param.CmndParamDict,
) -> None:
    return


####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "Direct Command Services" :anchor ""  :extraInfo "Examples and CSs"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _Direct Command Services_: |]]  Examples and CSs  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "examples_csu" :comment "" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<examples_csu>>  =verify= ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class examples_csu(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Basic example command.
        #+end_org """)

        od = collections.OrderedDict
        cmnd = cs.examples.cmndEnter
        literal = cs.examples.execInsert

        csxuFpsBase = "/bisos/var/tocsModules"
        csxuName = cs.G.icmMyName()
        csxuDerivedBase = f"/bisos/var/tocsModules/{csxuName}/derived"

        pyDictResultPath = f"inSchemaDict.py"
        graphvizResultPath = f"graphviz.pdf"
        cliCompgenResultPath = f"cliCompgen.sh"

        csxuFpsBasePars = od([('csxuFpsBasePath', csxuFpsBase),])
        csxuNamePars = od([('csxuName', csxuName),])
        csxuDerivedBasePars = od([('csxuDerivedBasePath', csxuDerivedBase),])

        pyDictResultPathPars = od([('pyDictResultPath', pyDictResultPath),])
        graphvizResultPathPars = od([('graphvizResultPath', graphvizResultPath),])
        cliCompgenResultPathPars = od([('cliCompgenResultPath', cliCompgenResultPath),])

        # csxuAllPars = od(list(csxuFpsBasePars.items()) + list(csxuNamePars.items()) + list(pyDictResultPathPars.items()) + list(graphvizResultPathPars.items()))
        csxuAllPars = od(list(csxuFpsBasePars.items()) + list(csxuNamePars.items()) + list(csxuDerivedBasePars.items()))

        csxuPyDictPars = od(list(csxuFpsBasePars.items()) + list(csxuNamePars.items()) + list(pyDictResultPathPars.items()))

        cs.examples.menuChapter('=CSLMXU FPs Create=')

        cmnd('csxuInSchema', args=csxuFpsBase)

        cs.examples.menuChapter('=CSLMU FPs to Py Dictionary and Graphviz=')

        #cmnd('csxuFpsToPyDict', pars=csxuPyDictPars)
        cmnd('csxuFpsToPyDict', pars=csxuAllPars)
        cmnd('csxuFpsToGraphviz', pars=csxuAllPars)
        cmnd('inSchema', pars=csxuFpsBasePars,  args="pdf-emacs")
        cmnd('csxuFpsToCliCompgen', pars=csxuAllPars)
        # cmnd('csxuFpsToGraphvizShow', pars=csxuNameAndFpsBasePars)

        # cs.examples.menuSection('/factNameGetattr/')
        # literal("facter networking")

        return(cmndOutcome)


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "cslmxuPlayerMenuExamples" :comment "" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<cslmxuPlayerMenuExamples>>  =verify= ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class cslmxuPlayerMenuExamples(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Basic example command.
        #+end_org """)

        od = collections.OrderedDict

        csxuFpsBase = "/bisos/var/tocsModules"
        csxuFpsBasePars = od([('csxuFpsBasePath', csxuFpsBase),])

        cs.examples.menuChapter('=TocsModules CSLMXUPlayer Examples=')

        cs.examples.cmndEnter('inSchema', pars=csxuFpsBasePars, args="pdf-emacs")
        cs.examples.cmndEnter('moduleInSchema', pars=csxuFpsBasePars, args="pdf-emacs")
        cs.examples.cmndEnter('cslmxuPlayerMenu')

        return(cmndOutcome)


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "cslmxuPlayerMenu" :comment "" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<cslmxuPlayerMenu>>  =verify= ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class cslmxuPlayerMenu(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Basic example command.
        #+end_org """)

        examples_csu().pyCmnd()

        return(cmndOutcome)


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "examplesFacter_csu" :comment "" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv "pyKwArgs"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<examplesFacter_csu>>  =verify= ro=cli pyInv=pyKwArgs   [[elisp:(org-cycle)][| ]]
#+end_org """
class examplesFacter_csu(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             pyKwArgs: typing.Any=None,   # pyInv Argument
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Basic example command.
        #+end_org """)

        self.captureRunStr(""" #+begin_org
*** Run Results
#+begin_src sh :results output :session shared
facterModule.cs -i examples 
  #+end_src
#+RESULTS:

        #+end_org """)

        od = collections.OrderedDict
        cmnd = cs.examples.cmndEnter
        literal = cs.examples.execInsert

        #  -v 1 --callTrackings monitor+ --callTrackings invoke+
        pars_debug_verbosity = od([('verbosity', "1"),])
        pars_debug_monitor = od([('callTrackings', "monitor+"),])
        pars_debug_invoke = od([('callTrackings', "invoke+"),])
        pars_debug_full = (pars_debug_verbosity | pars_debug_monitor | pars_debug_invoke)

        pars_cluster_default = od([('cluster', "default"),])

        # cmnd('targetRun', csName=csName, pars=(pars_debug_full |pars_upload), comment=f"""# DEBUG Small Batch""",)

        uploadPath = "MISSING"

        oneModuleBaseDir = "/bisos/core/tocsModules/facter/sample/"
        oneRunBaseDir = "/bisos/site/tocsModules/facter/sample/"

        if pyKwArgs:
            if pyKwArgs.get('uploadPath'):
                uploadPath =  pyKwArgs['uploadPath']
                uploadPath = str(pathlib.Path(uploadPath).expanduser().resolve())
            else:
                uploadPath = pathlib.Path(oneModuleBaseDir) / "facterModuleSample.py"
        else:
            uploadPath = pathlib.Path(oneModuleBaseDir) / "facterModuleSample.py"


        # Use an absolute path for upload to avoid relative-path surprises

        uploadPars = od([('upload', uploadPath)])

        oneModuleBaseDir = "/bisos/core/tocsModules/facter/sample/"
        oneRunBaseDir = "/bisos/site/tocsModules/facter/sample/"

        oneTargetFile = pathlib.Path(oneRunBaseDir) / "targets/examples.tgt"
        # targetPathAbs = str(pathlib.Path(oneTargetFile).expanduser().resolve())

        targetsFilePars = od([('upload', uploadPath),('targetsFile', oneTargetFile) ])

        cs.examples.menuChapter('=CSMU:: Facter Module  Commands=')


        cs.examples.menuSection('=CSMU:: Facter Module  Parameters=')

        cmnd('uploadedCsParams', pars=(uploadPars),)
        cmnd('uploadedSummary', pars=(uploadPars),)

        cmnd('moduleFpsInSchema', pars=(uploadPars),)
        cmnd('moduleFps', pars=(uploadPars), args="generic",)


        cs.examples.menuSection('=CSMU:: Cluster Run=')

        cmnd('clusterRun', pars=(uploadPars),)


        # literal("facter networking.interfaces.lo.bindings[0].address  # Fails, you can't do that")

        return(cmndOutcome)



####+BEGIN: b:py3:cs:framework/endOfFile :basedOn "classification"
""" #+begin_org
* [[elisp:(org-cycle)][| *End-Of-Editable-Text* |]] :: emacs and org variables and control parameters
#+end_org """

#+STARTUP: showall

### local variables:
### no-byte-compile: t
### end:
####+END:
