import os, time
from ctypes import *

if os.name == "nt":
    IQMEASURE_PATH = r'C:\Litepoint\IQmeasure\IQmeasure_x64_4.0.5.5\bin'
else:
    IQMEASURE_PATH = os.path.dirname(os.path.realpath(__file__))

MAX_BUFFER_SIZE = 12*4096
testerIP = "192.168.100.242"

def enum(*args):
    enums = dict(zip(args, range(len(args))))
    return type('Enum', (), enums)

IQMEASURE_ERROR_CODES = enum(
    'ERR_OK',
    'ERR_NO_CONNECTION',
    'ERR_NOT_INITIALIZED',
    'ERR_SAVE_WAVE_FAILED',
    'ERR_LOAD_WAVE_FAILED',
    'ERR_SET_TX_FAILED',
    'ERR_SET_WAVE_FAILED',
    'ERR_SET_RX_FAILED',
    'ERR_CAPTURE_FAILED',
    'ERR_NO_CAPTURE_DATA',
    'ERR_VSA_NUM_OUT_OF_RANGE',
    'ERR_ANALYSIS_FAILED',
    'ERR_NO_VALID_ANALYSIS',
    'ERR_VSG_PORT_IS_OFF',
    'ERR_NO_MOD_FILE_LOADED',
    'ERR_NO_CONT_FOR_MULTI_SEGMENT',
    'ERR_MEASUREMENT_NAME_NOT_FOUND',
    'ERR_INVALID_ANALYSIS_TYPE',
    'ERR_NO_ANALYSIS_RESULT_AVAILABLE',
    'ERR_NO_MEASUREMENT_RESULT',
    'ERR_INVALID_IP_ADDRESS',
    'ERR_GENERAL_ERR',
    'ERR_TX_NOT_DONE',
    'ERR_SET_TOKEN_FAILED',
    'ERR_TOKEN_RETRIEVAL_TIMEDOUT',
    'ERR_GET_TOKEN_FAILED',
    'ERR_INVALID_CAPTURE_INDEX',
    'ERR_VSG_POWER_EXCEED_LIMIT',
    'ERR_ANALYSIS_NULL_POINTER',
    'ERR_ANALYSIS_UNSUPPORTED_PARAM_NAME',
    'ERR_ANALYSIS_INVALID_PARAM_VALUE',
    'ERR_INVALID_DATA_CAPTURE_RANGE',
    'ERR_DATARATE_DOES_NOT_EXIST',
    'ERR_BUFFER_OVERFLOW',
    'ERR_SET_PATH_NOT_DONE',
    'ERR_DPD_TABLE_NON_EXISTENT',
    # FM Error Codes
    'ERR_FM_NOT_INITIALIZED',
    'ERR_FM_SET_TX_FAILED',
    'ERR_FM_GET_TX_FAILED',
    'ERR_FM_SET_AUDIO_TONE_FAILED',
    'ERR_FM_GET_AUDIO_TONE_FAILED',
    'ERR_FM_NO_CAPTURE_DATA',
    'ERR_FM_VSA_CAPTURE_FAILED',
    'ERR_FM_SET_RX_FAILED',
    'ERR_FM_GET_RX_FAILED',
    'ERR_FM_ANALYSIS_FAILED',
    'ERR_FM_CAPTURE_AUDIO_FAILED',
    'ERR_FM_GENERATE_AUDIO_FAILED',
    'ERR_FM_QUERY_AIM_FAILED',
    'ERR_FM_SAVE_WAV_AUDIO_FAILED',
    'ERR_FM_PLAY_AUDIO_FAILED',
    'ERR_FM_LOAD_AUDIO_FAILED',
    'ERR_FM_STOP_AUDIO_PLAY_FAILED',
    'ERR_GPS',
    'ERR_SET_MULTI_THREAD_FAILED',
    'ERR_UNKNOWN_TESTER_TYPE',
    'ERR_WRONG_TESTER_TYPE',
    'ERR_INVALID_TESTER_CONTROL',  # Tester control method not valid (SCPI', IQAPI', ...)
    'ERR_NO_RESPONSE_FROM_TESTER',

    'ERR_MPTA_NOT_ENABLE',
    'ERR_MPTA_NOT_DISENABLE',
    'ERR_MPTA_SET_TXRX',
    'ERR_MPTA_CAPTURE_FAILED',

    # Add
    'ERR_INVALID_TEST_TYPE',
    'ERR_INVALID_SEQUENCE_NUM',
    'ERR_TX_RX_FREQ_NOT_EQUAL',
    'ERR_INVALID_RF_PORT_SETTING',
    'ERR_INVALID_PACKET_COUNT',
    'ERR_NOT_SUPPORTED_RF_MODE',
    'ERR_EMPTY_WAVEFORM_NAME',
    'ERR_ZERO_WAVEFROM_SIZE',
    'ERR_NOT_DEFINED_CHANGE_DIRECTION_TIME',
    'ERR_WRONG_EXEC_PARAM_SIZE',
    'ERR_INVALID_PACKET_TYPE',
    'ERR_INVALID_MODULATION',
    'ERR_NOT_ENOUGH_RETURN_ACK',
    'ERR_INVALID_PARAM_SETTING',
    'ERR_UNKNOWN',
    'ERR_FUNCTION_NOT_SUPPORTED',
    'ERR_VSG_TRANSMIT_PKT_NOT_FINISHED',
    'ERR_SET_VSG_POWER_STATE_FAILED',
    'ERR_VSG_PLAY_WAVE_FAILED',
    'ERR_WAVEFORM_NOT_EXISTED_IN_TESTER',
    'ERR_INVALID_HANDLE',
    'ERR_CANNOT_FIND_TESTER_FOLDER',
    'ERR_WAVEFORM_NOT_FOUND',
    'ERR_SET_VSA_VSG_SEPARATION_FAILED',
    'ERR_NO_VALUE_DEFINED',
    'ERR_WRONG_SCPI_RETURN_SIZE',
    'ERR_NAV_ACTIVATE_FAILED',
    'ERR_NAV_DEACTIVATE_FAILED',
    'ERR_NAV_SET_CONTINUE_WAVE_FAILED',
    'ERR_NAV_SET_MODULATE_MODE_FAILED',
    'ERR_NAV_SET_TIME_OF_WEEK_FAILED',
    'ERR_NAV_SET_GLONASS_CHANNEL_FAILED',
    'ERR_NAV_SET_POWER_FAILED',
    'ERR_NAV_LOAD_SCENARIO_FILE_FAILED',
    'ERR_NAV_PLAY_SCENARIO_FILE_FAILED',
    'ERR_INVALID_FREQ_BAND',
    'ERR_OPEN_FILE_FAILD',
    'ERR_NOT_SUPPORTED_TECHNOLOGY',
    'ERR_WAVE_GEN_FAILED',
    'ERR_TBT_CAL_FAILED',

    # IQlink
    'ERR_IQLINK_DISASSOCIATE_FAILED',
    'ERR_IQLINK_SET_TCP_FAILED',
    'ERR_IQLINK_SET_UDP_FAILED',
    'ERR_IQLINK_SET_AP_FAILED',
    'ERR_IQLINK_SET_AP_OUT_OF_RANGE',
    'ERR_IQLINK_UPLINK_FAILED',
    'ERR_IQLINK_DOWNLINK_FAILED',
    'ERR_IQLINK_PER_FAILED',
    'ERR_IQLINK_PORT_ENABLE_FAILED',
    'ERR_IQLINK_SET_PATH_LOSS_FAILED',
    'ERR_IQLINK_SET_IPERF_FAILED',
    'ERR_IQLINK_TX_POWER_FAILED',
    'ERR_IQLINK_SET_RXPER_ACK_FAILED',
    'ERR_IQLINK_SET_DUT_AP_FAILED',
    'ERR_IQLINK_DUT_NOT_CONNECTED',
    # MVSA/GALL module define error
    'ERR_MODULE_DEF_NOT_SUPPORTED',

    'ERR_THREAD_CONTEXT_ALLOCATION_FAILED',
    'ERR_THREAD_CONTEXT_ALLOCATED_ALREADY',

    'ERR_INIT_GLOBAL_DATA_FAILED',
    'ERR_NO_LICENSE_INSTALLED',
    'ERR_MEMORY_ALLOCATION_FAILED',
    'ERR_UNINSTALL_LIBRARY_FAILED',
    'ERR_WRONG_INSTALLED_LIBRARY_VERS',
    'ERR_SEQ_BUILDER_NOT_INITIALIZED',
    'ERR_SET_BP_ROSC_FAILED',
    'ERR_SET_RFD_FAILED',
    # UWB error code
    'ERR_UWB_ALIGN_FAILED',

    'ERR_MAX_ERR_CODE_NUMBER'
)

class IQxel:
    def __init__(self, IQmeasure_path=""):
        if IQmeasure_path == "":
            IQmeasure_path = IQMEASURE_PATH
        os.chdir(IQmeasure_path)
        if os.name == "nt":
            self.IQmeasureDll = CDLL(os.path.join(IQmeasure_path, 'IQmeasure.dll'))
        else:
            self.IQmeasureDll = CDLL(os.path.join(IQmeasure_path, 'libIQmeasure.so'))

    def CreateResults(self, errCode, resultDict=None):
        if errCode != 0:
            errorStr = self.LP_GetErrorString(errCode)
            if errCode != IQMEASURE_ERROR_CODES.ERR_TX_NOT_DONE:
                # print("Error", errorStr)
                pass
            return {'err': errCode, 'errDesc': errorStr, 'output': None}
        else:
            return {'err': 0, 'errDesc': 'N/A', 'output': resultDict}

    def LP_GetErrorString(self, err):
        """
        Get the detailed error message for the specific error code
        """
        func = self.IQmeasureDll.LP_GetErrorString
        func.argtypes = [c_int]
        func.restype = c_char_p
        return func(err)

    def LP_Init(self, IQType=1, testerControlMethod=1):
        """
        Initializes the MATLAB environment for running IQmeasure.

        Parameters
        [in]	IQtype	Pointer to IQ tester type. IQXel or IQ legacy testers. It decides what dll to link.
        [in]	testerControlMethod	indicates what method is used to control LP tester: 0 = IQapi, 1 = SCPI command

        Returns
        0 if MATLAB initialized OK; non-zero indicates MATLAB failed to initialize.
        """
        func = self.IQmeasureDll.LP_Init
        func.restype = c_int
        ret = func(c_int(IQType), c_int(testerControlMethod))
        return self.CreateResults(ret)

    def LP_Term(self):
        func = self.IQmeasureDll.LP_Term
        func.restype = c_int
        return self.CreateResults(func())

    def LP_SetVsgModulation(self, modFileName, loadInternalWaveform=0):
        """
        0: pc
        1: tester
        """
        func = self.IQmeasureDll.LP_SetVsgModulation
        func.argtypes = [c_char_p, c_int]
        func.restype = c_int
        return self.CreateResults(func(modFileName.encode('utf-8'), loadInternalWaveform))

    def LP_EnableVsgRF(self, enabled):
        func = self.IQmeasureDll.LP_EnableVsgRF
        func.argtypes = [c_int]
        func.restype = c_int
        return self.CreateResults(func(enabled))

    def LP_SetFrameCnt(self, frameCnt):
        func = self.IQmeasureDll.LP_SetFrameCnt
        func.argtypes = [c_int]
        func.restype = c_int
        return self.CreateResults(func(frameCnt))

    def LP_SetVsa(self, rfFreqHz, rfAmplDb, port, extAttenDb=0, triggerLevelDb=-25,
                  triggerPreTime=10e-6, dFreqShiftHz=0.0, dTriggerGapTime=6e-6):
        """
        Sets up VSA for data capturing.

        Parameters
        [in]	rfFreqHz	The center frequency of VSA (Hz). Set real center frequency for 160MHz contiguous signal. Set center frequency of the first 80MHz for 80+80 signal.
        [in]	rfAmplDb	The amplitude of the peak power (dBm) for VSA to work with
        [in]	port	The port to which the VSG connects, with the following options:
        =1: OFF
        =2: RF port 1 (RF1)
        =3: RF port 2 (RF2)
        =4: RF port 3 (RF3)
        =5: RF port 4 (RF4)
        [in]	extAttenDb	The external attenuation (dB). Set to 0 always.
        [in]	triggerLevelDb	The trigger level (dBm) used for signal trigger (ignored in Free-run and External Trigger Modes)
        [in]	triggerPreTime	The pre-trigger time used for signal capture
        [in]	dFreqShiftHz	Frequency Shift
        Returns
        ERR_OK if no errors; otherwise call LP_GetErrorString() for detailed error message.
        """
        func = self.IQmeasureDll.LP_SetVsa
        ret = func(c_double(rfFreqHz), c_double(rfAmplDb), c_int(port), c_double(extAttenDb),
                   c_double(triggerLevelDb), c_double(triggerPreTime), c_double(dFreqShiftHz),
                   c_double(dTriggerGapTime))
        return self.CreateResults(ret)

    def LP_SetVsg(self, rfFreqHz, rfPowerLeveldBm, port, setGapPowerOff=True, dFreqShiftHz=0.0):
        """
        Sets up VSG.

        Parameters
        [in]	rfFreqHz	The center frequency of VSG (Hz). Set real center frequency for 160MHz contiguous signal. Set center frequency of the first 80MHz for 80+80 signal.
        [in]	rfPowerLeveldBm	The output power level of VSG (dBm)
        [in]	port	The port to which the VSG connects, with the following options:
                            =1: OFF
                            =2: RF port 1 (RF1)
                            =3: RF port 2 (RF2)
                            =4: RF port 3 (RF3)
                            =5: RF port 4 (RF4)
        [in]	setGapPowerOff
        =true: Turn off RF power in the gap between packets
        =false: Does not turn off RF power in the gap between packets
        [in]	dFreqShiftHz	Frequency Shift

        Returns
        ERR_OK if no errors; otherwise call LP_GetErrorString() for detailed error message.
        """
        func = self.IQmeasureDll.LP_SetVsg
        func.restype = c_int
        ret = func(c_double(rfFreqHz), c_double(rfPowerLeveldBm), c_int(port), c_bool(setGapPowerOff),
                   c_double(dFreqShiftHz))
        return self.CreateResults(ret)

    def LP_ScpiCommandSet(self, scpiCommand):
        func = self.IQmeasureDll.LP_ScpiCommandSet
        func.argtypes = [c_char_p]
        func.restype = c_int
        ret = func(scpiCommand.encode('utf-8'))
        return self.CreateResults(ret)

    def LP_ScpiCommandQuery(self, query, max_size=MAX_BUFFER_SIZE):
        response = create_string_buffer(max_size)
        actual_size = c_uint()
        func = self.IQmeasureDll.LP_ScpiCommandQuery
        func.argtypes = [c_char_p, c_uint, c_char_p, POINTER(c_uint)]
        func.restype = c_int
        ret = func(query.encode('utf-8'), max_size, response, byref(actual_size))
        return self.CreateResults(ret, response.value.decode('utf-8'))

    def LP_InitTesterN(self, ipAddresses, numOfTesters=1):
        """
        Initialize Testers.

        Parameters
        [in]	ipAddresses	The IP addresses of the testers to be connected
        [in]	numOfTesters	The number of testers to be connected
        [out]	num_mods_per_ip	The total number of available modules per IP(tester).

        Returns
        ERR_OK if the tester has been successfully initialized; otherwise call LP_GetErrorString() for detailed error message.
        """
        num_mods_per_ip = c_int()
        func = self.IQmeasureDll.LP_InitTesterN
        func.argtypes = [c_char_p, c_int, POINTER(c_int)]
        func.restype = c_int
        ret = func(ipAddresses.encode('utf-8'), numOfTesters, byref(num_mods_per_ip))
        return self.CreateResults(ret, {'NumberOfModulePerIP': num_mods_per_ip.value})

    def LP_SetTesterMode(self, signalMode, selectedModules, numOfSelectedModules):
        """
        Configure testers based on different signal modes.

        Parameters
        param1 [in]	signalMode:	The incoming/outgoing singal mode
        param2 [in]	selectedModules:	The selected modules array with specified module index in the module group
        param3 [in]	numOfSelectedModules:	The number of selected modules

        Return:
        ERR_OK if the tester has been successfully initialized; otherwise call LP_GetErrorString() for detailed error message.
        """
        func = self.IQmeasureDll.LP_SetTesterMode
        ret = func(c_int(signalMode), byref(c_int(selectedModules)), c_int(numOfSelectedModules))
        return self.CreateResults(ret)

    def module1(self):
        self.LP_Init()
        self.LP_InitTesterN(testerIP, 1)
        self.LP_SetTesterMode(0, [1], 1)  # RF1A
        self.LP_SetVsa(5180e6, 10, 2)  # VSA
        time.sleep(10)

    def module2(self):
        self.LP_Init()
        self.LP_InitTesterN(testerIP, 1)
        self.LP_SetTesterMode(0, [2], 1)  # RF1B
        self.LP_SetVsgModulation('user/mcs7.iqvsg', 1)
        self.LP_SetVsg(2412e6, -10, 2)
        self.LP_SetFrameCnt(1000)
        time.sleep(10)


if __name__ == '__main__':
    iqxel = IQxel()
    iqxel.module1()