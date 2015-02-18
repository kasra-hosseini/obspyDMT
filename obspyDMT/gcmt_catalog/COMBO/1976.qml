<?xml version='1.0' encoding='utf-8'?>
<q:quakeml xmlns:q="http://quakeml.org/xmlns/quakeml/1.2" xmlns="http://quakeml.org/xmlns/bed/1.2">
  <eventParameters publicID="smi:local/86a6734d-cf97-4dec-b539-cabf7c6ae5a9">
    <event publicID="smi:local/ndk/M010176A/event">
      <preferredOriginID>smi:local/ndk/M010176A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/M010176A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/M010176A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>KERMADEC ISLANDS REGION</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>M010176A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/M010176A/origin#reforigin">
        <time>
          <value>1976-01-01T01:29:39.600000Z</value>
        </time>
        <latitude>
          <value>-28.61</value>
        </latitude>
        <longitude>
          <value>-177.64</value>
        </longitude>
        <depth>
          <value>59000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/M010176A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/M010176A/origin#cmtorigin">
        <time>
          <value>1976-01-01T01:29:53.400000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>-29.25</value>
          <uncertainty>0.02</uncertainty>
        </latitude>
        <longitude>
          <value>-176.96</value>
          <uncertainty>0.01</uncertainty>
        </longitude>
        <depth>
          <value>47800.0</value>
          <uncertainty>600.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/M010176A/magnitude#moment_mag">
        <mag>
          <value>7.25</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/M010176A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/M010176A/magnitude#mb">
        <mag>
          <value>6.2</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/M010176A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/M010176A/magnitude#MS">
        <mag>
          <value>0.0</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/M010176A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/M010176A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>202.0</value>
            </strike>
            <dip>
              <value>30.0</value>
            </dip>
            <rake>
              <value>93.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>18.0</value>
            </strike>
            <dip>
              <value>60.0</value>
            </dip>
            <rake>
              <value>88.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>283.0</value>
            </azimuth>
            <plunge>
              <value>75.0</value>
            </plunge>
            <length>
              <value>8.94e+19</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>110.0</value>
            </azimuth>
            <plunge>
              <value>15.0</value>
            </plunge>
            <length>
              <value>-1.019e+20</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>19.0</value>
            </azimuth>
            <plunge>
              <value>2.0</value>
            </plunge>
            <length>
              <value>1.26e+19</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/M010176A/momenttensor">
          <derivedOriginID>smi:local/ndk/M010176A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>12</stationCount>
            <componentCount>30</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>9.56e+19</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>7.68e+19</value>
              <uncertainty>9e+17</uncertainty>
            </Mrr>
            <Mtt>
              <value>9e+17</value>
              <uncertainty>6e+17</uncertainty>
            </Mtt>
            <Mpp>
              <value>-7.77e+19</value>
              <uncertainty>7e+17</uncertainty>
            </Mpp>
            <Mrt>
              <value>1.39e+19</value>
              <uncertainty>1.6e+18</uncertainty>
            </Mrt>
            <Mrp>
              <value>4.52e+19</value>
              <uncertainty>1.6e+18</uncertainty>
            </Mrp>
            <Mtp>
              <value>-3.26e+19</value>
              <uncertainty>6e+17</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>18.8</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/M010176A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/M010176A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C010576A/event">
      <preferredOriginID>smi:local/ndk/C010576A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C010576A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C010576A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>CENTRAL PERU</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C010576A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C010576A/origin#reforigin">
        <time>
          <value>1976-01-05T02:31:36.300000Z</value>
        </time>
        <latitude>
          <value>-13.29</value>
        </latitude>
        <longitude>
          <value>-74.9</value>
        </longitude>
        <depth>
          <value>95000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C010576A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C010576A/origin#cmtorigin">
        <time>
          <value>1976-01-05T02:31:44.700000Z</value>
          <uncertainty>0.4</uncertainty>
        </time>
        <latitude>
          <value>-13.42</value>
          <uncertainty>0.07</uncertainty>
        </latitude>
        <longitude>
          <value>-75.14</value>
          <uncertainty>0.06</uncertainty>
        </longitude>
        <depth>
          <value>85400.0</value>
          <uncertainty>3200.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C010576A/magnitude#moment_mag">
        <mag>
          <value>5.65</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C010576A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C010576A/magnitude#mb">
        <mag>
          <value>6.0</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C010576A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C010576A/magnitude#MS">
        <mag>
          <value>0.0</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C010576A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C010576A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>350.0</value>
            </strike>
            <dip>
              <value>28.0</value>
            </dip>
            <rake>
              <value>-60.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>137.0</value>
            </strike>
            <dip>
              <value>66.0</value>
            </dip>
            <rake>
              <value>-105.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>238.0</value>
            </azimuth>
            <plunge>
              <value>19.0</value>
            </plunge>
            <length>
              <value>4.97e+17</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>20.0</value>
            </azimuth>
            <plunge>
              <value>66.0</value>
            </plunge>
            <length>
              <value>-2.62e+17</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>143.0</value>
            </azimuth>
            <plunge>
              <value>14.0</value>
            </plunge>
            <length>
              <value>-2.35e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C010576A/momenttensor">
          <derivedOriginID>smi:local/ndk/C010576A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>6</stationCount>
            <componentCount>14</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>5</stationCount>
            <componentCount>8</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>3.79e+17</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>-1.78e+17</value>
              <uncertainty>2.1e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>-5.9e+16</value>
              <uncertainty>2.8e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>2.37e+17</value>
              <uncertainty>2.8e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>-1.28e+17</value>
              <uncertainty>1.5e+16</uncertainty>
            </Mrt>
            <Mrp>
              <value>1.97e+17</value>
              <uncertainty>1.5e+16</uncertainty>
            </Mrp>
            <Mtp>
              <value>-2.9e+17</value>
              <uncertainty>2.2e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>3.2</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C010576A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C010576A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C010676A/event">
      <preferredOriginID>smi:local/ndk/C010676A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C010676A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C010676A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>OFF EAST COAST OF KAMCHATKA</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C010676A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C010676A/origin#reforigin">
        <time>
          <value>1976-01-06T21:08:19.300000Z</value>
        </time>
        <latitude>
          <value>51.6</value>
        </latitude>
        <longitude>
          <value>159.33</value>
        </longitude>
        <depth>
          <value>33000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C010676A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C010676A/origin#cmtorigin">
        <time>
          <value>1976-01-06T21:08:25.100000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>51.45</value>
          <uncertainty>0.02</uncertainty>
        </latitude>
        <longitude>
          <value>159.5</value>
          <uncertainty>0.03</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C010676A/magnitude#moment_mag">
        <mag>
          <value>6.13</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C010676A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C010676A/magnitude#mb">
        <mag>
          <value>5.7</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C010676A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C010676A/magnitude#MS">
        <mag>
          <value>6.0</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C010676A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C010676A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>206.0</value>
            </strike>
            <dip>
              <value>18.0</value>
            </dip>
            <rake>
              <value>78.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>39.0</value>
            </strike>
            <dip>
              <value>73.0</value>
            </dip>
            <rake>
              <value>94.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>315.0</value>
            </azimuth>
            <plunge>
              <value>62.0</value>
            </plunge>
            <length>
              <value>1.95e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>126.0</value>
            </azimuth>
            <plunge>
              <value>27.0</value>
            </plunge>
            <length>
              <value>-2e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>218.0</value>
            </azimuth>
            <plunge>
              <value>4.0</value>
            </plunge>
            <length>
              <value>5e+16</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C010676A/momenttensor">
          <derivedOriginID>smi:local/ndk/C010676A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>9</stationCount>
            <componentCount>27</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>9</stationCount>
            <componentCount>19</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>1.98e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>1.1e+18</value>
              <uncertainty>2e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>-3e+17</value>
              <uncertainty>2e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>-8e+17</value>
              <uncertainty>2e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>1.05e+18</value>
              <uncertainty>7e+16</uncertainty>
            </Mrt>
            <Mrp>
              <value>1.24e+18</value>
              <uncertainty>8e+16</uncertainty>
            </Mrp>
            <Mtp>
              <value>-5.6e+17</value>
              <uncertainty>2e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>5.6</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C010676A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C010676A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C010976A/event">
      <preferredOriginID>smi:local/ndk/C010976A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C010976A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C010976A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>VANUATU ISLANDS</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C010976A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C010976A/origin#reforigin">
        <time>
          <value>1976-01-09T23:54:35.600000Z</value>
        </time>
        <latitude>
          <value>-15.76</value>
        </latitude>
        <longitude>
          <value>167.87</value>
        </longitude>
        <depth>
          <value>168000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C010976A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C010976A/origin#cmtorigin">
        <time>
          <value>1976-01-09T23:54:40.100000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>-15.97</value>
          <uncertainty>0.02</uncertainty>
        </latitude>
        <longitude>
          <value>167.81</value>
          <uncertainty>0.02</uncertainty>
        </longitude>
        <depth>
          <value>173700.0</value>
          <uncertainty>800.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C010976A/magnitude#moment_mag">
        <mag>
          <value>6.31</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C010976A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C010976A/magnitude#mb">
        <mag>
          <value>6.1</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C010976A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C010976A/magnitude#MS">
        <mag>
          <value>0.0</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C010976A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C010976A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>246.0</value>
            </strike>
            <dip>
              <value>22.0</value>
            </dip>
            <rake>
              <value>-86.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>62.0</value>
            </strike>
            <dip>
              <value>68.0</value>
            </dip>
            <rake>
              <value>-91.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>153.0</value>
            </azimuth>
            <plunge>
              <value>23.0</value>
            </plunge>
            <length>
              <value>4.45e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>329.0</value>
            </azimuth>
            <plunge>
              <value>67.0</value>
            </plunge>
            <length>
              <value>-2.83e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>62.0</value>
            </azimuth>
            <plunge>
              <value>1.0</value>
            </plunge>
            <length>
              <value>-1.62e+18</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C010976A/momenttensor">
          <derivedOriginID>smi:local/ndk/C010976A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>10</stationCount>
            <componentCount>28</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>13</stationCount>
            <componentCount>26</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>3.64e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>-1.7e+18</value>
              <uncertainty>4e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>2.29e+18</value>
              <uncertainty>5e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>-5.9e+17</value>
              <uncertainty>5e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>-2.33e+18</value>
              <uncertainty>4e+16</uncertainty>
            </Mrt>
            <Mrp>
              <value>-1.23e+18</value>
              <uncertainty>3e+16</uncertainty>
            </Mrp>
            <Mtp>
              <value>2.01e+18</value>
              <uncertainty>5e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>7.0</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C010976A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C010976A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C011376A/event">
      <preferredOriginID>smi:local/ndk/C011376A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C011376A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C011376A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>ICELAND REGION</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C011376A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C011376A/origin#reforigin">
        <time>
          <value>1976-01-13T13:29:19.500000Z</value>
        </time>
        <latitude>
          <value>66.16</value>
        </latitude>
        <longitude>
          <value>-16.58</value>
        </longitude>
        <depth>
          <value>33000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C011376A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C011376A/origin#cmtorigin">
        <time>
          <value>1976-01-13T13:29:24.900000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>66.33</value>
          <uncertainty>0.02</uncertainty>
        </latitude>
        <longitude>
          <value>-16.29</value>
          <uncertainty>0.04</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C011376A/magnitude#moment_mag">
        <mag>
          <value>6.28</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C011376A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C011376A/magnitude#mb">
        <mag>
          <value>6.0</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C011376A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C011376A/magnitude#MS">
        <mag>
          <value>6.4</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C011376A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C011376A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>127.0</value>
            </strike>
            <dip>
              <value>82.0</value>
            </dip>
            <rake>
              <value>173.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>218.0</value>
            </strike>
            <dip>
              <value>83.0</value>
            </dip>
            <rake>
              <value>9.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>82.0</value>
            </azimuth>
            <plunge>
              <value>11.0</value>
            </plunge>
            <length>
              <value>3.63e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>352.0</value>
            </azimuth>
            <plunge>
              <value>1.0</value>
            </plunge>
            <length>
              <value>-2.98e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>255.0</value>
            </azimuth>
            <plunge>
              <value>79.0</value>
            </plunge>
            <length>
              <value>-6.5e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C011376A/momenttensor">
          <derivedOriginID>smi:local/ndk/C011376A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>9</stationCount>
            <componentCount>25</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>13</stationCount>
            <componentCount>33</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>3.3e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>-5.1e+17</value>
              <uncertainty>4e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>-2.86e+18</value>
              <uncertainty>4e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>3.37e+18</value>
              <uncertainty>4e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>5e+16</value>
              <uncertainty>1.6e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>-7.8e+17</value>
              <uncertainty>2e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>-8.6e+17</value>
              <uncertainty>4e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>6.8</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C011376A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C011376A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/M011476A/event">
      <preferredOriginID>smi:local/ndk/M011476A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/M011476A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/M011476A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>KERMADEC ISLANDS, NEW ZEALAND</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>M011476A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/M011476A/origin#reforigin">
        <time>
          <value>1976-01-14T15:56:34.900000Z</value>
        </time>
        <latitude>
          <value>-29.21</value>
        </latitude>
        <longitude>
          <value>-177.89</value>
        </longitude>
        <depth>
          <value>69000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/M011476A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/M011476A/origin#cmtorigin">
        <time>
          <value>1976-01-14T15:57:07.500000Z</value>
          <uncertainty>0.6</uncertainty>
        </time>
        <latitude>
          <value>-29.69</value>
          <uncertainty>0.07</uncertainty>
        </latitude>
        <longitude>
          <value>-177.04</value>
          <uncertainty>0.05</uncertainty>
        </longitude>
        <depth>
          <value>46700.0</value>
          <uncertainty>1500.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/M011476A/magnitude#moment_mag">
        <mag>
          <value>7.79</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/M011476A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/M011476A/magnitude#mb">
        <mag>
          <value>6.3</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/M011476A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/M011476A/magnitude#MS">
        <mag>
          <value>0.0</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/M011476A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/M011476A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>200.0</value>
            </strike>
            <dip>
              <value>26.0</value>
            </dip>
            <rake>
              <value>95.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>15.0</value>
            </strike>
            <dip>
              <value>64.0</value>
            </dip>
            <rake>
              <value>88.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>280.0</value>
            </azimuth>
            <plunge>
              <value>71.0</value>
            </plunge>
            <length>
              <value>6.07e+20</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>106.0</value>
            </azimuth>
            <plunge>
              <value>19.0</value>
            </plunge>
            <length>
              <value>-5.98e+20</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>16.0</value>
            </azimuth>
            <plunge>
              <value>2.0</value>
            </plunge>
            <length>
              <value>-9e+18</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/M011476A/momenttensor">
          <derivedOriginID>smi:local/ndk/M011476A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>12</stationCount>
            <componentCount>30</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>6.02e+20</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>4.78e+20</value>
              <uncertainty>1.3e+19</uncertainty>
            </Mrr>
            <Mtt>
              <value>-4.9e+19</value>
              <uncertainty>9e+18</uncertainty>
            </Mtt>
            <Mpp>
              <value>-4.3e+20</value>
              <uncertainty>1.1e+19</uncertainty>
            </Mpp>
            <Mrt>
              <value>8.3e+19</value>
              <uncertainty>2e+19</uncertainty>
            </Mrt>
            <Mrp>
              <value>3.62e+20</value>
              <uncertainty>2.8e+19</uncertainty>
            </Mrp>
            <Mtp>
              <value>-1.32e+20</value>
              <uncertainty>9e+18</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>40.0</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/M011476A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/M011476A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/M011476B/event">
      <preferredOriginID>smi:local/ndk/M011476B/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/M011476B/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/M011476B/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>KERMADEC ISLANDS REGION</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>M011476B</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/M011476B/origin#reforigin">
        <time>
          <value>1976-01-14T16:47:33.500000Z</value>
        </time>
        <latitude>
          <value>-28.43</value>
        </latitude>
        <longitude>
          <value>-177.66</value>
        </longitude>
        <depth>
          <value>33000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/M011476B/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/M011476B/origin#cmtorigin">
        <time>
          <value>1976-01-14T16:47:44.800000Z</value>
          <uncertainty>0.5</uncertainty>
        </time>
        <latitude>
          <value>-28.72</value>
          <uncertainty>0.06</uncertainty>
        </latitude>
        <longitude>
          <value>-176.75</value>
          <uncertainty>0.05</uncertainty>
        </longitude>
        <depth>
          <value>17700.0</value>
          <uncertainty>2500.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/M011476B/magnitude#moment_mag">
        <mag>
          <value>7.88</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/M011476B/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/M011476B/magnitude#mb">
        <mag>
          <value>6.5</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/M011476B/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/M011476B/magnitude#MS">
        <mag>
          <value>8.0</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/M011476B/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/M011476B/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>189.0</value>
            </strike>
            <dip>
              <value>11.0</value>
            </dip>
            <rake>
              <value>71.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>28.0</value>
            </strike>
            <dip>
              <value>80.0</value>
            </dip>
            <rake>
              <value>93.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>302.0</value>
            </azimuth>
            <plunge>
              <value>55.0</value>
            </plunge>
            <length>
              <value>7.9e+20</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>115.0</value>
            </azimuth>
            <plunge>
              <value>35.0</value>
            </plunge>
            <length>
              <value>-8.46e+20</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>207.0</value>
            </azimuth>
            <plunge>
              <value>3.0</value>
            </plunge>
            <length>
              <value>5.6e+19</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/M011476B/momenttensor">
          <derivedOriginID>smi:local/ndk/M011476B/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>12</stationCount>
            <componentCount>29</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>8.18e+20</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>2.56e+20</value>
              <uncertainty>1.2e+19</uncertainty>
            </Mrr>
            <Mtt>
              <value>1.8e+19</value>
              <uncertainty>8e+18</uncertainty>
            </Mtt>
            <Mpp>
              <value>-2.74e+20</value>
              <uncertainty>8e+18</uncertainty>
            </Mpp>
            <Mrt>
              <value>3.58e+20</value>
              <uncertainty>8.6e+19</uncertainty>
            </Mrt>
            <Mrp>
              <value>6.77e+20</value>
              <uncertainty>1.39e+20</uncertainty>
            </Mrp>
            <Mtp>
              <value>-1.23e+20</value>
              <uncertainty>7e+18</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>41.0</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/M011476B/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/M011476B/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/B011476C/event">
      <preferredOriginID>smi:local/ndk/B011476C/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/B011476C/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/B011476C/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>KERMADEC ISLANDS REGION</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>B011476C</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/B011476C/origin#reforigin">
        <time>
          <value>1976-01-14T22:43:43.100000Z</value>
        </time>
        <latitude>
          <value>-28.66</value>
        </latitude>
        <longitude>
          <value>-176.85</value>
        </longitude>
        <depth>
          <value>31000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/B011476C/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/B011476C/origin#cmtorigin">
        <time>
          <value>1976-01-14T22:43:50.700000Z</value>
          <uncertainty>0.9</uncertainty>
        </time>
        <latitude>
          <value>-28.61</value>
          <uncertainty>0.13</uncertainty>
        </latitude>
        <longitude>
          <value>-176.62</value>
          <uncertainty>0.09</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/B011476C/magnitude#moment_mag">
        <mag>
          <value>6.37</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/B011476C/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/B011476C/magnitude#mb">
        <mag>
          <value>5.5</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/B011476C/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/B011476C/magnitude#MS">
        <mag>
          <value>6.3</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/B011476C/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/B011476C/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>197.0</value>
            </strike>
            <dip>
              <value>17.0</value>
            </dip>
            <rake>
              <value>97.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>10.0</value>
            </strike>
            <dip>
              <value>73.0</value>
            </dip>
            <rake>
              <value>88.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>277.0</value>
            </azimuth>
            <plunge>
              <value>62.0</value>
            </plunge>
            <length>
              <value>4.34e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>101.0</value>
            </azimuth>
            <plunge>
              <value>28.0</value>
            </plunge>
            <length>
              <value>-4.73e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>10.0</value>
            </azimuth>
            <plunge>
              <value>2.0</value>
            </plunge>
            <length>
              <value>3.9e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/B011476C/momenttensor">
          <derivedOriginID>smi:local/ndk/B011476C/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>8</stationCount>
            <componentCount>19</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>4.54e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>2.34e+18</value>
              <uncertainty>2.6e+17</uncertainty>
            </Mrr>
            <Mtt>
              <value>2.4e+17</value>
              <uncertainty>4e+17</uncertainty>
            </Mtt>
            <Mpp>
              <value>-2.58e+18</value>
              <uncertainty>3.1e+17</uncertainty>
            </Mpp>
            <Mrt>
              <value>6.2e+17</value>
              <uncertainty>5.6e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>3.71e+18</value>
              <uncertainty>6.1e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>-6.8e+17</value>
              <uncertainty>3.4e+17</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>7.4</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/B011476C/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/B011476C/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/B011576A/event">
      <preferredOriginID>smi:local/ndk/B011576A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/B011576A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/B011576A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>KERMADEC ISLANDS REGION</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>B011576A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/B011576A/origin#reforigin">
        <time>
          <value>1976-01-15T06:06:46.100000Z</value>
        </time>
        <latitude>
          <value>-30.38</value>
        </latitude>
        <longitude>
          <value>-176.82</value>
        </longitude>
        <depth>
          <value>33000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/B011576A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/B011576A/origin#cmtorigin">
        <time>
          <value>1976-01-15T06:06:51.900000Z</value>
          <uncertainty>0.4</uncertainty>
        </time>
        <latitude>
          <value>-30.25</value>
          <uncertainty>0.06</uncertainty>
        </latitude>
        <longitude>
          <value>-176.63</value>
          <uncertainty>0.04</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/B011576A/magnitude#moment_mag">
        <mag>
          <value>6.13</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/B011576A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/B011576A/magnitude#mb">
        <mag>
          <value>5.3</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/B011576A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/B011576A/magnitude#MS">
        <mag>
          <value>6.2</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/B011576A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/B011576A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>196.0</value>
            </strike>
            <dip>
              <value>26.0</value>
            </dip>
            <rake>
              <value>91.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>15.0</value>
            </strike>
            <dip>
              <value>64.0</value>
            </dip>
            <rake>
              <value>89.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>283.0</value>
            </azimuth>
            <plunge>
              <value>71.0</value>
            </plunge>
            <length>
              <value>1.86e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>105.0</value>
            </azimuth>
            <plunge>
              <value>19.0</value>
            </plunge>
            <length>
              <value>-2.05e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>15.0</value>
            </azimuth>
            <plunge>
              <value>1.0</value>
            </plunge>
            <length>
              <value>1.8e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/B011576A/momenttensor">
          <derivedOriginID>smi:local/ndk/B011576A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>10</stationCount>
            <componentCount>28</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>1.96e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>1.44e+18</value>
              <uncertainty>5e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>6e+16</value>
              <uncertainty>6e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>-1.5e+18</value>
              <uncertainty>6e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>3e+17</value>
              <uncertainty>1.6e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>1.18e+18</value>
              <uncertainty>2e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>-4.6e+17</value>
              <uncertainty>6e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>5.6</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/B011576A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/B011576A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/B011576B/event">
      <preferredOriginID>smi:local/ndk/B011576B/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/B011576B/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/B011576B/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>KERMADEC ISLANDS REGION</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>B011576B</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/B011576B/origin#reforigin">
        <time>
          <value>1976-01-15T16:12:22.300000Z</value>
        </time>
        <latitude>
          <value>-30.15</value>
        </latitude>
        <longitude>
          <value>-177.24</value>
        </longitude>
        <depth>
          <value>33000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/B011576B/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/B011576B/origin#cmtorigin">
        <time>
          <value>1976-01-15T16:12:26.500000Z</value>
          <uncertainty>0.4</uncertainty>
        </time>
        <latitude>
          <value>-30.25</value>
          <uncertainty>0.05</uncertainty>
        </latitude>
        <longitude>
          <value>-176.99</value>
          <uncertainty>0.04</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/B011576B/magnitude#moment_mag">
        <mag>
          <value>5.92</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/B011576B/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/B011576B/magnitude#mb">
        <mag>
          <value>5.1</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/B011576B/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/B011576B/magnitude#MS">
        <mag>
          <value>6.1</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/B011576B/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/B011576B/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>180.0</value>
            </strike>
            <dip>
              <value>10.0</value>
            </dip>
            <rake>
              <value>73.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>17.0</value>
            </strike>
            <dip>
              <value>80.0</value>
            </dip>
            <rake>
              <value>93.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>291.0</value>
            </azimuth>
            <plunge>
              <value>55.0</value>
            </plunge>
            <length>
              <value>9.41e+17</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>105.0</value>
            </azimuth>
            <plunge>
              <value>35.0</value>
            </plunge>
            <length>
              <value>-9.85e+17</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>197.0</value>
            </azimuth>
            <plunge>
              <value>3.0</value>
            </plunge>
            <length>
              <value>4.3e+16</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/B011576B/momenttensor">
          <derivedOriginID>smi:local/ndk/B011576B/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>9</stationCount>
            <componentCount>24</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>9.63e+17</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>3.07e+17</value>
              <uncertainty>1.3e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>3.8e+16</value>
              <uncertainty>1.4e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>-3.45e+17</value>
              <uncertainty>1.5e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>2.75e+17</value>
              <uncertainty>3.3e+16</uncertainty>
            </Mrt>
            <Mrp>
              <value>8.61e+17</value>
              <uncertainty>4.5e+16</uncertainty>
            </Mrp>
            <Mtp>
              <value>-6.8e+16</value>
              <uncertainty>1.6e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>4.0</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/B011576B/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/B011576B/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/M012176A/event">
      <preferredOriginID>smi:local/ndk/M012176A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/M012176A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/M012176A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>KURIL ISLANDS</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>M012176A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/M012176A/origin#reforigin">
        <time>
          <value>1976-01-21T10:05:24.100000Z</value>
        </time>
        <latitude>
          <value>44.92</value>
        </latitude>
        <longitude>
          <value>149.12</value>
        </longitude>
        <depth>
          <value>41000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/M012176A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/M012176A/origin#cmtorigin">
        <time>
          <value>1976-01-21T10:05:33.600000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>44.58</value>
          <uncertainty>0.02</uncertainty>
        </latitude>
        <longitude>
          <value>149.49</value>
          <uncertainty>0.03</uncertainty>
        </longitude>
        <depth>
          <value>26500.0</value>
          <uncertainty>900.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/M012176A/magnitude#moment_mag">
        <mag>
          <value>7.16</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/M012176A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/M012176A/magnitude#mb">
        <mag>
          <value>6.3</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/M012176A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/M012176A/magnitude#MS">
        <mag>
          <value>7.0</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/M012176A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/M012176A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>237.0</value>
            </strike>
            <dip>
              <value>16.0</value>
            </dip>
            <rake>
              <value>116.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>30.0</value>
            </strike>
            <dip>
              <value>76.0</value>
            </dip>
            <rake>
              <value>83.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>291.0</value>
            </azimuth>
            <plunge>
              <value>59.0</value>
            </plunge>
            <length>
              <value>6.89e+19</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>126.0</value>
            </azimuth>
            <plunge>
              <value>31.0</value>
            </plunge>
            <length>
              <value>-6.94e+19</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>32.0</value>
            </azimuth>
            <plunge>
              <value>7.0</value>
            </plunge>
            <length>
              <value>5e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/M012176A/momenttensor">
          <derivedOriginID>smi:local/ndk/M012176A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>11</stationCount>
            <componentCount>23</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>6.91e+19</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>3.21e+19</value>
              <uncertainty>5e+17</uncertainty>
            </Mrr>
            <Mtt>
              <value>-1.49e+19</value>
              <uncertainty>4e+17</uncertainty>
            </Mtt>
            <Mpp>
              <value>-1.72e+19</value>
              <uncertainty>3e+17</uncertainty>
            </Mpp>
            <Mrt>
              <value>2.87e+19</value>
              <uncertainty>2.5e+18</uncertainty>
            </Mrt>
            <Mrp>
              <value>5.33e+19</value>
              <uncertainty>3.3e+18</uncertainty>
            </Mrp>
            <Mtp>
              <value>-1.84e+19</value>
              <uncertainty>3e+17</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>18.6</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/M012176A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/M012176A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C012376A/event">
      <preferredOriginID>smi:local/ndk/C012376A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C012376A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C012376A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>FLORES SEA</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C012376A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C012376A/origin#reforigin">
        <time>
          <value>1976-01-23T05:45:30.500000Z</value>
        </time>
        <latitude>
          <value>-7.48</value>
        </latitude>
        <longitude>
          <value>119.9</value>
        </longitude>
        <depth>
          <value>614000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C012376A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C012376A/origin#cmtorigin">
        <time>
          <value>1976-01-23T05:45:38.500000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>-7.37</value>
          <uncertainty>0.02</uncertainty>
        </latitude>
        <longitude>
          <value>120.07</value>
          <uncertainty>0.02</uncertainty>
        </longitude>
        <depth>
          <value>623100.0</value>
          <uncertainty>1500.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C012376A/magnitude#moment_mag">
        <mag>
          <value>6.73</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C012376A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C012376A/magnitude#mb">
        <mag>
          <value>6.4</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C012376A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C012376A/magnitude#MS">
        <mag>
          <value>0.0</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C012376A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C012376A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>233.0</value>
            </strike>
            <dip>
              <value>38.0</value>
            </dip>
            <rake>
              <value>-96.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>61.0</value>
            </strike>
            <dip>
              <value>53.0</value>
            </dip>
            <rake>
              <value>-85.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>147.0</value>
            </azimuth>
            <plunge>
              <value>8.0</value>
            </plunge>
            <length>
              <value>1.54e+19</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>354.0</value>
            </azimuth>
            <plunge>
              <value>82.0</value>
            </plunge>
            <length>
              <value>-1.63e+19</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>238.0</value>
            </azimuth>
            <plunge>
              <value>4.0</value>
            </plunge>
            <length>
              <value>9e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C012376A/momenttensor">
          <derivedOriginID>smi:local/ndk/C012376A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>7</stationCount>
            <componentCount>18</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>13</stationCount>
            <componentCount>29</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>1.58e+19</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>-1.56e+19</value>
              <uncertainty>2e+17</uncertainty>
            </Mrr>
            <Mtt>
              <value>1.06e+19</value>
              <uncertainty>2e+17</uncertainty>
            </Mtt>
            <Mpp>
              <value>5e+18</value>
              <uncertainty>2e+17</uncertainty>
            </Mpp>
            <Mrt>
              <value>-4.1e+18</value>
              <uncertainty>2e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>-1.3e+18</value>
              <uncertainty>2e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>6.4e+18</value>
              <uncertainty>2e+17</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>11.4</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C012376A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C012376A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C012476A/event">
      <preferredOriginID>smi:local/ndk/C012476A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C012476A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C012476A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>KERMADEC ISLANDS REGION</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C012476A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C012476A/origin#reforigin">
        <time>
          <value>1976-01-24T21:48:25.900000Z</value>
        </time>
        <latitude>
          <value>-28.64</value>
        </latitude>
        <longitude>
          <value>-177.59</value>
        </longitude>
        <depth>
          <value>78000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C012476A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C012476A/origin#cmtorigin">
        <time>
          <value>1976-01-24T21:48:27.100000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>-28.79</value>
          <uncertainty>0.02</uncertainty>
        </latitude>
        <longitude>
          <value>-177.17</value>
          <uncertainty>0.01</uncertainty>
        </longitude>
        <depth>
          <value>60200.0</value>
          <uncertainty>800.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C012476A/magnitude#moment_mag">
        <mag>
          <value>6.21</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C012476A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C012476A/magnitude#mb">
        <mag>
          <value>6.2</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C012476A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C012476A/magnitude#MS">
        <mag>
          <value>0.0</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C012476A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C012476A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>196.0</value>
            </strike>
            <dip>
              <value>37.0</value>
            </dip>
            <rake>
              <value>89.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>17.0</value>
            </strike>
            <dip>
              <value>53.0</value>
            </dip>
            <rake>
              <value>90.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>289.0</value>
            </azimuth>
            <plunge>
              <value>82.0</value>
            </plunge>
            <length>
              <value>2.45e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>106.0</value>
            </azimuth>
            <plunge>
              <value>8.0</value>
            </plunge>
            <length>
              <value>-2.66e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>196.0</value>
            </azimuth>
            <plunge>
              <value>0.0</value>
            </plunge>
            <length>
              <value>2.1e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C012476A/momenttensor">
          <derivedOriginID>smi:local/ndk/C012476A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>10</stationCount>
            <componentCount>27</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>11</stationCount>
            <componentCount>21</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>2.56e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>2.35e+18</value>
              <uncertainty>4e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>0.0</value>
              <uncertainty>3e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>-2.34e+18</value>
              <uncertainty>3e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>2.2e+17</value>
              <uncertainty>5e+16</uncertainty>
            </Mrt>
            <Mrp>
              <value>7e+17</value>
              <uncertainty>5e+16</uncertainty>
            </Mrp>
            <Mtp>
              <value>-7.4e+17</value>
              <uncertainty>3e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>6.2</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C012476A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C012476A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/B012676A/event">
      <preferredOriginID>smi:local/ndk/B012676A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/B012676A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/B012676A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>KERMADEC ISLANDS REGION</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>B012676A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/B012676A/origin#reforigin">
        <time>
          <value>1976-01-26T19:01:38.600000Z</value>
        </time>
        <latitude>
          <value>-29.34</value>
        </latitude>
        <longitude>
          <value>-176.46</value>
        </longitude>
        <depth>
          <value>30000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/B012676A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/B012676A/origin#cmtorigin">
        <time>
          <value>1976-01-26T19:01:49.400000Z</value>
          <uncertainty>0.9</uncertainty>
        </time>
        <latitude>
          <value>-28.27</value>
          <uncertainty>0.11</uncertainty>
        </latitude>
        <longitude>
          <value>-177.18</value>
          <uncertainty>0.09</uncertainty>
        </longitude>
        <depth>
          <value>62000.0</value>
          <uncertainty>8900.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/B012676A/magnitude#moment_mag">
        <mag>
          <value>5.34</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/B012676A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/B012676A/magnitude#mb">
        <mag>
          <value>6.0</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/B012676A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/B012676A/magnitude#MS">
        <mag>
          <value>0.0</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/B012676A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/B012676A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>253.0</value>
            </strike>
            <dip>
              <value>18.0</value>
            </dip>
            <rake>
              <value>146.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>16.0</value>
            </strike>
            <dip>
              <value>80.0</value>
            </dip>
            <rake>
              <value>75.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>268.0</value>
            </azimuth>
            <plunge>
              <value>53.0</value>
            </plunge>
            <length>
              <value>1.23e+17</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>118.0</value>
            </azimuth>
            <plunge>
              <value>33.0</value>
            </plunge>
            <length>
              <value>-1.31e+17</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>18.0</value>
            </azimuth>
            <plunge>
              <value>15.0</value>
            </plunge>
            <length>
              <value>8e+15</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/B012676A/momenttensor">
          <derivedOriginID>smi:local/ndk/B012676A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>12</stationCount>
            <componentCount>32</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>1.27e+17</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>3.9e+16</value>
              <uncertainty>1.2e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>-1.4e+16</value>
              <uncertainty>1.7e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>-2.5e+16</value>
              <uncertainty>1.7e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>2.8e+16</value>
              <uncertainty>1.9e+16</uncertainty>
            </Mrt>
            <Mrp>
              <value>1.11e+17</value>
              <uncertainty>4.1e+16</uncertainty>
            </Mrp>
            <Mtp>
              <value>-4.2e+16</value>
              <uncertainty>1.9e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>6.0</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/B012676A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/B012676A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C020376A/event">
      <preferredOriginID>smi:local/ndk/C020376A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C020376A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C020376A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>NEAR EAST COAST OF KAMCHATKA</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C020376A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C020376A/origin#reforigin">
        <time>
          <value>1976-02-03T23:57:54.900000Z</value>
        </time>
        <latitude>
          <value>54.5</value>
        </latitude>
        <longitude>
          <value>161.89</value>
        </longitude>
        <depth>
          <value>33000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C020376A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C020376A/origin#cmtorigin">
        <time>
          <value>1976-02-03T23:58:03.700000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>54.25</value>
          <uncertainty>0.02</uncertainty>
        </latitude>
        <longitude>
          <value>162.16</value>
          <uncertainty>0.04</uncertainty>
        </longitude>
        <depth>
          <value>48000.0</value>
          <uncertainty>1400.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C020376A/magnitude#moment_mag">
        <mag>
          <value>5.82</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C020376A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C020376A/magnitude#mb">
        <mag>
          <value>6.0</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C020376A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C020376A/magnitude#MS">
        <mag>
          <value>5.2</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C020376A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C020376A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>257.0</value>
            </strike>
            <dip>
              <value>27.0</value>
            </dip>
            <rake>
              <value>133.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>31.0</value>
            </strike>
            <dip>
              <value>70.0</value>
            </dip>
            <rake>
              <value>71.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>274.0</value>
            </azimuth>
            <plunge>
              <value>60.0</value>
            </plunge>
            <length>
              <value>6.96e+17</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>136.0</value>
            </azimuth>
            <plunge>
              <value>23.0</value>
            </plunge>
            <length>
              <value>-6.47e+17</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>38.0</value>
            </azimuth>
            <plunge>
              <value>18.0</value>
            </plunge>
            <length>
              <value>-5e+16</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C020376A/momenttensor">
          <derivedOriginID>smi:local/ndk/C020376A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>11</stationCount>
            <componentCount>32</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>12</stationCount>
            <componentCount>16</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>6.72e+17</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>4.2e+17</value>
              <uncertainty>1.1e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>-3.11e+17</value>
              <uncertainty>1.3e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>-1.09e+17</value>
              <uncertainty>1.2e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>1.75e+17</value>
              <uncertainty>1.6e+16</uncertainty>
            </Mrt>
            <Mrp>
              <value>4.71e+17</value>
              <uncertainty>1.8e+16</uncertainty>
            </Mrp>
            <Mtp>
              <value>-2.41e+17</value>
              <uncertainty>1e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>4.0</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C020376A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C020376A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/M020476A/event">
      <preferredOriginID>smi:local/ndk/M020476A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/M020476A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/M020476A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>GUATEMALA</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>M020476A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/M020476A/origin#reforigin">
        <time>
          <value>1976-02-04T09:01:43.400000Z</value>
        </time>
        <latitude>
          <value>15.32</value>
        </latitude>
        <longitude>
          <value>-89.1</value>
        </longitude>
        <depth>
          <value>5000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/M020476A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/M020476A/origin#cmtorigin">
        <time>
          <value>1976-02-04T09:02:07.200000Z</value>
          <uncertainty>0.3</uncertainty>
        </time>
        <latitude>
          <value>15.14</value>
          <uncertainty>0.02</uncertainty>
        </latitude>
        <longitude>
          <value>-89.78</value>
          <uncertainty>0.02</uncertainty>
        </longitude>
        <depth>
          <value>16300.0</value>
          <uncertainty>1300.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/M020476A/magnitude#moment_mag">
        <mag>
          <value>7.47</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/M020476A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/M020476A/magnitude#mb">
        <mag>
          <value>6.2</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/M020476A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/M020476A/magnitude#MS">
        <mag>
          <value>7.5</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/M020476A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/M020476A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>254.0</value>
            </strike>
            <dip>
              <value>73.0</value>
            </dip>
            <rake>
              <value>-10.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>347.0</value>
            </strike>
            <dip>
              <value>80.0</value>
            </dip>
            <rake>
              <value>-162.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>119.0</value>
            </azimuth>
            <plunge>
              <value>5.0</value>
            </plunge>
            <length>
              <value>2.12e+20</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>211.0</value>
            </azimuth>
            <plunge>
              <value>20.0</value>
            </plunge>
            <length>
              <value>-1.95e+20</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>15.0</value>
            </azimuth>
            <plunge>
              <value>70.0</value>
            </plunge>
            <length>
              <value>-1.7e+19</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/M020476A/momenttensor">
          <derivedOriginID>smi:local/ndk/M020476A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>15</stationCount>
            <componentCount>34</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>2.04e+20</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>-3.5e+19</value>
              <uncertainty>2e+18</uncertainty>
            </Mrr>
            <Mtt>
              <value>-7.8e+19</value>
              <uncertainty>2e+18</uncertainty>
            </Mtt>
            <Mpp>
              <value>1.12e+20</value>
              <uncertainty>2e+18</uncertainty>
            </Mpp>
            <Mrt>
              <value>3.8e+19</value>
              <uncertainty>1.8e+19</uncertainty>
            </Mrt>
            <Mrp>
              <value>-4.7e+19</value>
              <uncertainty>1.8e+19</uncertainty>
            </Mrp>
            <Mtp>
              <value>1.67e+20</value>
              <uncertainty>3e+18</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>27.6</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/M020476A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/M020476A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/B020676A/event">
      <preferredOriginID>smi:local/ndk/B020676A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/B020676A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/B020676A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>EASTERN NEW GUINEA REG., P.N.G.</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>B020676A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/B020676A/origin#reforigin">
        <time>
          <value>1976-02-06T16:53:50.500000Z</value>
        </time>
        <latitude>
          <value>-5.98</value>
        </latitude>
        <longitude>
          <value>146.31</value>
        </longitude>
        <depth>
          <value>37000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/B020676A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/B020676A/origin#cmtorigin">
        <time>
          <value>1976-02-06T16:53:58.800000Z</value>
          <uncertainty>0.3</uncertainty>
        </time>
        <latitude>
          <value>-6.04</value>
          <uncertainty>0.05</uncertainty>
        </latitude>
        <longitude>
          <value>146.1</value>
          <uncertainty>0.04</uncertainty>
        </longitude>
        <depth>
          <value>29500.0</value>
          <uncertainty>2000.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/B020676A/magnitude#moment_mag">
        <mag>
          <value>5.98</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/B020676A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/B020676A/magnitude#mb">
        <mag>
          <value>6.0</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/B020676A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/B020676A/magnitude#MS">
        <mag>
          <value>5.6</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/B020676A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/B020676A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>357.0</value>
            </strike>
            <dip>
              <value>6.0</value>
            </dip>
            <rake>
              <value>140.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>128.0</value>
            </strike>
            <dip>
              <value>86.0</value>
            </dip>
            <rake>
              <value>85.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>33.0</value>
            </azimuth>
            <plunge>
              <value>49.0</value>
            </plunge>
            <length>
              <value>1.15e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>222.0</value>
            </azimuth>
            <plunge>
              <value>41.0</value>
            </plunge>
            <length>
              <value>-1.211e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>128.0</value>
            </azimuth>
            <plunge>
              <value>5.0</value>
            </plunge>
            <length>
              <value>6.1e+16</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/B020676A/momenttensor">
          <derivedOriginID>smi:local/ndk/B020676A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>10</stationCount>
            <componentCount>25</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>1.181e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>1.29e+17</value>
              <uncertainty>1.7e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>-5e+15</value>
              <uncertainty>2.4e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>-1.24e+17</value>
              <uncertainty>2e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>9.23e+17</value>
              <uncertainty>6.1e+16</uncertainty>
            </Mrt>
            <Mrp>
              <value>-7.12e+17</value>
              <uncertainty>4.9e+16</uncertainty>
            </Mrp>
            <Mtp>
              <value>1.45e+17</value>
              <uncertainty>1.9e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>4.6</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/B020676A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/B020676A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C021476A/event">
      <preferredOriginID>smi:local/ndk/C021476A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C021476A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C021476A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>DRAKE PASSAGE</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C021476A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C021476A/origin#reforigin">
        <time>
          <value>1976-02-14T03:10:37.300000Z</value>
        </time>
        <latitude>
          <value>-57.41</value>
        </latitude>
        <longitude>
          <value>-64.42</value>
        </longitude>
        <depth>
          <value>40000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C021476A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C021476A/origin#cmtorigin">
        <time>
          <value>1976-02-14T03:10:35.100000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>-57.22</value>
          <uncertainty>0.03</uncertainty>
        </latitude>
        <longitude>
          <value>-64.94</value>
          <uncertainty>0.05</uncertainty>
        </longitude>
        <depth>
          <value>16900.0</value>
          <uncertainty>1300.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C021476A/magnitude#moment_mag">
        <mag>
          <value>5.84</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C021476A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C021476A/magnitude#mb">
        <mag>
          <value>6.0</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C021476A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C021476A/magnitude#MS">
        <mag>
          <value>5.7</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C021476A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C021476A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>345.0</value>
            </strike>
            <dip>
              <value>37.0</value>
            </dip>
            <rake>
              <value>107.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>145.0</value>
            </strike>
            <dip>
              <value>54.0</value>
            </dip>
            <rake>
              <value>78.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>13.0</value>
            </azimuth>
            <plunge>
              <value>77.0</value>
            </plunge>
            <length>
              <value>6.44e+17</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>243.0</value>
            </azimuth>
            <plunge>
              <value>9.0</value>
            </plunge>
            <length>
              <value>-7.83e+17</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>152.0</value>
            </azimuth>
            <plunge>
              <value>10.0</value>
            </plunge>
            <length>
              <value>1.4e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C021476A/momenttensor">
          <derivedOriginID>smi:local/ndk/C021476A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>11</stationCount>
            <componentCount>25</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>10</stationCount>
            <componentCount>16</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>7.13e+17</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>5.97e+17</value>
              <uncertainty>1.8e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>-1.7e+16</value>
              <uncertainty>1.8e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>-5.8e+17</value>
              <uncertainty>1.5e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>1.7e+17</value>
              <uncertainty>5e+16</uncertainty>
            </Mrt>
            <Mrp>
              <value>-1.48e+17</value>
              <uncertainty>4.9e+16</uncertainty>
            </Mrp>
            <Mtp>
              <value>3.56e+17</value>
              <uncertainty>1.6e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>4.0</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C021476A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C021476A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C021576A/event">
      <preferredOriginID>smi:local/ndk/C021576A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C021576A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C021576A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>PHILIPPINE ISLANDS REGION</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C021576A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C021576A/origin#reforigin">
        <time>
          <value>1976-02-15T01:54:23.100000Z</value>
        </time>
        <latitude>
          <value>13.0</value>
        </latitude>
        <longitude>
          <value>125.79</value>
        </longitude>
        <depth>
          <value>33000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C021576A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C021576A/origin#cmtorigin">
        <time>
          <value>1976-02-15T01:54:30.300000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>13.12</value>
          <uncertainty>0.02</uncertainty>
        </latitude>
        <longitude>
          <value>126.02</value>
          <uncertainty>0.02</uncertainty>
        </longitude>
        <depth>
          <value>15600.0</value>
          <uncertainty>800.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C021576A/magnitude#moment_mag">
        <mag>
          <value>6.47</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C021576A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C021576A/magnitude#mb">
        <mag>
          <value>6.1</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C021576A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C021576A/magnitude#MS">
        <mag>
          <value>6.1</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C021576A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C021576A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>322.0</value>
            </strike>
            <dip>
              <value>39.0</value>
            </dip>
            <rake>
              <value>-73.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>121.0</value>
            </strike>
            <dip>
              <value>53.0</value>
            </dip>
            <rake>
              <value>-104.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>220.0</value>
            </azimuth>
            <plunge>
              <value>7.0</value>
            </plunge>
            <length>
              <value>7.49e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>342.0</value>
            </azimuth>
            <plunge>
              <value>77.0</value>
            </plunge>
            <length>
              <value>-5.44e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>129.0</value>
            </azimuth>
            <plunge>
              <value>11.0</value>
            </plunge>
            <length>
              <value>-2.06e+18</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C021576A/momenttensor">
          <derivedOriginID>smi:local/ndk/C021576A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>8</stationCount>
            <componentCount>20</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>12</stationCount>
            <componentCount>25</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>6.47e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>-5.14e+18</value>
              <uncertainty>8e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>3.27e+18</value>
              <uncertainty>7e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>1.86e+18</value>
              <uncertainty>6e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>-1.56e+18</value>
              <uncertainty>2.8e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>5.1e+17</value>
              <uncertainty>2.2e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>-4.69e+18</value>
              <uncertainty>6e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>8.4</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C021576A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C021576A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C021576B/event">
      <preferredOriginID>smi:local/ndk/C021576B/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C021576B/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C021576B/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>KERMADEC ISLANDS REGION</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C021576B</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C021576B/origin#reforigin">
        <time>
          <value>1976-02-15T21:23:22.600000Z</value>
        </time>
        <latitude>
          <value>-28.39</value>
        </latitude>
        <longitude>
          <value>-176.79</value>
        </longitude>
        <depth>
          <value>54000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C021576B/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C021576B/origin#cmtorigin">
        <time>
          <value>1976-02-15T21:23:23.400000Z</value>
          <uncertainty>0.3</uncertainty>
        </time>
        <latitude>
          <value>-28.52</value>
          <uncertainty>0.04</uncertainty>
        </latitude>
        <longitude>
          <value>-176.47</value>
          <uncertainty>0.03</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>1300.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C021576B/magnitude#moment_mag">
        <mag>
          <value>6.05</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C021576B/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C021576B/magnitude#mb">
        <mag>
          <value>5.5</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C021576B/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C021576B/magnitude#MS">
        <mag>
          <value>6.2</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C021576B/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C021576B/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>204.0</value>
            </strike>
            <dip>
              <value>17.0</value>
            </dip>
            <rake>
              <value>96.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>18.0</value>
            </strike>
            <dip>
              <value>73.0</value>
            </dip>
            <rake>
              <value>88.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>285.0</value>
            </azimuth>
            <plunge>
              <value>62.0</value>
            </plunge>
            <length>
              <value>1.42e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>109.0</value>
            </azimuth>
            <plunge>
              <value>28.0</value>
            </plunge>
            <length>
              <value>-1.54e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>18.0</value>
            </azimuth>
            <plunge>
              <value>2.0</value>
            </plunge>
            <length>
              <value>1.2e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C021576B/momenttensor">
          <derivedOriginID>smi:local/ndk/C021576B/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>11</stationCount>
            <componentCount>30</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>12</stationCount>
            <componentCount>16</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>1.48e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>7.7e+17</value>
              <uncertainty>2e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>0.0</value>
              <uncertainty>2e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>-7.6e+17</value>
              <uncertainty>2e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>3.7e+17</value>
              <uncertainty>6e+16</uncertainty>
            </Mrt>
            <Mrp>
              <value>1.17e+18</value>
              <uncertainty>1.4e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>-3.3e+17</value>
              <uncertainty>2e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>5.0</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C021576B/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C021576B/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C022276A/event">
      <preferredOriginID>smi:local/ndk/C022276A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C022276A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C022276A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>NEAR N COAST OF NEW GUINEA, PNG.</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C022276A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C022276A/origin#reforigin">
        <time>
          <value>1976-02-22T05:11:07.900000Z</value>
        </time>
        <latitude>
          <value>-3.36</value>
        </latitude>
        <longitude>
          <value>145.24</value>
        </longitude>
        <depth>
          <value>22000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C022276A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C022276A/origin#cmtorigin">
        <time>
          <value>1976-02-22T05:11:10.200000Z</value>
          <uncertainty>0.3</uncertainty>
        </time>
        <latitude>
          <value>-3.44</value>
          <uncertainty>0.04</uncertainty>
        </latitude>
        <longitude>
          <value>145.61</value>
          <uncertainty>0.03</uncertainty>
        </longitude>
        <depth>
          <value>25300.0</value>
          <uncertainty>3700.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C022276A/magnitude#moment_mag">
        <mag>
          <value>5.48</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C022276A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C022276A/magnitude#mb">
        <mag>
          <value>5.1</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C022276A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C022276A/magnitude#MS">
        <mag>
          <value>6.0</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C022276A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C022276A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>272.0</value>
            </strike>
            <dip>
              <value>88.0</value>
            </dip>
            <rake>
              <value>-1.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>2.0</value>
            </strike>
            <dip>
              <value>89.0</value>
            </dip>
            <rake>
              <value>-178.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>137.0</value>
            </azimuth>
            <plunge>
              <value>0.0</value>
            </plunge>
            <length>
              <value>2.03e+17</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>227.0</value>
            </azimuth>
            <plunge>
              <value>2.0</value>
            </plunge>
            <length>
              <value>-2.17e+17</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>31.0</value>
            </azimuth>
            <plunge>
              <value>88.0</value>
            </plunge>
            <length>
              <value>1.4e+16</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C022276A/momenttensor">
          <derivedOriginID>smi:local/ndk/C022276A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>11</stationCount>
            <componentCount>28</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>8</stationCount>
            <componentCount>13</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>2.1e+17</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>1.4e+16</value>
              <uncertainty>5e+15</uncertainty>
            </Mrr>
            <Mtt>
              <value>7e+15</value>
              <uncertainty>8e+15</uncertainty>
            </Mtt>
            <Mpp>
              <value>-2.1e+16</value>
              <uncertainty>7e+15</uncertainty>
            </Mpp>
            <Mrt>
              <value>4e+15</value>
              <uncertainty>1.2e+16</uncertainty>
            </Mrt>
            <Mrp>
              <value>-6e+15</value>
              <uncertainty>1.2e+16</uncertainty>
            </Mrp>
            <Mtp>
              <value>2.1e+17</value>
              <uncertainty>6e+15</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>2.6</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C022276A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C022276A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C022376A/event">
      <preferredOriginID>smi:local/ndk/C022376A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C022376A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C022376A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>QUEEN CHARLOTTE ISLANDS REGION</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C022376A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C022376A/origin#reforigin">
        <time>
          <value>1976-02-23T15:14:16.000000Z</value>
        </time>
        <latitude>
          <value>51.47</value>
        </latitude>
        <longitude>
          <value>-130.44</value>
        </longitude>
        <depth>
          <value>16000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C022376A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C022376A/origin#cmtorigin">
        <time>
          <value>1976-02-23T15:14:21.300000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>51.63</value>
          <uncertainty>0.02</uncertainty>
        </latitude>
        <longitude>
          <value>-130.93</value>
          <uncertainty>0.03</uncertainty>
        </longitude>
        <depth>
          <value>22500.0</value>
          <uncertainty>2100.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C022376A/magnitude#moment_mag">
        <mag>
          <value>5.97</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C022376A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C022376A/magnitude#mb">
        <mag>
          <value>5.6</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C022376A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C022376A/magnitude#MS">
        <mag>
          <value>6.0</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C022376A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C022376A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>263.0</value>
            </strike>
            <dip>
              <value>79.0</value>
            </dip>
            <rake>
              <value>-10.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>355.0</value>
            </strike>
            <dip>
              <value>80.0</value>
            </dip>
            <rake>
              <value>-169.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>129.0</value>
            </azimuth>
            <plunge>
              <value>1.0</value>
            </plunge>
            <length>
              <value>1.19e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>219.0</value>
            </azimuth>
            <plunge>
              <value>15.0</value>
            </plunge>
            <length>
              <value>-1.08e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>37.0</value>
            </azimuth>
            <plunge>
              <value>75.0</value>
            </plunge>
            <length>
              <value>-1.1e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C022376A/momenttensor">
          <derivedOriginID>smi:local/ndk/C022376A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>10</stationCount>
            <componentCount>22</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>13</stationCount>
            <componentCount>18</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>1.14e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>-1.7e+17</value>
              <uncertainty>2e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>-1.6e+17</value>
              <uncertainty>3e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>3.3e+17</value>
              <uncertainty>2e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>1.8e+17</value>
              <uncertainty>6e+16</uncertainty>
            </Mrt>
            <Mrp>
              <value>-1.6e+17</value>
              <uncertainty>5e+16</uncertainty>
            </Mrp>
            <Mtp>
              <value>1.08e+18</value>
              <uncertainty>2e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>4.8</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C022376A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C022376A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C022876A/event">
      <preferredOriginID>smi:local/ndk/C022876A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C022876A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C022876A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>OFF COAST OF SOUTHERN CHILE</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C022876A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C022876A/origin#reforigin">
        <time>
          <value>1976-02-28T16:27:09.000000Z</value>
        </time>
        <latitude>
          <value>-40.0</value>
        </latitude>
        <longitude>
          <value>-74.73</value>
        </longitude>
        <depth>
          <value>9000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C022876A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C022876A/origin#cmtorigin">
        <time>
          <value>1976-02-28T16:27:13.900000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>-40.3</value>
          <uncertainty>0.03</uncertainty>
        </latitude>
        <longitude>
          <value>-75.57</value>
          <uncertainty>0.02</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C022876A/magnitude#moment_mag">
        <mag>
          <value>5.92</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C022876A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C022876A/magnitude#mb">
        <mag>
          <value>6.0</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C022876A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C022876A/magnitude#MS">
        <mag>
          <value>5.5</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C022876A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C022876A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>13.0</value>
            </strike>
            <dip>
              <value>45.0</value>
            </dip>
            <rake>
              <value>-85.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>187.0</value>
            </strike>
            <dip>
              <value>45.0</value>
            </dip>
            <rake>
              <value>-95.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>280.0</value>
            </azimuth>
            <plunge>
              <value>0.0</value>
            </plunge>
            <length>
              <value>1.07e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>13.0</value>
            </azimuth>
            <plunge>
              <value>87.0</value>
            </plunge>
            <length>
              <value>-8e+17</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>190.0</value>
            </azimuth>
            <plunge>
              <value>3.0</value>
            </plunge>
            <length>
              <value>-2.7e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C022876A/momenttensor">
          <derivedOriginID>smi:local/ndk/C022876A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>10</stationCount>
            <componentCount>25</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>13</stationCount>
            <componentCount>21</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>9.4e+17</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>-8e+17</value>
              <uncertainty>1e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>-2.3e+17</value>
              <uncertainty>2e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>1.03e+18</value>
              <uncertainty>1e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>-3e+16</value>
              <uncertainty>5e+16</uncertainty>
            </Mrt>
            <Mrp>
              <value>1e+16</value>
              <uncertainty>6e+16</uncertainty>
            </Mrp>
            <Mtp>
              <value>2.3e+17</value>
              <uncertainty>1e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>4.4</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C022876A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C022876A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C030376A/event">
      <preferredOriginID>smi:local/ndk/C030376A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C030376A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C030376A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>FLORES REGION, INDONESIA</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C030376A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C030376A/origin#reforigin">
        <time>
          <value>1976-03-03T22:50:10.000000Z</value>
        </time>
        <latitude>
          <value>-8.23</value>
        </latitude>
        <longitude>
          <value>121.44</value>
        </longitude>
        <depth>
          <value>30000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C030376A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C030376A/origin#cmtorigin">
        <time>
          <value>1976-03-03T22:50:17.100000Z</value>
          <uncertainty>0.3</uncertainty>
        </time>
        <latitude>
          <value>-8.47</value>
          <uncertainty>0.03</uncertainty>
        </latitude>
        <longitude>
          <value>121.69</value>
          <uncertainty>0.03</uncertainty>
        </longitude>
        <depth>
          <value>38700.0</value>
          <uncertainty>2100.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C030376A/magnitude#moment_mag">
        <mag>
          <value>5.66</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C030376A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C030376A/magnitude#mb">
        <mag>
          <value>6.0</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C030376A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C030376A/magnitude#MS">
        <mag>
          <value>5.0</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C030376A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C030376A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>68.0</value>
            </strike>
            <dip>
              <value>36.0</value>
            </dip>
            <rake>
              <value>83.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>257.0</value>
            </strike>
            <dip>
              <value>54.0</value>
            </dip>
            <rake>
              <value>95.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>187.0</value>
            </azimuth>
            <plunge>
              <value>80.0</value>
            </plunge>
            <length>
              <value>3.45e+17</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>343.0</value>
            </azimuth>
            <plunge>
              <value>9.0</value>
            </plunge>
            <length>
              <value>-4.24e+17</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>74.0</value>
            </azimuth>
            <plunge>
              <value>4.0</value>
            </plunge>
            <length>
              <value>7.8e+16</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C030376A/momenttensor">
          <derivedOriginID>smi:local/ndk/C030376A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>10</stationCount>
            <componentCount>27</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>7</stationCount>
            <componentCount>9</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>3.84e+17</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>3.24e+17</value>
              <uncertainty>1.1e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>-3.62e+17</value>
              <uncertainty>1.3e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>3.8e+16</value>
              <uncertainty>1.4e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>-1.23e+17</value>
              <uncertainty>2.5e+16</uncertainty>
            </Mrt>
            <Mrp>
              <value>-1.8e+16</value>
              <uncertainty>2e+16</uncertainty>
            </Mrp>
            <Mtp>
              <value>-1.36e+17</value>
              <uncertainty>1.1e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>3.2</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C030376A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C030376A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C030476A/event">
      <preferredOriginID>smi:local/ndk/C030476A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C030476A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C030476A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>VANUATU ISLANDS</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C030476A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C030476A/origin#reforigin">
        <time>
          <value>1976-03-04T02:50:00.500000Z</value>
        </time>
        <latitude>
          <value>-14.74</value>
        </latitude>
        <longitude>
          <value>167.1</value>
        </longitude>
        <depth>
          <value>90000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C030476A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C030476A/origin#cmtorigin">
        <time>
          <value>1976-03-04T02:50:08.900000Z</value>
          <uncertainty>0.1</uncertainty>
        </time>
        <latitude>
          <value>-14.91</value>
          <uncertainty>0.01</uncertainty>
        </latitude>
        <longitude>
          <value>166.95</value>
          <uncertainty>0.01</uncertainty>
        </longitude>
        <depth>
          <value>103000.0</value>
          <uncertainty>800.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C030476A/magnitude#moment_mag">
        <mag>
          <value>6.89</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C030476A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C030476A/magnitude#mb">
        <mag>
          <value>6.4</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C030476A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C030476A/magnitude#MS">
        <mag>
          <value>0.0</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C030476A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C030476A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>190.0</value>
            </strike>
            <dip>
              <value>50.0</value>
            </dip>
            <rake>
              <value>158.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>294.0</value>
            </strike>
            <dip>
              <value>73.0</value>
            </dip>
            <rake>
              <value>42.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>160.0</value>
            </azimuth>
            <plunge>
              <value>41.0</value>
            </plunge>
            <length>
              <value>2.88e+19</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>57.0</value>
            </azimuth>
            <plunge>
              <value>14.0</value>
            </plunge>
            <length>
              <value>-2.67e+19</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>312.0</value>
            </azimuth>
            <plunge>
              <value>46.0</value>
            </plunge>
            <length>
              <value>-2.1e+18</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C030476A/momenttensor">
          <derivedOriginID>smi:local/ndk/C030476A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>11</stationCount>
            <componentCount>31</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>15</stationCount>
            <componentCount>37</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>2.77e+19</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>9.7e+18</value>
              <uncertainty>2e+17</uncertainty>
            </Mrr>
            <Mtt>
              <value>6.6e+18</value>
              <uncertainty>2e+17</uncertainty>
            </Mtt>
            <Mpp>
              <value>-1.63e+19</value>
              <uncertainty>2e+17</uncertainty>
            </Mpp>
            <Mrt>
              <value>-1.75e+19</value>
              <uncertainty>2e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>-3e+17</value>
              <uncertainty>2e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>1.62e+19</value>
              <uncertainty>2e+17</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>13.8</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C030476A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C030476A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C030876A/event">
      <preferredOriginID>smi:local/ndk/C030876A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C030876A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C030876A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>SANTA CRUZ ISLANDS REGION</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C030876A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C030876A/origin#reforigin">
        <time>
          <value>1976-03-08T04:39:55.900000Z</value>
        </time>
        <latitude>
          <value>-10.73</value>
        </latitude>
        <longitude>
          <value>165.02</value>
        </longitude>
        <depth>
          <value>47000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C030876A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C030876A/origin#cmtorigin">
        <time>
          <value>1976-03-08T04:39:57.500000Z</value>
          <uncertainty>0.1</uncertainty>
        </time>
        <latitude>
          <value>-10.87</value>
          <uncertainty>0.01</uncertainty>
        </latitude>
        <longitude>
          <value>164.93</value>
          <uncertainty>0.01</uncertainty>
        </longitude>
        <depth>
          <value>29700.0</value>
          <uncertainty>700.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C030876A/magnitude#moment_mag">
        <mag>
          <value>6.07</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C030876A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C030876A/magnitude#mb">
        <mag>
          <value>6.1</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C030876A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C030876A/magnitude#MS">
        <mag>
          <value>5.9</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C030876A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C030876A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>276.0</value>
            </strike>
            <dip>
              <value>39.0</value>
            </dip>
            <rake>
              <value>73.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>117.0</value>
            </strike>
            <dip>
              <value>53.0</value>
            </dip>
            <rake>
              <value>103.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>73.0</value>
            </azimuth>
            <plunge>
              <value>77.0</value>
            </plunge>
            <length>
              <value>1.49e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>198.0</value>
            </azimuth>
            <plunge>
              <value>7.0</value>
            </plunge>
            <length>
              <value>-1.67e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>289.0</value>
            </azimuth>
            <plunge>
              <value>11.0</value>
            </plunge>
            <length>
              <value>1.7e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C030876A/momenttensor">
          <derivedOriginID>smi:local/ndk/C030876A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>14</stationCount>
            <componentCount>39</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>15</stationCount>
            <componentCount>27</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>1.58e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>1.4e+18</value>
              <uncertainty>2e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>-1.47e+18</value>
              <uncertainty>2e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>7e+16</value>
              <uncertainty>2e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>3.1e+17</value>
              <uncertainty>5e+16</uncertainty>
            </Mrt>
            <Mrp>
              <value>-3.5e+17</value>
              <uncertainty>5e+16</uncertainty>
            </Mrp>
            <Mtp>
              <value>5.1e+17</value>
              <uncertainty>1e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>5.2</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C030876A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C030876A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C031376A/event">
      <preferredOriginID>smi:local/ndk/C031376A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C031376A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C031376A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>SOLOMON ISLANDS</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C031376A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C031376A/origin#reforigin">
        <time>
          <value>1976-03-13T05:22:44.000000Z</value>
        </time>
        <latitude>
          <value>-6.26</value>
        </latitude>
        <longitude>
          <value>154.72</value>
        </longitude>
        <depth>
          <value>50000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C031376A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C031376A/origin#cmtorigin">
        <time>
          <value>1976-03-13T05:22:51.500000Z</value>
          <uncertainty>0.1</uncertainty>
        </time>
        <latitude>
          <value>-6.49</value>
          <uncertainty>0.01</uncertainty>
        </latitude>
        <longitude>
          <value>154.55</value>
          <uncertainty>0.01</uncertainty>
        </longitude>
        <depth>
          <value>47700.0</value>
          <uncertainty>800.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C031376A/magnitude#moment_mag">
        <mag>
          <value>6.16</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C031376A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C031376A/magnitude#mb">
        <mag>
          <value>5.5</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C031376A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C031376A/magnitude#MS">
        <mag>
          <value>6.1</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C031376A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C031376A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>325.0</value>
            </strike>
            <dip>
              <value>41.0</value>
            </dip>
            <rake>
              <value>109.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>121.0</value>
            </strike>
            <dip>
              <value>51.0</value>
            </dip>
            <rake>
              <value>74.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>335.0</value>
            </azimuth>
            <plunge>
              <value>77.0</value>
            </plunge>
            <length>
              <value>2.03e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>222.0</value>
            </azimuth>
            <plunge>
              <value>5.0</value>
            </plunge>
            <length>
              <value>-2.31e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>131.0</value>
            </azimuth>
            <plunge>
              <value>12.0</value>
            </plunge>
            <length>
              <value>2.9e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C031376A/momenttensor">
          <derivedOriginID>smi:local/ndk/C031376A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>13</stationCount>
            <componentCount>36</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>14</stationCount>
            <componentCount>23</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>2.17e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>1.91e+18</value>
              <uncertainty>3e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>-1.07e+18</value>
              <uncertainty>2e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>-8.4e+17</value>
              <uncertainty>3e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>5.3e+17</value>
              <uncertainty>5e+16</uncertainty>
            </Mrt>
            <Mrp>
              <value>0.0</value>
              <uncertainty>4e+16</uncertainty>
            </Mrp>
            <Mtp>
              <value>1.32e+18</value>
              <uncertainty>3e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>5.8</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C031376A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C031376A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C032476A/event">
      <preferredOriginID>smi:local/ndk/C032476A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C032476A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C032476A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>KERMADEC ISLANDS, NEW ZEALAND</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C032476A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C032476A/origin#reforigin">
        <time>
          <value>1976-03-24T04:46:04.400000Z</value>
        </time>
        <latitude>
          <value>-29.89</value>
        </latitude>
        <longitude>
          <value>-177.87</value>
        </longitude>
        <depth>
          <value>33000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C032476A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C032476A/origin#cmtorigin">
        <time>
          <value>1976-03-24T04:46:16.400000Z</value>
          <uncertainty>0.1</uncertainty>
        </time>
        <latitude>
          <value>-29.99</value>
          <uncertainty>0.02</uncertainty>
        </latitude>
        <longitude>
          <value>-177.51</value>
          <uncertainty>0.01</uncertainty>
        </longitude>
        <depth>
          <value>54100.0</value>
          <uncertainty>500.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C032476A/magnitude#moment_mag">
        <mag>
          <value>7.02</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C032476A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C032476A/magnitude#mb">
        <mag>
          <value>6.4</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C032476A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C032476A/magnitude#MS">
        <mag>
          <value>6.8</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C032476A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C032476A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>206.0</value>
            </strike>
            <dip>
              <value>34.0</value>
            </dip>
            <rake>
              <value>103.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>11.0</value>
            </strike>
            <dip>
              <value>57.0</value>
            </dip>
            <rake>
              <value>81.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>254.0</value>
            </azimuth>
            <plunge>
              <value>76.0</value>
            </plunge>
            <length>
              <value>4.09e+19</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>107.0</value>
            </azimuth>
            <plunge>
              <value>12.0</value>
            </plunge>
            <length>
              <value>-4.6e+19</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>15.0</value>
            </azimuth>
            <plunge>
              <value>7.0</value>
            </plunge>
            <length>
              <value>5.1e+18</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C032476A/momenttensor">
          <derivedOriginID>smi:local/ndk/C032476A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>10</stationCount>
            <componentCount>26</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>15</stationCount>
            <componentCount>37</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>4.34e+19</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>3.67e+19</value>
              <uncertainty>4e+17</uncertainty>
            </Mrr>
            <Mtt>
              <value>1.2e+18</value>
              <uncertainty>3e+17</uncertainty>
            </Mtt>
            <Mpp>
              <value>-3.78e+19</value>
              <uncertainty>3e+17</uncertainty>
            </Mpp>
            <Mrt>
              <value>7e+17</value>
              <uncertainty>6e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>1.78e+19</value>
              <uncertainty>5e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>-1.41e+19</value>
              <uncertainty>3e+17</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>16.2</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C032476A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C032476A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C032976A/event">
      <preferredOriginID>smi:local/ndk/C032976A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C032976A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C032976A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>OFF COAST OF CENTRAL AMERICA</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C032976A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C032976A/origin#reforigin">
        <time>
          <value>1976-03-29T05:39:35.500000Z</value>
        </time>
        <latitude>
          <value>3.93</value>
        </latitude>
        <longitude>
          <value>-85.88</value>
        </longitude>
        <depth>
          <value>33000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C032976A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C032976A/origin#cmtorigin">
        <time>
          <value>1976-03-29T05:39:40.400000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>3.87</value>
          <uncertainty>0.01</uncertainty>
        </latitude>
        <longitude>
          <value>-85.8</value>
          <uncertainty>0.01</uncertainty>
        </longitude>
        <depth>
          <value>17500.0</value>
          <uncertainty>1200.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C032976A/magnitude#moment_mag">
        <mag>
          <value>6.6</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C032976A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C032976A/magnitude#mb">
        <mag>
          <value>5.9</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C032976A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C032976A/magnitude#MS">
        <mag>
          <value>6.5</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C032976A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C032976A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>200.0</value>
            </strike>
            <dip>
              <value>79.0</value>
            </dip>
            <rake>
              <value>178.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>290.0</value>
            </strike>
            <dip>
              <value>88.0</value>
            </dip>
            <rake>
              <value>11.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>156.0</value>
            </azimuth>
            <plunge>
              <value>9.0</value>
            </plunge>
            <length>
              <value>1.09e+19</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>65.0</value>
            </azimuth>
            <plunge>
              <value>6.0</value>
            </plunge>
            <length>
              <value>-9.08e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>302.0</value>
            </azimuth>
            <plunge>
              <value>79.0</value>
            </plunge>
            <length>
              <value>-1.82e+18</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C032976A/momenttensor">
          <derivedOriginID>smi:local/ndk/C032976A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>13</stationCount>
            <componentCount>34</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>17</stationCount>
            <componentCount>42</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>9.99e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>-1.58e+18</value>
              <uncertainty>9e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>7.13e+18</value>
              <uncertainty>9e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>-5.55e+18</value>
              <uncertainty>9e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>-2.11e+18</value>
              <uncertainty>3.8e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>-1.5e+17</value>
              <uncertainty>3e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>7.46e+18</value>
              <uncertainty>9e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>9.8</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C032976A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C032976A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C040676A/event">
      <preferredOriginID>smi:local/ndk/C040676A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C040676A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C040676A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>NEW IRELAND REGION, P.N.G.</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C040676A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C040676A/origin#reforigin">
        <time>
          <value>1976-04-06T13:49:10.800000Z</value>
        </time>
        <latitude>
          <value>-3.87</value>
        </latitude>
        <longitude>
          <value>152.09</value>
        </longitude>
        <depth>
          <value>21000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C040676A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C040676A/origin#cmtorigin">
        <time>
          <value>1976-04-06T13:49:20.600000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>-3.72</value>
          <uncertainty>0.01</uncertainty>
        </latitude>
        <longitude>
          <value>152.17</value>
          <uncertainty>0.02</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C040676A/magnitude#moment_mag">
        <mag>
          <value>6.35</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C040676A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C040676A/magnitude#mb">
        <mag>
          <value>5.8</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C040676A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C040676A/magnitude#MS">
        <mag>
          <value>6.4</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C040676A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C040676A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>308.0</value>
            </strike>
            <dip>
              <value>81.0</value>
            </dip>
            <rake>
              <value>-5.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>39.0</value>
            </strike>
            <dip>
              <value>85.0</value>
            </dip>
            <rake>
              <value>-171.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>173.0</value>
            </azimuth>
            <plunge>
              <value>3.0</value>
            </plunge>
            <length>
              <value>4.12e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>264.0</value>
            </azimuth>
            <plunge>
              <value>10.0</value>
            </plunge>
            <length>
              <value>-4.35e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>66.0</value>
            </azimuth>
            <plunge>
              <value>80.0</value>
            </plunge>
            <length>
              <value>2.3e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C040676A/momenttensor">
          <derivedOriginID>smi:local/ndk/C040676A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>13</stationCount>
            <componentCount>31</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>15</stationCount>
            <componentCount>32</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>4.24e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>1.1e+17</value>
              <uncertainty>5e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>4.01e+18</value>
              <uncertainty>4e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>-4.12e+18</value>
              <uncertainty>5e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>-1.2e+17</value>
              <uncertainty>2e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>-7.8e+17</value>
              <uncertainty>2.2e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>9.3e+17</value>
              <uncertainty>4e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>7.4</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C040676A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C040676A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C040876A/event">
      <preferredOriginID>smi:local/ndk/C040876A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C040876A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C040876A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>NORTHWESTERN UZBEKISTAN</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C040876A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C040876A/origin#reforigin">
        <time>
          <value>1976-04-08T02:40:27.000000Z</value>
        </time>
        <latitude>
          <value>40.31</value>
        </latitude>
        <longitude>
          <value>63.77</value>
        </longitude>
        <depth>
          <value>33000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C040876A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C040876A/origin#cmtorigin">
        <time>
          <value>1976-04-08T02:40:33.400000Z</value>
          <uncertainty>0.1</uncertainty>
        </time>
        <latitude>
          <value>40.41</value>
          <uncertainty>0.01</uncertainty>
        </latitude>
        <longitude>
          <value>63.65</value>
          <uncertainty>0.02</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C040876A/magnitude#moment_mag">
        <mag>
          <value>6.64</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C040876A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C040876A/magnitude#mb">
        <mag>
          <value>6.5</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C040876A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C040876A/magnitude#MS">
        <mag>
          <value>7.0</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C040876A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C040876A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>290.0</value>
            </strike>
            <dip>
              <value>46.0</value>
            </dip>
            <rake>
              <value>108.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>84.0</value>
            </strike>
            <dip>
              <value>47.0</value>
            </dip>
            <rake>
              <value>72.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>279.0</value>
            </azimuth>
            <plunge>
              <value>77.0</value>
            </plunge>
            <length>
              <value>1.23e+19</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>187.0</value>
            </azimuth>
            <plunge>
              <value>1.0</value>
            </plunge>
            <length>
              <value>-1.07e+19</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>97.0</value>
            </azimuth>
            <plunge>
              <value>13.0</value>
            </plunge>
            <length>
              <value>-1.6e+18</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C040876A/momenttensor">
          <derivedOriginID>smi:local/ndk/C040876A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>12</stationCount>
            <componentCount>35</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>17</stationCount>
            <componentCount>42</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>1.15e+19</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>1.16e+19</value>
              <uncertainty>1e+17</uncertainty>
            </Mrr>
            <Mtt>
              <value>-1.05e+19</value>
              <uncertainty>1e+17</uncertainty>
            </Mtt>
            <Mpp>
              <value>-1.1e+18</value>
              <uncertainty>1e+17</uncertainty>
            </Mpp>
            <Mrt>
              <value>6e+17</value>
              <uncertainty>4e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>3e+18</value>
              <uncertainty>4e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>1.2e+18</value>
              <uncertainty>1e+17</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>10.2</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C040876A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C040876A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C040876B/event">
      <preferredOriginID>smi:local/ndk/C040876B/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C040876B/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C040876B/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>NORTHWESTERN UZBEKISTAN</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C040876B</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C040876B/origin#reforigin">
        <time>
          <value>1976-04-08T02:59:05.500000Z</value>
        </time>
        <latitude>
          <value>40.17</value>
        </latitude>
        <longitude>
          <value>63.81</value>
        </longitude>
        <depth>
          <value>33000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C040876B/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C040876B/origin#cmtorigin">
        <time>
          <value>1976-04-08T02:59:08.300000Z</value>
          <uncertainty>1.4</uncertainty>
        </time>
        <latitude>
          <value>41.48</value>
          <uncertainty>0.14</uncertainty>
        </latitude>
        <longitude>
          <value>63.54</value>
          <uncertainty>0.15</uncertainty>
        </longitude>
        <depth>
          <value>42900.0</value>
          <uncertainty>5900.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C040876B/magnitude#moment_mag">
        <mag>
          <value>6.1</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C040876B/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C040876B/magnitude#mb">
        <mag>
          <value>6.2</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C040876B/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C040876B/magnitude#MS">
        <mag>
          <value>0.0</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C040876B/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C040876B/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>96.0</value>
            </strike>
            <dip>
              <value>31.0</value>
            </dip>
            <rake>
              <value>130.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>232.0</value>
            </strike>
            <dip>
              <value>66.0</value>
            </dip>
            <rake>
              <value>69.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>108.0</value>
            </azimuth>
            <plunge>
              <value>62.0</value>
            </plunge>
            <length>
              <value>2.04e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>338.0</value>
            </azimuth>
            <plunge>
              <value>19.0</value>
            </plunge>
            <length>
              <value>-1.52e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>241.0</value>
            </azimuth>
            <plunge>
              <value>20.0</value>
            </plunge>
            <length>
              <value>-5.2e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C040876B/momenttensor">
          <derivedOriginID>smi:local/ndk/C040876B/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>4</stationCount>
            <componentCount>6</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>15</stationCount>
            <componentCount>21</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>1.78e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>1.39e+18</value>
              <uncertainty>1.6e+17</uncertainty>
            </Mrr>
            <Mtt>
              <value>-1.23e+18</value>
              <uncertainty>1.4e+17</uncertainty>
            </Mtt>
            <Mpp>
              <value>-1.5e+17</value>
              <uncertainty>1e+17</uncertainty>
            </Mpp>
            <Mrt>
              <value>-6.1e+17</value>
              <uncertainty>3.2e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>-1.12e+18</value>
              <uncertainty>2.8e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>-1.5e+17</value>
              <uncertainty>1e+17</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>5.6</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C040876B/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C040876B/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C040976A/event">
      <preferredOriginID>smi:local/ndk/C040976A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C040976A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C040976A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>NEAR COAST OF ECUADOR</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C040976A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C040976A/origin#reforigin">
        <time>
          <value>1976-04-09T07:08:47.000000Z</value>
        </time>
        <latitude>
          <value>0.78</value>
        </latitude>
        <longitude>
          <value>-79.8</value>
        </longitude>
        <depth>
          <value>9000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C040976A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C040976A/origin#cmtorigin">
        <time>
          <value>1976-04-09T07:08:58.300000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>0.79</value>
          <uncertainty>0.01</uncertainty>
        </latitude>
        <longitude>
          <value>-79.89</value>
          <uncertainty>0.01</uncertainty>
        </longitude>
        <depth>
          <value>19400.0</value>
          <uncertainty>600.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C040976A/magnitude#moment_mag">
        <mag>
          <value>6.63</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C040976A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C040976A/magnitude#mb">
        <mag>
          <value>6.1</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C040976A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C040976A/magnitude#MS">
        <mag>
          <value>6.7</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C040976A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C040976A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>32.0</value>
            </strike>
            <dip>
              <value>22.0</value>
            </dip>
            <rake>
              <value>136.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>164.0</value>
            </strike>
            <dip>
              <value>75.0</value>
            </dip>
            <rake>
              <value>74.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>53.0</value>
            </azimuth>
            <plunge>
              <value>57.0</value>
            </plunge>
            <length>
              <value>1.173e+19</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>267.0</value>
            </azimuth>
            <plunge>
              <value>28.0</value>
            </plunge>
            <length>
              <value>-1.054e+19</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>169.0</value>
            </azimuth>
            <plunge>
              <value>16.0</value>
            </plunge>
            <length>
              <value>-1.19e+18</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C040976A/momenttensor">
          <derivedOriginID>smi:local/ndk/C040976A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>12</stationCount>
            <componentCount>33</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>16</stationCount>
            <componentCount>36</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>1.113e+19</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>5.88e+18</value>
              <uncertainty>7e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>1.9e+17</value>
              <uncertainty>5e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>-6.07e+18</value>
              <uncertainty>7e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>3.75e+18</value>
              <uncertainty>2.5e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>-8.54e+18</value>
              <uncertainty>4.2e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>-1.48e+18</value>
              <uncertainty>4e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>10.2</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C040976A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C040976A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C041076A/event">
      <preferredOriginID>smi:local/ndk/C041076A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C041076A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C041076A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>SOLOMON ISLANDS</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C041076A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C041076A/origin#reforigin">
        <time>
          <value>1976-04-10T04:24:59.400000Z</value>
        </time>
        <latitude>
          <value>-6.43</value>
        </latitude>
        <longitude>
          <value>154.83</value>
        </longitude>
        <depth>
          <value>54000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C041076A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C041076A/origin#cmtorigin">
        <time>
          <value>1976-04-10T04:25:04.300000Z</value>
          <uncertainty>0.5</uncertainty>
        </time>
        <latitude>
          <value>-6.5</value>
          <uncertainty>0.07</uncertainty>
        </latitude>
        <longitude>
          <value>154.63</value>
          <uncertainty>0.07</uncertainty>
        </longitude>
        <depth>
          <value>40600.0</value>
          <uncertainty>6200.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C041076A/magnitude#moment_mag">
        <mag>
          <value>5.32</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C041076A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C041076A/magnitude#mb">
        <mag>
          <value>6.0</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C041076A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C041076A/magnitude#MS">
        <mag>
          <value>0.0</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C041076A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C041076A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>199.0</value>
            </strike>
            <dip>
              <value>49.0</value>
            </dip>
            <rake>
              <value>-32.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>311.0</value>
            </strike>
            <dip>
              <value>67.0</value>
            </dip>
            <rake>
              <value>-134.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>71.0</value>
            </azimuth>
            <plunge>
              <value>11.0</value>
            </plunge>
            <length>
              <value>1.32e+17</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>173.0</value>
            </azimuth>
            <plunge>
              <value>48.0</value>
            </plunge>
            <length>
              <value>-1.11e+17</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>332.0</value>
            </azimuth>
            <plunge>
              <value>40.0</value>
            </plunge>
            <length>
              <value>-2.1e+16</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C041076A/momenttensor">
          <derivedOriginID>smi:local/ndk/C041076A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>8</stationCount>
            <componentCount>20</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>2</stationCount>
            <componentCount>3</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>1.22e+17</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>-6.6e+16</value>
              <uncertainty>7e+15</uncertainty>
            </Mrr>
            <Mtt>
              <value>-4.5e+16</value>
              <uncertainty>1.5e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>1.1e+17</value>
              <uncertainty>1e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>5.4e+16</value>
              <uncertainty>1.2e+16</uncertainty>
            </Mrt>
            <Mrp>
              <value>-2.2e+16</value>
              <uncertainty>1.6e+16</uncertainty>
            </Mrp>
            <Mtp>
              <value>-5e+16</value>
              <uncertainty>6e+15</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>2.2</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C041076A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C041076A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C041476A/event">
      <preferredOriginID>smi:local/ndk/C041476A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C041476A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C041476A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>WEST OF MACQUARIE ISLAND</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C041476A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C041476A/origin#reforigin">
        <time>
          <value>1976-04-14T15:26:16.800000Z</value>
        </time>
        <latitude>
          <value>-51.9</value>
        </latitude>
        <longitude>
          <value>139.47</value>
        </longitude>
        <depth>
          <value>33000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C041476A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C041476A/origin#cmtorigin">
        <time>
          <value>1976-04-14T15:26:18.900000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>-52.1</value>
          <uncertainty>0.02</uncertainty>
        </latitude>
        <longitude>
          <value>139.46</value>
          <uncertainty>0.03</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C041476A/magnitude#moment_mag">
        <mag>
          <value>6.03</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C041476A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C041476A/magnitude#mb">
        <mag>
          <value>5.4</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C041476A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C041476A/magnitude#MS">
        <mag>
          <value>6.2</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C041476A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C041476A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>180.0</value>
            </strike>
            <dip>
              <value>89.0</value>
            </dip>
            <rake>
              <value>0.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>90.0</value>
            </strike>
            <dip>
              <value>90.0</value>
            </dip>
            <rake>
              <value>179.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>45.0</value>
            </azimuth>
            <plunge>
              <value>1.0</value>
            </plunge>
            <length>
              <value>1.47e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>135.0</value>
            </azimuth>
            <plunge>
              <value>0.0</value>
            </plunge>
            <length>
              <value>-1.34e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>261.0</value>
            </azimuth>
            <plunge>
              <value>89.0</value>
            </plunge>
            <length>
              <value>-1.2e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C041476A/momenttensor">
          <derivedOriginID>smi:local/ndk/C041476A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>13</stationCount>
            <componentCount>34</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>14</stationCount>
            <componentCount>25</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>1.4e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>-1.2e+17</value>
              <uncertainty>2e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>5e+16</value>
              <uncertainty>2e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>7e+16</value>
              <uncertainty>2e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>2e+16</value>
              <uncertainty>6e+16</uncertainty>
            </Mrt>
            <Mrp>
              <value>0.0</value>
              <uncertainty>6e+16</uncertainty>
            </Mrp>
            <Mtp>
              <value>-1.4e+18</value>
              <uncertainty>2e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>5.2</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C041476A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C041476A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C042276A/event">
      <preferredOriginID>smi:local/ndk/C042276A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C042276A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C042276A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>SOUTHERN IRAN</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C042276A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C042276A/origin#reforigin">
        <time>
          <value>1976-04-22T17:03:07.900000Z</value>
        </time>
        <latitude>
          <value>28.71</value>
        </latitude>
        <longitude>
          <value>52.13</value>
        </longitude>
        <depth>
          <value>24000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C042276A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C042276A/origin#cmtorigin">
        <time>
          <value>1976-04-22T17:03:10.600000Z</value>
          <uncertainty>0.4</uncertainty>
        </time>
        <latitude>
          <value>28.49</value>
          <uncertainty>0.05</uncertainty>
        </latitude>
        <longitude>
          <value>52.08</value>
          <uncertainty>0.03</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C042276A/magnitude#moment_mag">
        <mag>
          <value>5.64</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C042276A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C042276A/magnitude#mb">
        <mag>
          <value>6.0</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C042276A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C042276A/magnitude#MS">
        <mag>
          <value>5.5</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C042276A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C042276A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>141.0</value>
            </strike>
            <dip>
              <value>41.0</value>
            </dip>
            <rake>
              <value>98.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>310.0</value>
            </strike>
            <dip>
              <value>49.0</value>
            </dip>
            <rake>
              <value>83.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>170.0</value>
            </azimuth>
            <plunge>
              <value>83.0</value>
            </plunge>
            <length>
              <value>3.85e+17</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>45.0</value>
            </azimuth>
            <plunge>
              <value>4.0</value>
            </plunge>
            <length>
              <value>-3.47e+17</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>315.0</value>
            </azimuth>
            <plunge>
              <value>6.0</value>
            </plunge>
            <length>
              <value>-3.8e+16</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C042276A/momenttensor">
          <derivedOriginID>smi:local/ndk/C042276A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>11</stationCount>
            <componentCount>25</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>7</stationCount>
            <componentCount>9</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>3.66e+17</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>3.77e+17</value>
              <uncertainty>1e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>-1.83e+17</value>
              <uncertainty>1.4e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>-1.94e+17</value>
              <uncertainty>1e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>-6.3e+16</value>
              <uncertainty>4.1e+16</uncertainty>
            </Mrt>
            <Mrp>
              <value>6e+15</value>
              <uncertainty>4.1e+16</uncertainty>
            </Mrp>
            <Mtp>
              <value>1.55e+17</value>
              <uncertainty>1e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>3.2</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C042276A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C042276A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C042976A/event">
      <preferredOriginID>smi:local/ndk/C042976A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C042976A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C042976A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>KERMADEC ISLANDS REGION</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C042976A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C042976A/origin#reforigin">
        <time>
          <value>1976-04-29T06:32:49.000000Z</value>
        </time>
        <latitude>
          <value>-28.2</value>
        </latitude>
        <longitude>
          <value>-176.88</value>
        </longitude>
        <depth>
          <value>62000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C042976A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C042976A/origin#cmtorigin">
        <time>
          <value>1976-04-29T06:32:51.400000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>-28.06</value>
          <uncertainty>0.03</uncertainty>
        </latitude>
        <longitude>
          <value>-176.35</value>
          <uncertainty>0.02</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C042976A/magnitude#moment_mag">
        <mag>
          <value>6.15</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C042976A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C042976A/magnitude#mb">
        <mag>
          <value>5.3</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C042976A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C042976A/magnitude#MS">
        <mag>
          <value>6.1</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C042976A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C042976A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>182.0</value>
            </strike>
            <dip>
              <value>26.0</value>
            </dip>
            <rake>
              <value>75.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>18.0</value>
            </strike>
            <dip>
              <value>65.0</value>
            </dip>
            <rake>
              <value>97.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>302.0</value>
            </azimuth>
            <plunge>
              <value>69.0</value>
            </plunge>
            <length>
              <value>1.99e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>103.0</value>
            </azimuth>
            <plunge>
              <value>20.0</value>
            </plunge>
            <length>
              <value>-2.22e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>195.0</value>
            </azimuth>
            <plunge>
              <value>6.0</value>
            </plunge>
            <length>
              <value>2.4e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C042976A/momenttensor">
          <derivedOriginID>smi:local/ndk/C042976A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>10</stationCount>
            <componentCount>28</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>13</stationCount>
            <componentCount>26</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>2.11e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>1.49e+18</value>
              <uncertainty>3e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>1.9e+17</value>
              <uncertainty>3e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>-1.68e+18</value>
              <uncertainty>2e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>4.8e+17</value>
              <uncertainty>1.1e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>1.26e+18</value>
              <uncertainty>1.3e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>-3.6e+17</value>
              <uncertainty>3e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>5.8</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C042976A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C042976A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C050476A/event">
      <preferredOriginID>smi:local/ndk/C050476A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C050476A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C050476A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>SOUTH ISLAND, NEW ZEALAND</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C050476A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C050476A/origin#reforigin">
        <time>
          <value>1976-05-04T13:56:29.900000Z</value>
        </time>
        <latitude>
          <value>-44.64</value>
        </latitude>
        <longitude>
          <value>167.57</value>
        </longitude>
        <depth>
          <value>19000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C050476A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C050476A/origin#cmtorigin">
        <time>
          <value>1976-05-04T13:56:36.200000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>-44.75</value>
          <uncertainty>0.02</uncertainty>
        </latitude>
        <longitude>
          <value>167.63</value>
          <uncertainty>0.02</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C050476A/magnitude#moment_mag">
        <mag>
          <value>6.53</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C050476A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C050476A/magnitude#mb">
        <mag>
          <value>6.0</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C050476A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C050476A/magnitude#MS">
        <mag>
          <value>6.6</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C050476A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C050476A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>57.0</value>
            </strike>
            <dip>
              <value>18.0</value>
            </dip>
            <rake>
              <value>136.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>189.0</value>
            </strike>
            <dip>
              <value>77.0</value>
            </dip>
            <rake>
              <value>77.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>83.0</value>
            </azimuth>
            <plunge>
              <value>56.0</value>
            </plunge>
            <length>
              <value>7.64e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>290.0</value>
            </azimuth>
            <plunge>
              <value>31.0</value>
            </plunge>
            <length>
              <value>-8.27e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>192.0</value>
            </azimuth>
            <plunge>
              <value>13.0</value>
            </plunge>
            <length>
              <value>6.3e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C050476A/momenttensor">
          <derivedOriginID>smi:local/ndk/C050476A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>9</stationCount>
            <componentCount>25</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>14</stationCount>
            <componentCount>29</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>7.96e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>3.03e+18</value>
              <uncertainty>6e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>-1.2e+17</value>
              <uncertainty>7e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>-2.91e+18</value>
              <uncertainty>4e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>-9.5e+17</value>
              <uncertainty>2.5e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>-6.94e+18</value>
              <uncertainty>2.4e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>-2.4e+18</value>
              <uncertainty>4e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>8.4</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C050476A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C050476A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C050576A/event">
      <preferredOriginID>smi:local/ndk/C050576A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C050576A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C050576A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>KERMADEC ISLANDS, NEW ZEALAND</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C050576A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C050576A/origin#reforigin">
        <time>
          <value>1976-05-05T04:52:51.000000Z</value>
        </time>
        <latitude>
          <value>-29.93</value>
        </latitude>
        <longitude>
          <value>-177.84</value>
        </longitude>
        <depth>
          <value>35000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C050576A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C050576A/origin#cmtorigin">
        <time>
          <value>1976-05-05T04:53:02.600000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>-29.84</value>
          <uncertainty>0.02</uncertainty>
        </latitude>
        <longitude>
          <value>-177.43</value>
          <uncertainty>0.01</uncertainty>
        </longitude>
        <depth>
          <value>41800.0</value>
          <uncertainty>600.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C050576A/magnitude#moment_mag">
        <mag>
          <value>7.03</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C050576A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C050576A/magnitude#mb">
        <mag>
          <value>6.2</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C050576A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C050576A/magnitude#MS">
        <mag>
          <value>6.8</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C050576A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C050576A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>211.0</value>
            </strike>
            <dip>
              <value>34.0</value>
            </dip>
            <rake>
              <value>105.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>13.0</value>
            </strike>
            <dip>
              <value>57.0</value>
            </dip>
            <rake>
              <value>80.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>254.0</value>
            </azimuth>
            <plunge>
              <value>75.0</value>
            </plunge>
            <length>
              <value>4.06e+19</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>111.0</value>
            </azimuth>
            <plunge>
              <value>12.0</value>
            </plunge>
            <length>
              <value>-4.72e+19</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>19.0</value>
            </azimuth>
            <plunge>
              <value>8.0</value>
            </plunge>
            <length>
              <value>6.6e+18</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C050576A/momenttensor">
          <derivedOriginID>smi:local/ndk/C050576A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>10</stationCount>
            <componentCount>26</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>14</stationCount>
            <componentCount>35</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>4.39e+19</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>3.63e+19</value>
              <uncertainty>5e+17</uncertainty>
            </Mrr>
            <Mtt>
              <value>4e+17</value>
              <uncertainty>3e+17</uncertainty>
            </Mtt>
            <Mpp>
              <value>-3.66e+19</value>
              <uncertainty>4e+17</uncertainty>
            </Mpp>
            <Mrt>
              <value>1.5e+18</value>
              <uncertainty>8e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>1.8e+19</value>
              <uncertainty>8e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>-1.75e+19</value>
              <uncertainty>3e+17</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>15.8</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C050576A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C050576A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C050676A/event">
      <preferredOriginID>smi:local/ndk/C050676A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C050676A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C050676A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>AUSTRIA</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C050676A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C050676A/origin#reforigin">
        <time>
          <value>1976-05-06T20:00:11.600000Z</value>
        </time>
        <latitude>
          <value>46.36</value>
        </latitude>
        <longitude>
          <value>13.27</value>
        </longitude>
        <depth>
          <value>9000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C050676A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C050676A/origin#cmtorigin">
        <time>
          <value>1976-05-06T20:00:21.900000Z</value>
          <uncertainty>0.3</uncertainty>
        </time>
        <latitude>
          <value>46.33</value>
          <uncertainty>0.03</uncertainty>
        </latitude>
        <longitude>
          <value>13.17</value>
          <uncertainty>0.02</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C050676A/magnitude#moment_mag">
        <mag>
          <value>6.47</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C050676A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C050676A/magnitude#mb">
        <mag>
          <value>6.0</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C050676A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C050676A/magnitude#MS">
        <mag>
          <value>6.5</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C050676A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C050676A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>284.0</value>
            </strike>
            <dip>
              <value>18.0</value>
            </dip>
            <rake>
              <value>119.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>74.0</value>
            </strike>
            <dip>
              <value>74.0</value>
            </dip>
            <rake>
              <value>81.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>332.0</value>
            </azimuth>
            <plunge>
              <value>60.0</value>
            </plunge>
            <length>
              <value>6.45e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>172.0</value>
            </azimuth>
            <plunge>
              <value>29.0</value>
            </plunge>
            <length>
              <value>-6.21e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>77.0</value>
            </azimuth>
            <plunge>
              <value>9.0</value>
            </plunge>
            <length>
              <value>-2.4e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C050676A/momenttensor">
          <derivedOriginID>smi:local/ndk/C050676A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>10</stationCount>
            <componentCount>24</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>13</stationCount>
            <componentCount>26</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>6.33e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>3.36e+18</value>
              <uncertainty>5e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>-3.4e+18</value>
              <uncertainty>5e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>4e+16</value>
              <uncertainty>3e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>5.06e+18</value>
              <uncertainty>2e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>1.74e+18</value>
              <uncertainty>1.7e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>4e+16</value>
              <uncertainty>3e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>8.4</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C050676A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C050676A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C051176A/event">
      <preferredOriginID>smi:local/ndk/C051176A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C051176A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C051176A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>WESTERN INDIAN-ANTARCTIC RIDGE</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C051176A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C051176A/origin#reforigin">
        <time>
          <value>1976-05-11T11:29:06.200000Z</value>
        </time>
        <latitude>
          <value>-51.51</value>
        </latitude>
        <longitude>
          <value>139.68</value>
        </longitude>
        <depth>
          <value>33000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C051176A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C051176A/origin#cmtorigin">
        <time>
          <value>1976-05-11T11:29:08.600000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>-51.73</value>
          <uncertainty>0.02</uncertainty>
        </latitude>
        <longitude>
          <value>139.71</value>
          <uncertainty>0.03</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C051176A/magnitude#moment_mag">
        <mag>
          <value>5.9</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C051176A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C051176A/magnitude#mb">
        <mag>
          <value>5.6</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C051176A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C051176A/magnitude#MS">
        <mag>
          <value>6.1</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C051176A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C051176A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>271.0</value>
            </strike>
            <dip>
              <value>73.0</value>
            </dip>
            <rake>
              <value>-167.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>177.0</value>
            </strike>
            <dip>
              <value>77.0</value>
            </dip>
            <rake>
              <value>-17.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>224.0</value>
            </azimuth>
            <plunge>
              <value>3.0</value>
            </plunge>
            <length>
              <value>8.51e+17</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>133.0</value>
            </azimuth>
            <plunge>
              <value>21.0</value>
            </plunge>
            <length>
              <value>-9.27e+17</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>322.0</value>
            </azimuth>
            <plunge>
              <value>69.0</value>
            </plunge>
            <length>
              <value>7.6e+16</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C051176A/momenttensor">
          <derivedOriginID>smi:local/ndk/C051176A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>12</stationCount>
            <componentCount>29</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>15</stationCount>
            <componentCount>26</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>8.89e+17</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>-5.2e+16</value>
              <uncertainty>1.2e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>6.7e+16</value>
              <uncertainty>1.3e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>-1.5e+16</value>
              <uncertainty>1.2e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>2.02e+17</value>
              <uncertainty>4.1e+16</uncertainty>
            </Mrt>
            <Mrp>
              <value>2.74e+17</value>
              <uncertainty>3.7e+16</uncertainty>
            </Mrp>
            <Mtp>
              <value>-8.22e+17</value>
              <uncertainty>1.1e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>4.4</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C051176A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C051176A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/B051176B/event">
      <preferredOriginID>smi:local/ndk/B051176B/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/B051176B/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/B051176B/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>WESTERN INDIAN-ANTARCTIC RIDGE</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>B051176B</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/B051176B/origin#reforigin">
        <time>
          <value>1976-05-11T15:50:41.600000Z</value>
        </time>
        <latitude>
          <value>-51.6</value>
        </latitude>
        <longitude>
          <value>139.68</value>
        </longitude>
        <depth>
          <value>33000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/B051176B/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/B051176B/origin#cmtorigin">
        <time>
          <value>1976-05-11T15:50:37.600000Z</value>
          <uncertainty>0.4</uncertainty>
        </time>
        <latitude>
          <value>-51.67</value>
          <uncertainty>0.04</uncertainty>
        </latitude>
        <longitude>
          <value>140.13</value>
          <uncertainty>0.05</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/B051176B/magnitude#moment_mag">
        <mag>
          <value>6.35</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/B051176B/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/B051176B/magnitude#mb">
        <mag>
          <value>5.8</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/B051176B/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/B051176B/magnitude#MS">
        <mag>
          <value>6.6</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/B051176B/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/B051176B/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>358.0</value>
            </strike>
            <dip>
              <value>76.0</value>
            </dip>
            <rake>
              <value>11.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>266.0</value>
            </strike>
            <dip>
              <value>79.0</value>
            </dip>
            <rake>
              <value>166.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>222.0</value>
            </azimuth>
            <plunge>
              <value>17.0</value>
            </plunge>
            <length>
              <value>4.44e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>312.0</value>
            </azimuth>
            <plunge>
              <value>2.0</value>
            </plunge>
            <length>
              <value>-3.95e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>49.0</value>
            </azimuth>
            <plunge>
              <value>73.0</value>
            </plunge>
            <length>
              <value>-4.9e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/B051176B/momenttensor">
          <derivedOriginID>smi:local/ndk/B051176B/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>12</stationCount>
            <componentCount>27</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>4.19e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>-6e+16</value>
              <uncertainty>7e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>4.7e+17</value>
              <uncertainty>9e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>-4e+17</value>
              <uncertainty>8e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>-1.12e+18</value>
              <uncertainty>1.7e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>8.4e+17</value>
              <uncertainty>1.4e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>-3.95e+18</value>
              <uncertainty>1e+17</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>7.0</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/B051176B/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/B051176B/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C051176C/event">
      <preferredOriginID>smi:local/ndk/C051176C/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C051176C/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C051176C/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>CENTRAL MEDITERRANEAN SEA</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C051176C</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C051176C/origin#reforigin">
        <time>
          <value>1976-05-11T16:59:48.200000Z</value>
        </time>
        <latitude>
          <value>37.56</value>
        </latitude>
        <longitude>
          <value>20.35</value>
        </longitude>
        <depth>
          <value>33000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C051176C/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C051176C/origin#cmtorigin">
        <time>
          <value>1976-05-11T16:59:53.500000Z</value>
          <uncertainty>0.4</uncertainty>
        </time>
        <latitude>
          <value>36.99</value>
          <uncertainty>0.04</uncertainty>
        </latitude>
        <longitude>
          <value>20.13</value>
          <uncertainty>0.03</uncertainty>
        </longitude>
        <depth>
          <value>15100.0</value>
          <uncertainty>1500.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C051176C/magnitude#moment_mag">
        <mag>
          <value>6.42</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C051176C/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C051176C/magnitude#mb">
        <mag>
          <value>5.8</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C051176C/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C051176C/magnitude#MS">
        <mag>
          <value>6.4</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C051176C/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C051176C/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>339.0</value>
            </strike>
            <dip>
              <value>14.0</value>
            </dip>
            <rake>
              <value>110.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>139.0</value>
            </strike>
            <dip>
              <value>77.0</value>
            </dip>
            <rake>
              <value>85.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>42.0</value>
            </azimuth>
            <plunge>
              <value>58.0</value>
            </plunge>
            <length>
              <value>5.51e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>233.0</value>
            </azimuth>
            <plunge>
              <value>31.0</value>
            </plunge>
            <length>
              <value>-5.24e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>140.0</value>
            </azimuth>
            <plunge>
              <value>5.0</value>
            </plunge>
            <length>
              <value>-2.7e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C051176C/momenttensor">
          <derivedOriginID>smi:local/ndk/C051176C/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>11</stationCount>
            <componentCount>30</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>15</stationCount>
            <componentCount>27</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>5.37e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>2.55e+18</value>
              <uncertainty>8e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>-7.1e+17</value>
              <uncertainty>8e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>-1.84e+18</value>
              <uncertainty>6e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>3.27e+18</value>
              <uncertainty>4.8e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>-3.48e+18</value>
              <uncertainty>5.3e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>9.5e+17</value>
              <uncertainty>5e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>7.8</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C051176C/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C051176C/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C051576A/event">
      <preferredOriginID>smi:local/ndk/C051576A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C051576A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C051576A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>CENTRAL PERU</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C051576A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C051576A/origin#reforigin">
        <time>
          <value>1976-05-15T21:55:58.500000Z</value>
        </time>
        <latitude>
          <value>-11.64</value>
        </latitude>
        <longitude>
          <value>-74.48</value>
        </longitude>
        <depth>
          <value>33000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C051576A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C051576A/origin#cmtorigin">
        <time>
          <value>1976-05-15T21:56:05.000000Z</value>
          <uncertainty>0.1</uncertainty>
        </time>
        <latitude>
          <value>-11.72</value>
          <uncertainty>0.01</uncertainty>
        </latitude>
        <longitude>
          <value>-74.26</value>
          <uncertainty>0.02</uncertainty>
        </longitude>
        <depth>
          <value>25500.0</value>
          <uncertainty>800.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C051576A/magnitude#moment_mag">
        <mag>
          <value>6.74</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C051576A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C051576A/magnitude#mb">
        <mag>
          <value>6.0</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C051576A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C051576A/magnitude#MS">
        <mag>
          <value>6.6</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C051576A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C051576A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>153.0</value>
            </strike>
            <dip>
              <value>15.0</value>
            </dip>
            <rake>
              <value>77.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>347.0</value>
            </strike>
            <dip>
              <value>76.0</value>
            </dip>
            <rake>
              <value>93.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>262.0</value>
            </azimuth>
            <plunge>
              <value>59.0</value>
            </plunge>
            <length>
              <value>1.64e+19</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>74.0</value>
            </azimuth>
            <plunge>
              <value>31.0</value>
            </plunge>
            <length>
              <value>-1.67e+19</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>166.0</value>
            </azimuth>
            <plunge>
              <value>3.0</value>
            </plunge>
            <length>
              <value>3e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C051576A/momenttensor">
          <derivedOriginID>smi:local/ndk/C051576A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>13</stationCount>
            <componentCount>32</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>15</stationCount>
            <componentCount>37</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>1.65e+19</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>7.8e+18</value>
              <uncertainty>1e+17</uncertainty>
            </Mrr>
            <Mtt>
              <value>-5e+17</value>
              <uncertainty>1e+17</uncertainty>
            </Mtt>
            <Mpp>
              <value>-7.3e+18</value>
              <uncertainty>1e+17</uncertainty>
            </Mpp>
            <Mrt>
              <value>-3.1e+18</value>
              <uncertainty>3e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>1.41e+19</value>
              <uncertainty>6e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>2.7e+18</value>
              <uncertainty>1e+17</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>11.4</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C051576A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C051576A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C051776A/event">
      <preferredOriginID>smi:local/ndk/C051776A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C051776A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C051776A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>NORTHWESTERN UZBEKISTAN</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C051776A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C051776A/origin#reforigin">
        <time>
          <value>1976-05-17T02:58:40.600000Z</value>
        </time>
        <latitude>
          <value>40.38</value>
        </latitude>
        <longitude>
          <value>63.47</value>
        </longitude>
        <depth>
          <value>10000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C051776A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C051776A/origin#cmtorigin">
        <time>
          <value>1976-05-17T02:58:48.900000Z</value>
          <uncertainty>0.1</uncertainty>
        </time>
        <latitude>
          <value>40.42</value>
          <uncertainty>0.01</uncertainty>
        </latitude>
        <longitude>
          <value>63.46</value>
          <uncertainty>0.02</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C051776A/magnitude#moment_mag">
        <mag>
          <value>6.7</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C051776A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C051776A/magnitude#mb">
        <mag>
          <value>6.3</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C051776A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C051776A/magnitude#MS">
        <mag>
          <value>7.0</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C051776A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C051776A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>225.0</value>
            </strike>
            <dip>
              <value>36.0</value>
            </dip>
            <rake>
              <value>85.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>51.0</value>
            </strike>
            <dip>
              <value>54.0</value>
            </dip>
            <rake>
              <value>93.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>335.0</value>
            </azimuth>
            <plunge>
              <value>80.0</value>
            </plunge>
            <length>
              <value>1.51e+19</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>139.0</value>
            </azimuth>
            <plunge>
              <value>9.0</value>
            </plunge>
            <length>
              <value>-1.29e+19</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>229.0</value>
            </azimuth>
            <plunge>
              <value>3.0</value>
            </plunge>
            <length>
              <value>-2.2e+18</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C051776A/momenttensor">
          <derivedOriginID>smi:local/ndk/C051776A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>12</stationCount>
            <componentCount>35</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>17</stationCount>
            <componentCount>41</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>1.4e+19</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>1.44e+19</value>
              <uncertainty>1e+17</uncertainty>
            </Mrr>
            <Mtt>
              <value>-7.7e+18</value>
              <uncertainty>1e+17</uncertainty>
            </Mtt>
            <Mpp>
              <value>-6.7e+18</value>
              <uncertainty>1e+17</uncertainty>
            </Mpp>
            <Mrt>
              <value>3.9e+18</value>
              <uncertainty>6e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>2.3e+18</value>
              <uncertainty>6e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>-5e+18</value>
              <uncertainty>1e+17</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>11.0</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C051776A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C051776A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C051876A/event">
      <preferredOriginID>smi:local/ndk/C051876A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C051876A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C051876A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>WEST OF MACQUARIE ISLAND</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C051876A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C051876A/origin#reforigin">
        <time>
          <value>1976-05-18T06:04:47.000000Z</value>
        </time>
        <latitude>
          <value>-59.95</value>
        </latitude>
        <longitude>
          <value>154.08</value>
        </longitude>
        <depth>
          <value>33000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C051876A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C051876A/origin#cmtorigin">
        <time>
          <value>1976-05-18T06:04:55.200000Z</value>
          <uncertainty>0.1</uncertainty>
        </time>
        <latitude>
          <value>-60.73</value>
          <uncertainty>0.01</uncertainty>
        </latitude>
        <longitude>
          <value>153.75</value>
          <uncertainty>0.02</uncertainty>
        </longitude>
        <depth>
          <value>25800.0</value>
          <uncertainty>1000.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C051876A/magnitude#moment_mag">
        <mag>
          <value>6.36</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C051876A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C051876A/magnitude#mb">
        <mag>
          <value>5.3</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C051876A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C051876A/magnitude#MS">
        <mag>
          <value>6.2</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C051876A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C051876A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>158.0</value>
            </strike>
            <dip>
              <value>76.0</value>
            </dip>
            <rake>
              <value>-2.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>248.0</value>
            </strike>
            <dip>
              <value>88.0</value>
            </dip>
            <rake>
              <value>-166.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>22.0</value>
            </azimuth>
            <plunge>
              <value>8.0</value>
            </plunge>
            <length>
              <value>4.44e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>114.0</value>
            </azimuth>
            <plunge>
              <value>11.0</value>
            </plunge>
            <length>
              <value>-4.29e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>255.0</value>
            </azimuth>
            <plunge>
              <value>76.0</value>
            </plunge>
            <length>
              <value>-1.4e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C051876A/momenttensor">
          <derivedOriginID>smi:local/ndk/C051876A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>14</stationCount>
            <componentCount>36</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>14</stationCount>
            <componentCount>27</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>4.37e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>-1.9e+17</value>
              <uncertainty>3e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>3.06e+18</value>
              <uncertainty>4e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>-2.87e+18</value>
              <uncertainty>4e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>9.1e+17</value>
              <uncertainty>1.2e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>4.4e+17</value>
              <uncertainty>1e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>-3.04e+18</value>
              <uncertainty>3e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>7.4</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C051876A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C051876A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C052976A/event">
      <preferredOriginID>smi:local/ndk/C052976A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C052976A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C052976A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>MYANMAR-CHINA BORDER REGION</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C052976A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C052976A/origin#reforigin">
        <time>
          <value>1976-05-29T12:23:18.700000Z</value>
        </time>
        <latitude>
          <value>24.57</value>
        </latitude>
        <longitude>
          <value>98.95</value>
        </longitude>
        <depth>
          <value>8000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C052976A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C052976A/origin#cmtorigin">
        <time>
          <value>1976-05-29T12:23:29.900000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>24.39</value>
          <uncertainty>0.02</uncertainty>
        </latitude>
        <longitude>
          <value>98.65</value>
          <uncertainty>0.03</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C052976A/magnitude#moment_mag">
        <mag>
          <value>6.66</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C052976A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C052976A/magnitude#mb">
        <mag>
          <value>6.1</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C052976A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C052976A/magnitude#MS">
        <mag>
          <value>6.9</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C052976A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C052976A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>323.0</value>
            </strike>
            <dip>
              <value>80.0</value>
            </dip>
            <rake>
              <value>-172.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>232.0</value>
            </strike>
            <dip>
              <value>82.0</value>
            </dip>
            <rake>
              <value>-10.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>278.0</value>
            </azimuth>
            <plunge>
              <value>1.0</value>
            </plunge>
            <length>
              <value>1.2e+19</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>187.0</value>
            </azimuth>
            <plunge>
              <value>13.0</value>
            </plunge>
            <length>
              <value>-1.25e+19</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>13.0</value>
            </azimuth>
            <plunge>
              <value>77.0</value>
            </plunge>
            <length>
              <value>5e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C052976A/momenttensor">
          <derivedOriginID>smi:local/ndk/C052976A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>12</stationCount>
            <componentCount>31</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>15</stationCount>
            <componentCount>34</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>1.22e+19</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>-1e+17</value>
              <uncertainty>2e+17</uncertainty>
            </Mrr>
            <Mtt>
              <value>-1.15e+19</value>
              <uncertainty>2e+17</uncertainty>
            </Mtt>
            <Mpp>
              <value>1.15e+19</value>
              <uncertainty>2e+17</uncertainty>
            </Mpp>
            <Mrt>
              <value>2.8e+18</value>
              <uncertainty>8e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>-1e+17</value>
              <uncertainty>9e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>3.1e+18</value>
              <uncertainty>2e+17</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>10.6</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C052976A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C052976A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/B052976B/event">
      <preferredOriginID>smi:local/ndk/B052976B/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/B052976B/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/B052976B/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>MYANMAR-CHINA BORDER REGION</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>B052976B</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/B052976B/origin#reforigin">
        <time>
          <value>1976-05-29T14:00:18.500000Z</value>
        </time>
        <latitude>
          <value>24.53</value>
        </latitude>
        <longitude>
          <value>98.71</value>
        </longitude>
        <depth>
          <value>10000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/B052976B/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/B052976B/origin#cmtorigin">
        <time>
          <value>1976-05-29T14:00:33.200000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>24.29</value>
          <uncertainty>0.03</uncertainty>
        </latitude>
        <longitude>
          <value>98.58</value>
          <uncertainty>0.03</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/B052976B/magnitude#moment_mag">
        <mag>
          <value>6.63</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/B052976B/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/B052976B/magnitude#mb">
        <mag>
          <value>6.0</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/B052976B/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/B052976B/magnitude#MS">
        <mag>
          <value>7.0</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/B052976B/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/B052976B/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>242.0</value>
            </strike>
            <dip>
              <value>88.0</value>
            </dip>
            <rake>
              <value>0.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>152.0</value>
            </strike>
            <dip>
              <value>90.0</value>
            </dip>
            <rake>
              <value>178.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>107.0</value>
            </azimuth>
            <plunge>
              <value>1.0</value>
            </plunge>
            <length>
              <value>1.109e+19</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>197.0</value>
            </azimuth>
            <plunge>
              <value>1.0</value>
            </plunge>
            <length>
              <value>-1.131e+19</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>328.0</value>
            </azimuth>
            <plunge>
              <value>88.0</value>
            </plunge>
            <length>
              <value>2.2e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/B052976B/momenttensor">
          <derivedOriginID>smi:local/ndk/B052976B/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>10</stationCount>
            <componentCount>22</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>1.12e+19</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>2.2e+17</value>
              <uncertainty>3.1e+17</uncertainty>
            </Mrr>
            <Mtt>
              <value>-9.45e+18</value>
              <uncertainty>2.9e+17</uncertainty>
            </Mtt>
            <Mpp>
              <value>9.23e+18</value>
              <uncertainty>3.5e+17</uncertainty>
            </Mpp>
            <Mrt>
              <value>1.6e+17</value>
              <uncertainty>8.1e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>-3.2e+17</value>
              <uncertainty>1.07e+18</uncertainty>
            </Mrp>
            <Mtp>
              <value>6.18e+18</value>
              <uncertainty>3.8e+17</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>10.8</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/B052976B/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/B052976B/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C053076A/event">
      <preferredOriginID>smi:local/ndk/C053076A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C053076A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C053076A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>OFF COAST OF SOUTHERN CHILE</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C053076A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C053076A/origin#reforigin">
        <time>
          <value>1976-05-30T03:08:54.200000Z</value>
        </time>
        <latitude>
          <value>-41.64</value>
        </latitude>
        <longitude>
          <value>-75.41</value>
        </longitude>
        <depth>
          <value>28000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C053076A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C053076A/origin#cmtorigin">
        <time>
          <value>1976-05-30T03:08:55.400000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>-42.06</value>
          <uncertainty>0.02</uncertainty>
        </latitude>
        <longitude>
          <value>-75.94</value>
          <uncertainty>0.02</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C053076A/magnitude#moment_mag">
        <mag>
          <value>6.09</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C053076A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C053076A/magnitude#mb">
        <mag>
          <value>6.0</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C053076A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C053076A/magnitude#MS">
        <mag>
          <value>5.9</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C053076A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C053076A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>187.0</value>
            </strike>
            <dip>
              <value>44.0</value>
            </dip>
            <rake>
              <value>-101.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>23.0</value>
            </strike>
            <dip>
              <value>47.0</value>
            </dip>
            <rake>
              <value>-79.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>105.0</value>
            </azimuth>
            <plunge>
              <value>2.0</value>
            </plunge>
            <length>
              <value>1.7e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>4.0</value>
            </azimuth>
            <plunge>
              <value>82.0</value>
            </plunge>
            <length>
              <value>-1.7e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>195.0</value>
            </azimuth>
            <plunge>
              <value>8.0</value>
            </plunge>
            <length>
              <value>0.0</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C053076A/momenttensor">
          <derivedOriginID>smi:local/ndk/C053076A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>10</stationCount>
            <componentCount>24</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>14</stationCount>
            <componentCount>23</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>1.7e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>-1.66e+18</value>
              <uncertainty>2e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>8e+16</value>
              <uncertainty>2e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>1.59e+18</value>
              <uncertainty>2e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>-2.4e+17</value>
              <uncertainty>9e+16</uncertainty>
            </Mrt>
            <Mrp>
              <value>-3e+16</value>
              <uncertainty>1e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>4.3e+17</value>
              <uncertainty>2e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>5.4</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C053076A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C053076A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C053176A/event">
      <preferredOriginID>smi:local/ndk/C053176A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C053176A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C053176A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>MYANMAR-CHINA BORDER REGION</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C053176A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C053176A/origin#reforigin">
        <time>
          <value>1976-05-31T05:08:28.500000Z</value>
        </time>
        <latitude>
          <value>24.34</value>
        </latitude>
        <longitude>
          <value>98.64</value>
        </longitude>
        <depth>
          <value>14000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C053176A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C053176A/origin#cmtorigin">
        <time>
          <value>1976-05-31T05:08:35.400000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>24.26</value>
          <uncertainty>0.02</uncertainty>
        </latitude>
        <longitude>
          <value>98.6</value>
          <uncertainty>0.02</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C053176A/magnitude#moment_mag">
        <mag>
          <value>6.07</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C053176A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C053176A/magnitude#mb">
        <mag>
          <value>5.5</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C053176A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C053176A/magnitude#MS">
        <mag>
          <value>6.2</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C053176A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C053176A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>342.0</value>
            </strike>
            <dip>
              <value>72.0</value>
            </dip>
            <rake>
              <value>-169.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>249.0</value>
            </strike>
            <dip>
              <value>80.0</value>
            </dip>
            <rake>
              <value>-18.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>297.0</value>
            </azimuth>
            <plunge>
              <value>5.0</value>
            </plunge>
            <length>
              <value>1.64e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>205.0</value>
            </azimuth>
            <plunge>
              <value>20.0</value>
            </plunge>
            <length>
              <value>-1.62e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>40.0</value>
            </azimuth>
            <plunge>
              <value>69.0</value>
            </plunge>
            <length>
              <value>-2e+16</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C053176A/momenttensor">
          <derivedOriginID>smi:local/ndk/C053176A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>13</stationCount>
            <componentCount>32</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>14</stationCount>
            <componentCount>30</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>1.63e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>-1.9e+17</value>
              <uncertainty>2e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>-8.5e+17</value>
              <uncertainty>2e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>1.05e+18</value>
              <uncertainty>2e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>5.3e+17</value>
              <uncertainty>9e+16</uncertainty>
            </Mrt>
            <Mrp>
              <value>-9e+16</value>
              <uncertainty>1e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>1.2e+18</value>
              <uncertainty>2e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>5.4</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C053176A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C053176A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C060376A/event">
      <preferredOriginID>smi:local/ndk/C060376A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C060376A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C060376A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>NEW IRELAND REGION, P.N.G.</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C060376A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C060376A/origin#reforigin">
        <time>
          <value>1976-06-03T16:44:38.800000Z</value>
        </time>
        <latitude>
          <value>-5.2</value>
        </latitude>
        <longitude>
          <value>153.44</value>
        </longitude>
        <depth>
          <value>88000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C060376A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C060376A/origin#cmtorigin">
        <time>
          <value>1976-06-03T16:44:53.100000Z</value>
          <uncertainty>0.1</uncertainty>
        </time>
        <latitude>
          <value>-4.75</value>
          <uncertainty>0.01</uncertainty>
        </latitude>
        <longitude>
          <value>153.47</value>
          <uncertainty>0.01</uncertainty>
        </longitude>
        <depth>
          <value>85900.0</value>
          <uncertainty>600.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C060376A/magnitude#moment_mag">
        <mag>
          <value>7.12</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C060376A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C060376A/magnitude#mb">
        <mag>
          <value>6.2</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C060376A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C060376A/magnitude#MS">
        <mag>
          <value>0.0</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C060376A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C060376A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>143.0</value>
            </strike>
            <dip>
              <value>31.0</value>
            </dip>
            <rake>
              <value>83.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>331.0</value>
            </strike>
            <dip>
              <value>59.0</value>
            </dip>
            <rake>
              <value>94.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>252.0</value>
            </azimuth>
            <plunge>
              <value>75.0</value>
            </plunge>
            <length>
              <value>5.88e+19</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>58.0</value>
            </azimuth>
            <plunge>
              <value>14.0</value>
            </plunge>
            <length>
              <value>-6.27e+19</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>149.0</value>
            </azimuth>
            <plunge>
              <value>3.0</value>
            </plunge>
            <length>
              <value>3.9e+18</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C060376A/momenttensor">
          <derivedOriginID>smi:local/ndk/C060376A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>14</stationCount>
            <componentCount>35</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>17</stationCount>
            <componentCount>43</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>6.08e+19</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>5.11e+19</value>
              <uncertainty>6e+17</uncertainty>
            </Mrr>
            <Mtt>
              <value>-1.33e+19</value>
              <uncertainty>5e+17</uncertainty>
            </Mtt>
            <Mpp>
              <value>-3.78e+19</value>
              <uncertainty>5e+17</uncertainty>
            </Mpp>
            <Mrt>
              <value>-1.27e+19</value>
              <uncertainty>5e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>2.65e+19</value>
              <uncertainty>5e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>2.71e+19</value>
              <uncertainty>4e+17</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>17.4</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C060376A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C060376A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C060576A/event">
      <preferredOriginID>smi:local/ndk/C060576A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C060576A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C060576A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>SOLOMON ISLANDS</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C060576A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C060576A/origin#reforigin">
        <time>
          <value>1976-06-05T08:20:07.200000Z</value>
        </time>
        <latitude>
          <value>-10.09</value>
        </latitude>
        <longitude>
          <value>161.01</value>
        </longitude>
        <depth>
          <value>61000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C060576A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C060576A/origin#cmtorigin">
        <time>
          <value>1976-06-05T08:20:10.900000Z</value>
          <uncertainty>0.1</uncertainty>
        </time>
        <latitude>
          <value>-10.15</value>
          <uncertainty>0.01</uncertainty>
        </latitude>
        <longitude>
          <value>160.93</value>
          <uncertainty>0.01</uncertainty>
        </longitude>
        <depth>
          <value>47400.0</value>
          <uncertainty>600.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C060576A/magnitude#moment_mag">
        <mag>
          <value>6.26</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C060576A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C060576A/magnitude#mb">
        <mag>
          <value>6.2</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C060576A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C060576A/magnitude#MS">
        <mag>
          <value>0.0</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C060576A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C060576A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>148.0</value>
            </strike>
            <dip>
              <value>44.0</value>
            </dip>
            <rake>
              <value>113.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>298.0</value>
            </strike>
            <dip>
              <value>50.0</value>
            </dip>
            <rake>
              <value>69.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>143.0</value>
            </azimuth>
            <plunge>
              <value>74.0</value>
            </plunge>
            <length>
              <value>3.17e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>43.0</value>
            </azimuth>
            <plunge>
              <value>3.0</value>
            </plunge>
            <length>
              <value>-3.01e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>312.0</value>
            </azimuth>
            <plunge>
              <value>16.0</value>
            </plunge>
            <length>
              <value>-1.6e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C060576A/momenttensor">
          <derivedOriginID>smi:local/ndk/C060576A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>13</stationCount>
            <componentCount>33</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>13</stationCount>
            <componentCount>27</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>3.09e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>2.91e+18</value>
              <uncertainty>3e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>-1.54e+18</value>
              <uncertainty>3e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>-1.38e+18</value>
              <uncertainty>3e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>-8.1e+17</value>
              <uncertainty>6e+16</uncertainty>
            </Mrt>
            <Mrp>
              <value>-4.3e+17</value>
              <uncertainty>5e+16</uncertainty>
            </Mrp>
            <Mtp>
              <value>1.54e+18</value>
              <uncertainty>3e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>6.6</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C060576A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C060576A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C060776A/event">
      <preferredOriginID>smi:local/ndk/C060776A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C060776A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C060776A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>PHILIPPINE ISLANDS REGION</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C060776A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C060776A/origin#reforigin">
        <time>
          <value>1976-06-07T07:36:55.400000Z</value>
        </time>
        <latitude>
          <value>14.09</value>
        </latitude>
        <longitude>
          <value>124.83</value>
        </longitude>
        <depth>
          <value>33000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C060776A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C060776A/origin#cmtorigin">
        <time>
          <value>1976-06-07T07:37:00.300000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>14.23</value>
          <uncertainty>0.01</uncertainty>
        </latitude>
        <longitude>
          <value>125.07</value>
          <uncertainty>0.01</uncertainty>
        </longitude>
        <depth>
          <value>24400.0</value>
          <uncertainty>1300.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C060776A/magnitude#moment_mag">
        <mag>
          <value>6.55</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C060776A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C060776A/magnitude#mb">
        <mag>
          <value>6.1</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C060776A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C060776A/magnitude#MS">
        <mag>
          <value>6.4</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C060776A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C060776A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>249.0</value>
            </strike>
            <dip>
              <value>67.0</value>
            </dip>
            <rake>
              <value>180.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>339.0</value>
            </strike>
            <dip>
              <value>90.0</value>
            </dip>
            <rake>
              <value>23.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>206.0</value>
            </azimuth>
            <plunge>
              <value>16.0</value>
            </plunge>
            <length>
              <value>8.96e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>111.0</value>
            </azimuth>
            <plunge>
              <value>16.0</value>
            </plunge>
            <length>
              <value>-7.74e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>339.0</value>
            </azimuth>
            <plunge>
              <value>67.0</value>
            </plunge>
            <length>
              <value>-1.21e+18</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C060776A/momenttensor">
          <derivedOriginID>smi:local/ndk/C060776A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>10</stationCount>
            <componentCount>26</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>14</stationCount>
            <componentCount>34</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>8.35e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>-9.3e+17</value>
              <uncertainty>9e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>5.57e+18</value>
              <uncertainty>9e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>-4.63e+18</value>
              <uncertainty>9e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>-1.81e+18</value>
              <uncertainty>2.5e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>2.82e+18</value>
              <uncertainty>3e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>-5.74e+18</value>
              <uncertainty>8e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>9.6</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C060776A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C060776A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C060776B/event">
      <preferredOriginID>smi:local/ndk/C060776B/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C060776B/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C060776B/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>GUERRERO, MEXICO</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C060776B</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C060776B/origin#reforigin">
        <time>
          <value>1976-06-07T14:26:39.100000Z</value>
        </time>
        <latitude>
          <value>17.4</value>
        </latitude>
        <longitude>
          <value>-100.64</value>
        </longitude>
        <depth>
          <value>45000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C060776B/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C060776B/origin#cmtorigin">
        <time>
          <value>1976-06-07T14:26:43.200000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>17.22</value>
          <uncertainty>0.02</uncertainty>
        </latitude>
        <longitude>
          <value>-100.91</value>
          <uncertainty>0.02</uncertainty>
        </longitude>
        <depth>
          <value>29000.0</value>
          <uncertainty>900.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C060776B/magnitude#moment_mag">
        <mag>
          <value>6.42</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C060776B/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C060776B/magnitude#mb">
        <mag>
          <value>6.1</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C060776B/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C060776B/magnitude#MS">
        <mag>
          <value>6.4</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C060776B/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C060776B/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>289.0</value>
            </strike>
            <dip>
              <value>18.0</value>
            </dip>
            <rake>
              <value>83.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>116.0</value>
            </strike>
            <dip>
              <value>72.0</value>
            </dip>
            <rake>
              <value>92.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>29.0</value>
            </azimuth>
            <plunge>
              <value>63.0</value>
            </plunge>
            <length>
              <value>5.41e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>204.0</value>
            </azimuth>
            <plunge>
              <value>27.0</value>
            </plunge>
            <length>
              <value>-5.4e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>295.0</value>
            </azimuth>
            <plunge>
              <value>2.0</value>
            </plunge>
            <length>
              <value>-1e+16</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C060776B/momenttensor">
          <derivedOriginID>smi:local/ndk/C060776B/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>13</stationCount>
            <componentCount>37</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>16</stationCount>
            <componentCount>34</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>5.4e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>3.2e+18</value>
              <uncertainty>5e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>-2.73e+18</value>
              <uncertainty>4e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>-4.7e+17</value>
              <uncertainty>4e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>3.88e+18</value>
              <uncertainty>1.9e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>-1.97e+18</value>
              <uncertainty>1.4e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>1.13e+18</value>
              <uncertainty>3e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>7.8</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C060776B/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C060776B/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C061576A/event">
      <preferredOriginID>smi:local/ndk/C061576A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C061576A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C061576A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>IRIAN JAYA REGION, INDONESIA</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C061576A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C061576A/origin#reforigin">
        <time>
          <value>1976-06-15T06:09:01.800000Z</value>
        </time>
        <latitude>
          <value>0.54</value>
        </latitude>
        <longitude>
          <value>134.79</value>
        </longitude>
        <depth>
          <value>33000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C061576A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C061576A/origin#cmtorigin">
        <time>
          <value>1976-06-15T06:09:07.100000Z</value>
          <uncertainty>0.1</uncertainty>
        </time>
        <latitude>
          <value>0.54</value>
          <uncertainty>0.01</uncertainty>
        </latitude>
        <longitude>
          <value>134.84</value>
          <uncertainty>0.01</uncertainty>
        </longitude>
        <depth>
          <value>20200.0</value>
          <uncertainty>800.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C061576A/magnitude#moment_mag">
        <mag>
          <value>6.45</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C061576A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C061576A/magnitude#mb">
        <mag>
          <value>6.0</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C061576A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C061576A/magnitude#MS">
        <mag>
          <value>6.3</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C061576A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C061576A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>86.0</value>
            </strike>
            <dip>
              <value>87.0</value>
            </dip>
            <rake>
              <value>-1.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>176.0</value>
            </strike>
            <dip>
              <value>89.0</value>
            </dip>
            <rake>
              <value>-177.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>311.0</value>
            </azimuth>
            <plunge>
              <value>1.0</value>
            </plunge>
            <length>
              <value>6.65e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>41.0</value>
            </azimuth>
            <plunge>
              <value>3.0</value>
            </plunge>
            <length>
              <value>-5.19e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>200.0</value>
            </azimuth>
            <plunge>
              <value>86.0</value>
            </plunge>
            <length>
              <value>-1.46e+18</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C061576A/momenttensor">
          <derivedOriginID>smi:local/ndk/C061576A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>12</stationCount>
            <componentCount>35</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>18</stationCount>
            <componentCount>39</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>5.92e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>-1.47e+18</value>
              <uncertainty>5e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>-5e+16</value>
              <uncertainty>5e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>1.51e+18</value>
              <uncertainty>5e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>-5e+16</value>
              <uncertainty>1.7e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>2.8e+17</value>
              <uncertainty>1.6e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>5.86e+18</value>
              <uncertainty>6e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>8.2</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C061576A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C061576A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/B061776A/event">
      <preferredOriginID>smi:local/ndk/B061776A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/B061776A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/B061776A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>NORTHERN ITALY</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>B061776A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/B061776A/origin#reforigin">
        <time>
          <value>1976-06-17T14:28:49.200000Z</value>
        </time>
        <latitude>
          <value>46.16</value>
        </latitude>
        <longitude>
          <value>12.86</value>
        </longitude>
        <depth>
          <value>24000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/B061776A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/B061776A/origin#cmtorigin">
        <time>
          <value>1976-06-17T14:28:58.300000Z</value>
          <uncertainty>3.8</uncertainty>
        </time>
        <latitude>
          <value>46.05</value>
          <uncertainty>0.31</uncertainty>
        </latitude>
        <longitude>
          <value>12.5</value>
          <uncertainty>0.35</uncertainty>
        </longitude>
        <depth>
          <value>45500.0</value>
          <uncertainty>14900.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/B061776A/magnitude#moment_mag">
        <mag>
          <value>5.17</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/B061776A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/B061776A/magnitude#mb">
        <mag>
          <value>6.1</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/B061776A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/B061776A/magnitude#MS">
        <mag>
          <value>0.0</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/B061776A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/B061776A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>58.0</value>
            </strike>
            <dip>
              <value>55.0</value>
            </dip>
            <rake>
              <value>37.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>305.0</value>
            </strike>
            <dip>
              <value>60.0</value>
            </dip>
            <rake>
              <value>139.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>269.0</value>
            </azimuth>
            <plunge>
              <value>49.0</value>
            </plunge>
            <length>
              <value>5.45e+16</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>2.0</value>
            </azimuth>
            <plunge>
              <value>3.0</value>
            </plunge>
            <length>
              <value>-8.72e+16</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>95.0</value>
            </azimuth>
            <plunge>
              <value>41.0</value>
            </plunge>
            <length>
              <value>3.27e+16</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/B061776A/momenttensor">
          <derivedOriginID>smi:local/ndk/B061776A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>12</stationCount>
            <componentCount>20</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>7.09e+16</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>4.49e+16</value>
              <uncertainty>9.8e+15</uncertainty>
            </Mrr>
            <Mtt>
              <value>-8.67e+16</value>
              <uncertainty>1.68e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>4.19e+16</value>
              <uncertainty>1.07e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>-6.6e+15</value>
              <uncertainty>1.45e+16</uncertainty>
            </Mrt>
            <Mrp>
              <value>1.11e+16</value>
              <uncertainty>1.25e+16</uncertainty>
            </Mrp>
            <Mtp>
              <value>4.4e+15</value>
              <uncertainty>1.25e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>6.6</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/B061776A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/B061776A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C061976A/event">
      <preferredOriginID>smi:local/ndk/C061976A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C061976A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C061976A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>MAURITIUS - REUNION REGION</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C061976A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C061976A/origin#reforigin">
        <time>
          <value>1976-06-19T15:00:46.700000Z</value>
        </time>
        <latitude>
          <value>-18.02</value>
        </latitude>
        <longitude>
          <value>65.41</value>
        </longitude>
        <depth>
          <value>33000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C061976A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C061976A/origin#cmtorigin">
        <time>
          <value>1976-06-19T15:00:55.400000Z</value>
          <uncertainty>0.1</uncertainty>
        </time>
        <latitude>
          <value>-17.58</value>
          <uncertainty>0.01</uncertainty>
        </latitude>
        <longitude>
          <value>65.59</value>
          <uncertainty>0.01</uncertainty>
        </longitude>
        <depth>
          <value>16200.0</value>
          <uncertainty>1500.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C061976A/magnitude#moment_mag">
        <mag>
          <value>6.37</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C061976A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C061976A/magnitude#mb">
        <mag>
          <value>5.6</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C061976A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C061976A/magnitude#MS">
        <mag>
          <value>6.1</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C061976A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C061976A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>59.0</value>
            </strike>
            <dip>
              <value>86.0</value>
            </dip>
            <rake>
              <value>2.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>329.0</value>
            </strike>
            <dip>
              <value>88.0</value>
            </dip>
            <rake>
              <value>176.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>284.0</value>
            </azimuth>
            <plunge>
              <value>4.0</value>
            </plunge>
            <length>
              <value>4.69e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>14.0</value>
            </azimuth>
            <plunge>
              <value>1.0</value>
            </plunge>
            <length>
              <value>-4.48e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>117.0</value>
            </azimuth>
            <plunge>
              <value>85.0</value>
            </plunge>
            <length>
              <value>-2.1e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C061976A/momenttensor">
          <derivedOriginID>smi:local/ndk/C061976A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>14</stationCount>
            <componentCount>36</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>15</stationCount>
            <componentCount>37</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>4.59e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>-1.8e+17</value>
              <uncertainty>4e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>-3.92e+18</value>
              <uncertainty>4e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>4.1e+18</value>
              <uncertainty>4e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>2e+16</value>
              <uncertainty>1.2e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>3.9e+17</value>
              <uncertainty>1.4e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>2.19e+18</value>
              <uncertainty>4e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>7.6</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C061976A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C061976A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C062076A/event">
      <preferredOriginID>smi:local/ndk/C062076A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C062076A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C062076A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>NORTHERN SUMATRA, INDONESIA</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C062076A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C062076A/origin#reforigin">
        <time>
          <value>1976-06-20T20:53:13.400000Z</value>
        </time>
        <latitude>
          <value>3.4</value>
        </latitude>
        <longitude>
          <value>96.32</value>
        </longitude>
        <depth>
          <value>33000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C062076A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C062076A/origin#cmtorigin">
        <time>
          <value>1976-06-20T20:53:23.500000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>3.18</value>
          <uncertainty>0.02</uncertainty>
        </latitude>
        <longitude>
          <value>96.24</value>
          <uncertainty>0.02</uncertainty>
        </longitude>
        <depth>
          <value>19100.0</value>
          <uncertainty>800.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C062076A/magnitude#moment_mag">
        <mag>
          <value>6.97</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C062076A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C062076A/magnitude#mb">
        <mag>
          <value>6.3</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C062076A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C062076A/magnitude#MS">
        <mag>
          <value>7.0</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C062076A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C062076A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>338.0</value>
            </strike>
            <dip>
              <value>28.0</value>
            </dip>
            <rake>
              <value>99.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>147.0</value>
            </strike>
            <dip>
              <value>62.0</value>
            </dip>
            <rake>
              <value>85.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>46.0</value>
            </azimuth>
            <plunge>
              <value>72.0</value>
            </plunge>
            <length>
              <value>3.07e+19</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>241.0</value>
            </azimuth>
            <plunge>
              <value>17.0</value>
            </plunge>
            <length>
              <value>-4.03e+19</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>150.0</value>
            </azimuth>
            <plunge>
              <value>4.0</value>
            </plunge>
            <length>
              <value>9.6e+18</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C062076A/momenttensor">
          <derivedOriginID>smi:local/ndk/C062076A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>13</stationCount>
            <componentCount>33</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>18</stationCount>
            <componentCount>41</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>3.55e+19</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>2.43e+19</value>
              <uncertainty>4e+17</uncertainty>
            </Mrr>
            <Mtt>
              <value>-2e+17</value>
              <uncertainty>3e+17</uncertainty>
            </Mtt>
            <Mpp>
              <value>-2.41e+19</value>
              <uncertainty>3e+17</uncertainty>
            </Mpp>
            <Mrt>
              <value>1.12e+19</value>
              <uncertainty>1.3e+18</uncertainty>
            </Mrt>
            <Mrp>
              <value>-1.68e+19</value>
              <uncertainty>1.5e+18</uncertainty>
            </Mrp>
            <Mtp>
              <value>1.84e+19</value>
              <uncertainty>3e+17</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>15.0</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C062076A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C062076A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C062576A/event">
      <preferredOriginID>smi:local/ndk/C062576A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C062576A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C062576A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>IRIAN JAYA, INDONESIA</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C062576A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C062576A/origin#reforigin">
        <time>
          <value>1976-06-25T19:18:56.900000Z</value>
        </time>
        <latitude>
          <value>-4.6</value>
        </latitude>
        <longitude>
          <value>140.09</value>
        </longitude>
        <depth>
          <value>33000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C062576A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C062576A/origin#cmtorigin">
        <time>
          <value>1976-06-25T19:19:12.800000Z</value>
          <uncertainty>0.1</uncertainty>
        </time>
        <latitude>
          <value>-4.66</value>
          <uncertainty>0.01</uncertainty>
        </latitude>
        <longitude>
          <value>140.29</value>
          <uncertainty>0.01</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C062576A/magnitude#moment_mag">
        <mag>
          <value>7.14</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C062576A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C062576A/magnitude#mb">
        <mag>
          <value>6.1</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C062576A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C062576A/magnitude#MS">
        <mag>
          <value>7.1</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C062576A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C062576A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>9.0</value>
            </strike>
            <dip>
              <value>59.0</value>
            </dip>
            <rake>
              <value>153.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>113.0</value>
            </strike>
            <dip>
              <value>67.0</value>
            </dip>
            <rake>
              <value>34.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>334.0</value>
            </azimuth>
            <plunge>
              <value>40.0</value>
            </plunge>
            <length>
              <value>6.81e+19</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>240.0</value>
            </azimuth>
            <plunge>
              <value>5.0</value>
            </plunge>
            <length>
              <value>-6.23e+19</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>144.0</value>
            </azimuth>
            <plunge>
              <value>50.0</value>
            </plunge>
            <length>
              <value>-5.8e+18</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C062576A/momenttensor">
          <derivedOriginID>smi:local/ndk/C062576A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>11</stationCount>
            <componentCount>25</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>16</stationCount>
            <componentCount>37</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>6.52e+19</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>2.4e+19</value>
              <uncertainty>4e+17</uncertainty>
            </Mrr>
            <Mtt>
              <value>1.48e+19</value>
              <uncertainty>3e+17</uncertainty>
            </Mtt>
            <Mpp>
              <value>-3.88e+19</value>
              <uncertainty>4e+17</uncertainty>
            </Mpp>
            <Mrt>
              <value>3.49e+19</value>
              <uncertainty>1.9e+18</uncertainty>
            </Mrt>
            <Mrp>
              <value>1.22e+19</value>
              <uncertainty>1.8e+18</uncertainty>
            </Mrp>
            <Mtp>
              <value>4.19e+19</value>
              <uncertainty>3e+17</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>18.2</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C062576A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C062576A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C062676A/event">
      <preferredOriginID>smi:local/ndk/C062676A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C062676A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C062676A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>TALAUD ISLANDS, INDONESIA</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C062676A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C062676A/origin#reforigin">
        <time>
          <value>1976-06-26T10:30:59.400000Z</value>
        </time>
        <latitude>
          <value>3.66</value>
        </latitude>
        <longitude>
          <value>126.75</value>
        </longitude>
        <depth>
          <value>33000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C062676A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C062676A/origin#cmtorigin">
        <time>
          <value>1976-06-26T10:31:05.600000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>3.77</value>
          <uncertainty>0.02</uncertainty>
        </latitude>
        <longitude>
          <value>127.06</value>
          <uncertainty>0.01</uncertainty>
        </longitude>
        <depth>
          <value>18000.0</value>
          <uncertainty>800.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C062676A/magnitude#moment_mag">
        <mag>
          <value>6.48</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C062676A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C062676A/magnitude#mb">
        <mag>
          <value>5.8</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C062676A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C062676A/magnitude#MS">
        <mag>
          <value>6.5</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C062676A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C062676A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>169.0</value>
            </strike>
            <dip>
              <value>26.0</value>
            </dip>
            <rake>
              <value>69.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>12.0</value>
            </strike>
            <dip>
              <value>66.0</value>
            </dip>
            <rake>
              <value>100.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>301.0</value>
            </azimuth>
            <plunge>
              <value>68.0</value>
            </plunge>
            <length>
              <value>6.52e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>95.0</value>
            </azimuth>
            <plunge>
              <value>20.0</value>
            </plunge>
            <length>
              <value>-6.65e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>188.0</value>
            </azimuth>
            <plunge>
              <value>9.0</value>
            </plunge>
            <length>
              <value>1.3e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C062676A/momenttensor">
          <derivedOriginID>smi:local/ndk/C062676A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>13</stationCount>
            <componentCount>35</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>17</stationCount>
            <componentCount>40</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>6.59e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>4.8e+18</value>
              <uncertainty>8e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>3.4e+17</value>
              <uncertainty>6e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>-5.14e+18</value>
              <uncertainty>7e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>1.35e+18</value>
              <uncertainty>2.4e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>4.1e+18</value>
              <uncertainty>3.3e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>-9e+16</value>
              <uncertainty>5e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>8.6</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C062676A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C062676A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C062976A/event">
      <preferredOriginID>smi:local/ndk/C062976A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C062976A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C062976A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>SOUTH OF KERMADEC ISLANDS</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C062976A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C062976A/origin#reforigin">
        <time>
          <value>1976-06-29T18:30:09.100000Z</value>
        </time>
        <latitude>
          <value>-33.82</value>
        </latitude>
        <longitude>
          <value>-177.83</value>
        </longitude>
        <depth>
          <value>48000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C062976A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C062976A/origin#cmtorigin">
        <time>
          <value>1976-06-29T18:30:12.900000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>-33.63</value>
          <uncertainty>0.02</uncertainty>
        </latitude>
        <longitude>
          <value>-177.63</value>
          <uncertainty>0.02</uncertainty>
        </longitude>
        <depth>
          <value>55200.0</value>
          <uncertainty>800.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C062976A/magnitude#moment_mag">
        <mag>
          <value>6.18</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C062976A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C062976A/magnitude#mb">
        <mag>
          <value>6.1</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C062976A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C062976A/magnitude#MS">
        <mag>
          <value>5.9</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C062976A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C062976A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>24.0</value>
            </strike>
            <dip>
              <value>37.0</value>
            </dip>
            <rake>
              <value>78.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>220.0</value>
            </strike>
            <dip>
              <value>54.0</value>
            </dip>
            <rake>
              <value>99.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>166.0</value>
            </azimuth>
            <plunge>
              <value>79.0</value>
            </plunge>
            <length>
              <value>2.18e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>303.0</value>
            </azimuth>
            <plunge>
              <value>8.0</value>
            </plunge>
            <length>
              <value>-2.55e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>34.0</value>
            </azimuth>
            <plunge>
              <value>7.0</value>
            </plunge>
            <length>
              <value>3.8e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C062976A/momenttensor">
          <derivedOriginID>smi:local/ndk/C062976A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>14</stationCount>
            <componentCount>33</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>16</stationCount>
            <componentCount>30</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>2.36e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>2.05e+18</value>
              <uncertainty>3e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>-4.1e+17</value>
              <uncertainty>3e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>-1.64e+18</value>
              <uncertainty>3e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>-5.5e+17</value>
              <uncertainty>4e+16</uncertainty>
            </Mrt>
            <Mrp>
              <value>-4.3e+17</value>
              <uncertainty>4e+16</uncertainty>
            </Mrp>
            <Mtp>
              <value>-1.3e+18</value>
              <uncertainty>3e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>6.0</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C062976A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C062976A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C071176A/event">
      <preferredOriginID>smi:local/ndk/C071176A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C071176A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C071176A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>PANAMA</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C071176A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C071176A/origin#reforigin">
        <time>
          <value>1976-07-11T16:54:31.800000Z</value>
        </time>
        <latitude>
          <value>7.34</value>
        </latitude>
        <longitude>
          <value>-78.47</value>
        </longitude>
        <depth>
          <value>22000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C071176A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C071176A/origin#cmtorigin">
        <time>
          <value>1976-07-11T16:54:39.500000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>7.19</value>
          <uncertainty>0.02</uncertainty>
        </latitude>
        <longitude>
          <value>-78.29</value>
          <uncertainty>0.02</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C071176A/magnitude#moment_mag">
        <mag>
          <value>6.75</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C071176A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C071176A/magnitude#mb">
        <mag>
          <value>6.3</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C071176A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C071176A/magnitude#MS">
        <mag>
          <value>6.7</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C071176A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C071176A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>74.0</value>
            </strike>
            <dip>
              <value>63.0</value>
            </dip>
            <rake>
              <value>171.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>167.0</value>
            </strike>
            <dip>
              <value>82.0</value>
            </dip>
            <rake>
              <value>27.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>34.0</value>
            </azimuth>
            <plunge>
              <value>24.0</value>
            </plunge>
            <length>
              <value>1.49e+19</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>298.0</value>
            </azimuth>
            <plunge>
              <value>13.0</value>
            </plunge>
            <length>
              <value>-1.85e+19</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>182.0</value>
            </azimuth>
            <plunge>
              <value>62.0</value>
            </plunge>
            <length>
              <value>3.6e+18</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C071176A/momenttensor">
          <derivedOriginID>smi:local/ndk/C071176A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>12</stationCount>
            <componentCount>35</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>15</stationCount>
            <componentCount>29</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>1.67e+19</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>4.4e+18</value>
              <uncertainty>2e+17</uncertainty>
            </Mrr>
            <Mtt>
              <value>5.5e+18</value>
              <uncertainty>2e+17</uncertainty>
            </Mtt>
            <Mpp>
              <value>-9.9e+18</value>
              <uncertainty>2e+17</uncertainty>
            </Mpp>
            <Mrt>
              <value>1.3e+18</value>
              <uncertainty>5e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>-6.6e+18</value>
              <uncertainty>5e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>-1.3e+19</value>
              <uncertainty>2e+17</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>11.6</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C071176A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C071176A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C071176B/event">
      <preferredOriginID>smi:local/ndk/C071176B/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C071176B/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C071176B/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>PANAMA</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C071176B</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C071176B/origin#reforigin">
        <time>
          <value>1976-07-11T20:41:47.500000Z</value>
        </time>
        <latitude>
          <value>7.41</value>
        </latitude>
        <longitude>
          <value>-78.13</value>
        </longitude>
        <depth>
          <value>3000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C071176B/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C071176B/origin#cmtorigin">
        <time>
          <value>1976-07-11T20:42:04.500000Z</value>
          <uncertainty>0.1</uncertainty>
        </time>
        <latitude>
          <value>7.32</value>
          <uncertainty>0.01</uncertainty>
        </latitude>
        <longitude>
          <value>-78.11</value>
          <uncertainty>0.01</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C071176B/magnitude#moment_mag">
        <mag>
          <value>7.26</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C071176B/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C071176B/magnitude#mb">
        <mag>
          <value>6.2</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C071176B/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C071176B/magnitude#MS">
        <mag>
          <value>7.0</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C071176B/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C071176B/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>78.0</value>
            </strike>
            <dip>
              <value>67.0</value>
            </dip>
            <rake>
              <value>161.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>176.0</value>
            </strike>
            <dip>
              <value>72.0</value>
            </dip>
            <rake>
              <value>24.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>38.0</value>
            </azimuth>
            <plunge>
              <value>30.0</value>
            </plunge>
            <length>
              <value>9.18e+19</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>306.0</value>
            </azimuth>
            <plunge>
              <value>3.0</value>
            </plunge>
            <length>
              <value>-1.013e+20</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>210.0</value>
            </azimuth>
            <plunge>
              <value>60.0</value>
            </plunge>
            <length>
              <value>9.5e+18</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C071176B/momenttensor">
          <derivedOriginID>smi:local/ndk/C071176B/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>11</stationCount>
            <componentCount>23</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>16</stationCount>
            <componentCount>41</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>9.66e+19</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>2.91e+19</value>
              <uncertainty>7e+17</uncertainty>
            </Mrr>
            <Mtt>
              <value>8.9e+18</value>
              <uncertainty>6e+17</uncertainty>
            </Mtt>
            <Mpp>
              <value>-3.8e+19</value>
              <uncertainty>8e+17</uncertainty>
            </Mpp>
            <Mrt>
              <value>2.38e+19</value>
              <uncertainty>3.1e+18</uncertainty>
            </Mrt>
            <Mrp>
              <value>-2.72e+19</value>
              <uncertainty>3.6e+18</uncertainty>
            </Mrp>
            <Mtp>
              <value>-8.31e+19</value>
              <uncertainty>6e+17</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>21.4</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C071176B/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C071176B/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C071476A/event">
      <preferredOriginID>smi:local/ndk/C071476A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C071476A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C071476A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>BALI REGION, INDONESIA</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C071476A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C071476A/origin#reforigin">
        <time>
          <value>1976-07-14T07:13:24.000000Z</value>
        </time>
        <latitude>
          <value>-8.17</value>
        </latitude>
        <longitude>
          <value>114.89</value>
        </longitude>
        <depth>
          <value>40000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C071476A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C071476A/origin#cmtorigin">
        <time>
          <value>1976-07-14T07:13:30.300000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>-8.14</value>
          <uncertainty>0.01</uncertainty>
        </latitude>
        <longitude>
          <value>114.89</value>
          <uncertainty>0.02</uncertainty>
        </longitude>
        <depth>
          <value>28400.0</value>
          <uncertainty>900.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C071476A/magnitude#moment_mag">
        <mag>
          <value>6.47</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C071476A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C071476A/magnitude#mb">
        <mag>
          <value>6.2</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C071476A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C071476A/magnitude#MS">
        <mag>
          <value>6.5</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C071476A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C071476A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>96.0</value>
            </strike>
            <dip>
              <value>29.0</value>
            </dip>
            <rake>
              <value>87.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>280.0</value>
            </strike>
            <dip>
              <value>61.0</value>
            </dip>
            <rake>
              <value>92.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>194.0</value>
            </azimuth>
            <plunge>
              <value>74.0</value>
            </plunge>
            <length>
              <value>6.45e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>8.0</value>
            </azimuth>
            <plunge>
              <value>16.0</value>
            </plunge>
            <length>
              <value>-6.49e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>99.0</value>
            </azimuth>
            <plunge>
              <value>2.0</value>
            </plunge>
            <length>
              <value>4e+16</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C071476A/momenttensor">
          <derivedOriginID>smi:local/ndk/C071476A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>11</stationCount>
            <componentCount>30</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>15</stationCount>
            <componentCount>31</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>6.47e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>5.43e+18</value>
              <uncertainty>9e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>-5.38e+18</value>
              <uncertainty>7e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>-6e+16</value>
              <uncertainty>7e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>-3.4e+18</value>
              <uncertainty>2.7e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>6.8e+17</value>
              <uncertainty>2.4e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>7.6e+17</value>
              <uncertainty>5e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>8.4</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C071476A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C071476A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C071776A/event">
      <preferredOriginID>smi:local/ndk/C071776A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C071776A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C071776A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>NEW BRITAIN REGION, P.N.G.</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C071776A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C071776A/origin#reforigin">
        <time>
          <value>1976-07-17T21:06:32.100000Z</value>
        </time>
        <latitude>
          <value>-4.16</value>
        </latitude>
        <longitude>
          <value>152.76</value>
        </longitude>
        <depth>
          <value>53000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C071776A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C071776A/origin#cmtorigin">
        <time>
          <value>1976-07-17T21:06:36.800000Z</value>
          <uncertainty>0.1</uncertainty>
        </time>
        <latitude>
          <value>-4.27</value>
          <uncertainty>0.02</uncertainty>
        </latitude>
        <longitude>
          <value>152.71</value>
          <uncertainty>0.01</uncertainty>
        </longitude>
        <depth>
          <value>36500.0</value>
          <uncertainty>700.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C071776A/magnitude#moment_mag">
        <mag>
          <value>6.56</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C071776A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C071776A/magnitude#mb">
        <mag>
          <value>6.0</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C071776A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C071776A/magnitude#MS">
        <mag>
          <value>6.6</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C071776A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C071776A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>343.0</value>
            </strike>
            <dip>
              <value>52.0</value>
            </dip>
            <rake>
              <value>146.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>96.0</value>
            </strike>
            <dip>
              <value>63.0</value>
            </dip>
            <rake>
              <value>43.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>315.0</value>
            </azimuth>
            <plunge>
              <value>48.0</value>
            </plunge>
            <length>
              <value>9.05e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>218.0</value>
            </azimuth>
            <plunge>
              <value>7.0</value>
            </plunge>
            <length>
              <value>-8.58e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>122.0</value>
            </azimuth>
            <plunge>
              <value>41.0</value>
            </plunge>
            <length>
              <value>-4.7e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C071776A/momenttensor">
          <derivedOriginID>smi:local/ndk/C071776A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>11</stationCount>
            <componentCount>28</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>15</stationCount>
            <componentCount>30</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>8.81e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>4.76e+18</value>
              <uncertainty>8e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>-3.41e+18</value>
              <uncertainty>8e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>-1.35e+18</value>
              <uncertainty>6e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>4.07e+18</value>
              <uncertainty>2e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>2.78e+18</value>
              <uncertainty>1.8e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>5.96e+18</value>
              <uncertainty>7e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>9.4</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C071776A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C071776A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C072176A/event">
      <preferredOriginID>smi:local/ndk/C072176A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C072176A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C072176A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>MYANMAR-CHINA BORDER REGION</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C072176A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C072176A/origin#reforigin">
        <time>
          <value>1976-07-21T15:10:45.600000Z</value>
        </time>
        <latitude>
          <value>24.78</value>
        </latitude>
        <longitude>
          <value>98.7</value>
        </longitude>
        <depth>
          <value>9000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C072176A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C072176A/origin#cmtorigin">
        <time>
          <value>1976-07-21T15:10:52.200000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>24.74</value>
          <uncertainty>0.02</uncertainty>
        </latitude>
        <longitude>
          <value>98.57</value>
          <uncertainty>0.02</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C072176A/magnitude#moment_mag">
        <mag>
          <value>6.13</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C072176A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C072176A/magnitude#mb">
        <mag>
          <value>5.8</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C072176A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C072176A/magnitude#MS">
        <mag>
          <value>6.3</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C072176A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C072176A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>338.0</value>
            </strike>
            <dip>
              <value>88.0</value>
            </dip>
            <rake>
              <value>-178.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>248.0</value>
            </strike>
            <dip>
              <value>88.0</value>
            </dip>
            <rake>
              <value>-2.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>293.0</value>
            </azimuth>
            <plunge>
              <value>1.0</value>
            </plunge>
            <length>
              <value>1.98e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>203.0</value>
            </azimuth>
            <plunge>
              <value>3.0</value>
            </plunge>
            <length>
              <value>-1.98e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>33.0</value>
            </azimuth>
            <plunge>
              <value>87.0</value>
            </plunge>
            <length>
              <value>1e+16</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C072176A/momenttensor">
          <derivedOriginID>smi:local/ndk/C072176A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>10</stationCount>
            <componentCount>28</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>14</stationCount>
            <componentCount>29</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>1.98e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>0.0</value>
              <uncertainty>3e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>-1.38e+18</value>
              <uncertainty>3e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>1.38e+18</value>
              <uncertainty>3e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>1e+17</value>
              <uncertainty>1.3e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>-2e+16</value>
              <uncertainty>1.4e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>1.42e+18</value>
              <uncertainty>3e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>5.8</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C072176A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C072176A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/B072676A/event">
      <preferredOriginID>smi:local/ndk/B072676A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/B072676A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/B072676A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>SOUTHERN EAST PACIFIC RISE</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>B072676A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/B072676A/origin#reforigin">
        <time>
          <value>1976-07-26T01:41:25.400000Z</value>
        </time>
        <latitude>
          <value>-21.91</value>
        </latitude>
        <longitude>
          <value>-113.33</value>
        </longitude>
        <depth>
          <value>33000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/B072676A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/B072676A/origin#cmtorigin">
        <time>
          <value>1976-07-26T01:41:28.700000Z</value>
          <uncertainty>0.5</uncertainty>
        </time>
        <latitude>
          <value>-21.76</value>
          <uncertainty>0.07</uncertainty>
        </latitude>
        <longitude>
          <value>-113.44</value>
          <uncertainty>0.09</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/B072676A/magnitude#moment_mag">
        <mag>
          <value>5.48</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/B072676A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/B072676A/magnitude#mb">
        <mag>
          <value>5.2</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/B072676A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/B072676A/magnitude#MS">
        <mag>
          <value>6.2</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/B072676A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/B072676A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>274.0</value>
            </strike>
            <dip>
              <value>67.0</value>
            </dip>
            <rake>
              <value>6.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>182.0</value>
            </strike>
            <dip>
              <value>84.0</value>
            </dip>
            <rake>
              <value>157.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>136.0</value>
            </azimuth>
            <plunge>
              <value>20.0</value>
            </plunge>
            <length>
              <value>1.92e+17</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>230.0</value>
            </azimuth>
            <plunge>
              <value>11.0</value>
            </plunge>
            <length>
              <value>-2.22e+17</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>348.0</value>
            </azimuth>
            <plunge>
              <value>67.0</value>
            </plunge>
            <length>
              <value>3.1e+16</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/B072676A/momenttensor">
          <derivedOriginID>smi:local/ndk/B072676A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>9</stationCount>
            <componentCount>16</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>2.07e+17</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>3.9e+16</value>
              <uncertainty>1e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>4e+15</value>
              <uncertainty>7e+15</uncertainty>
            </Mtt>
            <Mpp>
              <value>-4.3e+16</value>
              <uncertainty>1.2e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>-6e+15</value>
              <uncertainty>2.2e+16</uncertainty>
            </Mrt>
            <Mrp>
              <value>-7.4e+16</value>
              <uncertainty>3e+16</uncertainty>
            </Mrp>
            <Mtp>
              <value>1.91e+17</value>
              <uncertainty>1e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>2.6</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/B072676A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/B072676A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C072676B/event">
      <preferredOriginID>smi:local/ndk/C072676B/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C072676B/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C072676B/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>BORNEO</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C072676B</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C072676B/origin#reforigin">
        <time>
          <value>1976-07-26T02:56:39.300000Z</value>
        </time>
        <latitude>
          <value>4.96</value>
        </latitude>
        <longitude>
          <value>118.31</value>
        </longitude>
        <depth>
          <value>33000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C072676B/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C072676B/origin#cmtorigin">
        <time>
          <value>1976-07-26T02:56:46.900000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>5.08</value>
          <uncertainty>0.02</uncertainty>
        </latitude>
        <longitude>
          <value>118.55</value>
          <uncertainty>0.02</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C072676B/magnitude#moment_mag">
        <mag>
          <value>6.27</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C072676B/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C072676B/magnitude#mb">
        <mag>
          <value>5.8</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C072676B/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C072676B/magnitude#MS">
        <mag>
          <value>6.2</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C072676B/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C072676B/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>59.0</value>
            </strike>
            <dip>
              <value>70.0</value>
            </dip>
            <rake>
              <value>-172.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>327.0</value>
            </strike>
            <dip>
              <value>83.0</value>
            </dip>
            <rake>
              <value>-20.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>15.0</value>
            </azimuth>
            <plunge>
              <value>9.0</value>
            </plunge>
            <length>
              <value>3.38e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>281.0</value>
            </azimuth>
            <plunge>
              <value>19.0</value>
            </plunge>
            <length>
              <value>-3.11e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>128.0</value>
            </azimuth>
            <plunge>
              <value>69.0</value>
            </plunge>
            <length>
              <value>-2.8e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C072676B/momenttensor">
          <derivedOriginID>smi:local/ndk/C072676B/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>9</stationCount>
            <componentCount>20</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>14</stationCount>
            <componentCount>27</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>3.24e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>-5e+17</value>
              <uncertainty>5e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>2.97e+18</value>
              <uncertainty>4e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>-2.47e+18</value>
              <uncertainty>5e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>3.6e+17</value>
              <uncertainty>1.8e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>-1e+18</value>
              <uncertainty>2e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>-1.36e+18</value>
              <uncertainty>5e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>6.8</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C072676B/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C072676B/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/M072776A/event">
      <preferredOriginID>smi:local/ndk/M072776A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/M072776A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/M072776A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>NORTHEASTERN CHINA</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>M072776A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/M072776A/origin#reforigin">
        <time>
          <value>1976-07-27T19:42:54.600000Z</value>
        </time>
        <latitude>
          <value>39.57</value>
        </latitude>
        <longitude>
          <value>117.98</value>
        </longitude>
        <depth>
          <value>23000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/M072776A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/M072776A/origin#cmtorigin">
        <time>
          <value>1976-07-27T19:43:11.100000Z</value>
          <uncertainty>0.3</uncertainty>
        </time>
        <latitude>
          <value>39.52</value>
          <uncertainty>0.01</uncertainty>
        </latitude>
        <longitude>
          <value>118.03</value>
          <uncertainty>0.04</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/M072776A/magnitude#moment_mag">
        <mag>
          <value>7.56</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/M072776A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/M072776A/magnitude#mb">
        <mag>
          <value>6.3</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/M072776A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/M072776A/magnitude#MS">
        <mag>
          <value>7.9</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/M072776A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/M072776A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>229.0</value>
            </strike>
            <dip>
              <value>43.0</value>
            </dip>
            <rake>
              <value>-163.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>126.0</value>
            </strike>
            <dip>
              <value>79.0</value>
            </dip>
            <rake>
              <value>-49.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>186.0</value>
            </azimuth>
            <plunge>
              <value>22.0</value>
            </plunge>
            <length>
              <value>2.52e+20</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>75.0</value>
            </azimuth>
            <plunge>
              <value>41.0</value>
            </plunge>
            <length>
              <value>-3.03e+20</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>297.0</value>
            </azimuth>
            <plunge>
              <value>40.0</value>
            </plunge>
            <length>
              <value>5.1e+19</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/M072776A/momenttensor">
          <derivedOriginID>smi:local/ndk/M072776A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>15</stationCount>
            <componentCount>35</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>2.77e+20</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>-7.4e+19</value>
              <uncertainty>3e+18</uncertainty>
            </Mrr>
            <Mtt>
              <value>2.07e+20</value>
              <uncertainty>2e+18</uncertainty>
            </Mtt>
            <Mpp>
              <value>-1.34e+20</value>
              <uncertainty>3e+18</uncertainty>
            </Mpp>
            <Mrt>
              <value>-1.16e+20</value>
              <uncertainty>2.2e+19</uncertainty>
            </Mrt>
            <Mrp>
              <value>1.77e+20</value>
              <uncertainty>2.2e+19</uncertainty>
            </Mrp>
            <Mtp>
              <value>3.2e+19</value>
              <uncertainty>2e+18</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>25.8</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/M072776A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/M072776A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C072876A/event">
      <preferredOriginID>smi:local/ndk/C072876A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C072876A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C072876A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>NORTHEASTERN CHINA</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C072876A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C072876A/origin#reforigin">
        <time>
          <value>1976-07-28T10:45:35.200000Z</value>
        </time>
        <latitude>
          <value>39.66</value>
        </latitude>
        <longitude>
          <value>118.4</value>
        </longitude>
        <depth>
          <value>26000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C072876A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C072876A/origin#cmtorigin">
        <time>
          <value>1976-07-28T10:45:45.900000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>39.75</value>
          <uncertainty>0.01</uncertainty>
        </latitude>
        <longitude>
          <value>118.78</value>
          <uncertainty>0.04</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C072876A/magnitude#moment_mag">
        <mag>
          <value>6.97</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C072876A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C072876A/magnitude#mb">
        <mag>
          <value>6.3</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C072876A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C072876A/magnitude#MS">
        <mag>
          <value>7.4</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C072876A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C072876A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>72.0</value>
            </strike>
            <dip>
              <value>44.0</value>
            </dip>
            <rake>
              <value>-110.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>279.0</value>
            </strike>
            <dip>
              <value>49.0</value>
            </dip>
            <rake>
              <value>-71.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>356.0</value>
            </azimuth>
            <plunge>
              <value>3.0</value>
            </plunge>
            <length>
              <value>4.43e+19</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>256.0</value>
            </azimuth>
            <plunge>
              <value>76.0</value>
            </plunge>
            <length>
              <value>-2.72e+19</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>87.0</value>
            </azimuth>
            <plunge>
              <value>14.0</value>
            </plunge>
            <length>
              <value>-1.72e+19</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C072876A/momenttensor">
          <derivedOriginID>smi:local/ndk/C072876A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>8</stationCount>
            <componentCount>12</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>13</stationCount>
            <componentCount>31</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>3.58e+19</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>-2.64e+19</value>
              <uncertainty>6e+17</uncertainty>
            </Mrr>
            <Mtt>
              <value>4.39e+19</value>
              <uncertainty>4e+17</uncertainty>
            </Mtt>
            <Mpp>
              <value>-1.75e+19</value>
              <uncertainty>6e+17</uncertainty>
            </Mpp>
            <Mrt>
              <value>3.3e+18</value>
              <uncertainty>2.9e+18</uncertainty>
            </Mrt>
            <Mrp>
              <value>-2.1e+18</value>
              <uncertainty>3.2e+18</uncertainty>
            </Mrp>
            <Mtp>
              <value>4.2e+18</value>
              <uncertainty>5e+17</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>15.2</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C072876A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C072876A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C072876B/event">
      <preferredOriginID>smi:local/ndk/C072876B/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C072876B/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C072876B/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>VANUATU ISLANDS</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C072876B</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C072876B/origin#reforigin">
        <time>
          <value>1976-07-28T17:15:01.700000Z</value>
        </time>
        <latitude>
          <value>-20.2</value>
        </latitude>
        <longitude>
          <value>170.0</value>
        </longitude>
        <depth>
          <value>5000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C072876B/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C072876B/origin#cmtorigin">
        <time>
          <value>1976-07-28T17:15:10.200000Z</value>
          <uncertainty>0.3</uncertainty>
        </time>
        <latitude>
          <value>-19.95</value>
          <uncertainty>0.04</uncertainty>
        </latitude>
        <longitude>
          <value>169.58</value>
          <uncertainty>0.04</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C072876B/magnitude#moment_mag">
        <mag>
          <value>6.31</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C072876B/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C072876B/magnitude#mb">
        <mag>
          <value>5.6</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C072876B/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C072876B/magnitude#MS">
        <mag>
          <value>6.0</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C072876B/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C072876B/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>196.0</value>
            </strike>
            <dip>
              <value>36.0</value>
            </dip>
            <rake>
              <value>-36.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>317.0</value>
            </strike>
            <dip>
              <value>70.0</value>
            </dip>
            <rake>
              <value>-120.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>69.0</value>
            </azimuth>
            <plunge>
              <value>20.0</value>
            </plunge>
            <length>
              <value>3.62e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>189.0</value>
            </azimuth>
            <plunge>
              <value>55.0</value>
            </plunge>
            <length>
              <value>-3.68e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>328.0</value>
            </azimuth>
            <plunge>
              <value>28.0</value>
            </plunge>
            <length>
              <value>6e+16</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C072876B/momenttensor">
          <derivedOriginID>smi:local/ndk/C072876B/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>10</stationCount>
            <componentCount>27</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>11</stationCount>
            <componentCount>24</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>3.65e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>-2.03e+18</value>
              <uncertainty>7e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>-7.5e+17</value>
              <uncertainty>1e+17</uncertainty>
            </Mtt>
            <Mpp>
              <value>2.78e+18</value>
              <uncertainty>8e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>2.15e+18</value>
              <uncertainty>2.3e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>-1.32e+18</value>
              <uncertainty>3e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>-8.8e+17</value>
              <uncertainty>6e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>7.0</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C072876B/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C072876B/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/B072876C/event">
      <preferredOriginID>smi:local/ndk/B072876C/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/B072876C/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/B072876C/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>TAJIKISTAN</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>B072876C</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/B072876C/origin#reforigin">
        <time>
          <value>1976-07-28T18:24:28.300000Z</value>
        </time>
        <latitude>
          <value>39.29</value>
        </latitude>
        <longitude>
          <value>72.79</value>
        </longitude>
        <depth>
          <value>50000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/B072876C/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/B072876C/origin#cmtorigin">
        <time>
          <value>1976-07-28T18:24:34.100000Z</value>
          <uncertainty>3.5</uncertainty>
        </time>
        <latitude>
          <value>39.27</value>
          <uncertainty>0.17</uncertainty>
        </latitude>
        <longitude>
          <value>71.67</value>
          <uncertainty>0.47</uncertainty>
        </longitude>
        <depth>
          <value>34200.0</value>
          <uncertainty>14600.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/B072876C/magnitude#moment_mag">
        <mag>
          <value>5.92</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/B072876C/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/B072876C/magnitude#mb">
        <mag>
          <value>5.1</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/B072876C/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/B072876C/magnitude#MS">
        <mag>
          <value>6.1</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/B072876C/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/B072876C/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>306.0</value>
            </strike>
            <dip>
              <value>41.0</value>
            </dip>
            <rake>
              <value>-38.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>66.0</value>
            </strike>
            <dip>
              <value>67.0</value>
            </dip>
            <rake>
              <value>-124.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>181.0</value>
            </azimuth>
            <plunge>
              <value>15.0</value>
            </plunge>
            <length>
              <value>1.045e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>293.0</value>
            </azimuth>
            <plunge>
              <value>55.0</value>
            </plunge>
            <length>
              <value>-8.66e+17</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>82.0</value>
            </azimuth>
            <plunge>
              <value>31.0</value>
            </plunge>
            <length>
              <value>-1.79e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/B072876C/momenttensor">
          <derivedOriginID>smi:local/ndk/B072876C/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>5</stationCount>
            <componentCount>6</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>9.55e+17</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>-5.58e+17</value>
              <uncertainty>8.1e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>9.32e+17</value>
              <uncertainty>1.72e+17</uncertainty>
            </Mtt>
            <Mpp>
              <value>-3.74e+17</value>
              <uncertainty>1.06e+17</uncertainty>
            </Mpp>
            <Mrt>
              <value>-4.25e+17</value>
              <uncertainty>2.24e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>-2.95e+17</value>
              <uncertainty>1.35e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>-9.6e+16</value>
              <uncertainty>7.6e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>3.8</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/B072876C/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/B072876C/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C072876D/event">
      <preferredOriginID>smi:local/ndk/C072876D/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C072876D/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C072876D/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>EASTERN CAUCASUS</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C072876D</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C072876D/origin#reforigin">
        <time>
          <value>1976-07-28T20:17:42.300000Z</value>
        </time>
        <latitude>
          <value>43.17</value>
        </latitude>
        <longitude>
          <value>45.6</value>
        </longitude>
        <depth>
          <value>21000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C072876D/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C072876D/origin#cmtorigin">
        <time>
          <value>1976-07-28T20:17:53.200000Z</value>
          <uncertainty>0.4</uncertainty>
        </time>
        <latitude>
          <value>43.15</value>
          <uncertainty>0.04</uncertainty>
        </latitude>
        <longitude>
          <value>45.45</value>
          <uncertainty>0.05</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C072876D/magnitude#moment_mag">
        <mag>
          <value>6.21</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C072876D/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C072876D/magnitude#mb">
        <mag>
          <value>5.4</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C072876D/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C072876D/magnitude#MS">
        <mag>
          <value>6.1</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C072876D/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C072876D/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>107.0</value>
            </strike>
            <dip>
              <value>15.0</value>
            </dip>
            <rake>
              <value>91.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>286.0</value>
            </strike>
            <dip>
              <value>75.0</value>
            </dip>
            <rake>
              <value>90.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>196.0</value>
            </azimuth>
            <plunge>
              <value>60.0</value>
            </plunge>
            <length>
              <value>2.63e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>16.0</value>
            </azimuth>
            <plunge>
              <value>30.0</value>
            </plunge>
            <length>
              <value>-2.55e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>286.0</value>
            </azimuth>
            <plunge>
              <value>0.0</value>
            </plunge>
            <length>
              <value>-8e+16</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C072876D/momenttensor">
          <derivedOriginID>smi:local/ndk/C072876D/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>11</stationCount>
            <componentCount>25</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>12</stationCount>
            <componentCount>17</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>2.59e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>1.32e+18</value>
              <uncertainty>4e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>-1.14e+18</value>
              <uncertainty>4e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>-1.8e+17</value>
              <uncertainty>3e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>-2.17e+18</value>
              <uncertainty>1.2e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>6.2e+17</value>
              <uncertainty>1.3e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>3.1e+17</value>
              <uncertainty>4e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>6.2</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C072876D/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C072876D/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C073176A/event">
      <preferredOriginID>smi:local/ndk/C073176A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C073176A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C073176A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>KERMADEC ISLANDS, NEW ZEALAND</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C073176A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C073176A/origin#reforigin">
        <time>
          <value>1976-07-31T00:46:58.000000Z</value>
        </time>
        <latitude>
          <value>-30.32</value>
        </latitude>
        <longitude>
          <value>-177.96</value>
        </longitude>
        <depth>
          <value>20000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C073176A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C073176A/origin#cmtorigin">
        <time>
          <value>1976-07-31T00:47:06.900000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>-30.26</value>
          <uncertainty>0.02</uncertainty>
        </latitude>
        <longitude>
          <value>-177.56</value>
          <uncertainty>0.01</uncertainty>
        </longitude>
        <depth>
          <value>50700.0</value>
          <uncertainty>700.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C073176A/magnitude#moment_mag">
        <mag>
          <value>6.44</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C073176A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C073176A/magnitude#mb">
        <mag>
          <value>5.8</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C073176A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C073176A/magnitude#MS">
        <mag>
          <value>6.2</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C073176A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C073176A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>196.0</value>
            </strike>
            <dip>
              <value>31.0</value>
            </dip>
            <rake>
              <value>93.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>13.0</value>
            </strike>
            <dip>
              <value>59.0</value>
            </dip>
            <rake>
              <value>89.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>279.0</value>
            </azimuth>
            <plunge>
              <value>75.0</value>
            </plunge>
            <length>
              <value>5.43e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>104.0</value>
            </azimuth>
            <plunge>
              <value>14.0</value>
            </plunge>
            <length>
              <value>-6.02e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>14.0</value>
            </azimuth>
            <plunge>
              <value>1.0</value>
            </plunge>
            <length>
              <value>5.8e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C073176A/momenttensor">
          <derivedOriginID>smi:local/ndk/C073176A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>12</stationCount>
            <componentCount>32</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>14</stationCount>
            <componentCount>31</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>5.73e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>4.72e+18</value>
              <uncertainty>8e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>2.2e+17</value>
              <uncertainty>7e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>-4.93e+18</value>
              <uncertainty>6e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>5.8e+17</value>
              <uncertainty>1.2e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>2.71e+18</value>
              <uncertainty>1e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>-1.43e+18</value>
              <uncertainty>5e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>8.0</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C073176A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C073176A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C080276A/event">
      <preferredOriginID>smi:local/ndk/C080276A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C080276A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C080276A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>VANUATU ISLANDS</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C080276A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C080276A/origin#reforigin">
        <time>
          <value>1976-08-02T10:55:25.700000Z</value>
        </time>
        <latitude>
          <value>-20.61</value>
        </latitude>
        <longitude>
          <value>169.27</value>
        </longitude>
        <depth>
          <value>52000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C080276A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C080276A/origin#cmtorigin">
        <time>
          <value>1976-08-02T10:55:34.500000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>-20.71</value>
          <uncertainty>0.02</uncertainty>
        </latitude>
        <longitude>
          <value>169.11</value>
          <uncertainty>0.01</uncertainty>
        </longitude>
        <depth>
          <value>42600.0</value>
          <uncertainty>700.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C080276A/magnitude#moment_mag">
        <mag>
          <value>6.85</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C080276A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C080276A/magnitude#mb">
        <mag>
          <value>6.1</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C080276A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C080276A/magnitude#MS">
        <mag>
          <value>6.9</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C080276A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C080276A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>336.0</value>
            </strike>
            <dip>
              <value>38.0</value>
            </dip>
            <rake>
              <value>88.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>159.0</value>
            </strike>
            <dip>
              <value>52.0</value>
            </dip>
            <rake>
              <value>92.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>79.0</value>
            </azimuth>
            <plunge>
              <value>83.0</value>
            </plunge>
            <length>
              <value>2.28e+19</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>248.0</value>
            </azimuth>
            <plunge>
              <value>7.0</value>
            </plunge>
            <length>
              <value>-2.48e+19</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>338.0</value>
            </azimuth>
            <plunge>
              <value>1.0</value>
            </plunge>
            <length>
              <value>1.9e+18</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C080276A/momenttensor">
          <derivedOriginID>smi:local/ndk/C080276A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>10</stationCount>
            <componentCount>25</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>15</stationCount>
            <componentCount>37</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>2.38e+19</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>2.22e+19</value>
              <uncertainty>3e+17</uncertainty>
            </Mrr>
            <Mtt>
              <value>-1.9e+18</value>
              <uncertainty>3e+17</uncertainty>
            </Mtt>
            <Mpp>
              <value>-2.03e+19</value>
              <uncertainty>2e+17</uncertainty>
            </Mpp>
            <Mrt>
              <value>1.6e+18</value>
              <uncertainty>6e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>-5.1e+18</value>
              <uncertainty>5e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>9.2e+18</value>
              <uncertainty>2e+17</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>13.0</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C080276A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C080276A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C081276A/event">
      <preferredOriginID>smi:local/ndk/C081276A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C081276A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C081276A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>MYANMAR</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C081276A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C081276A/origin#reforigin">
        <time>
          <value>1976-08-12T23:26:46.200000Z</value>
        </time>
        <latitude>
          <value>26.68</value>
        </latitude>
        <longitude>
          <value>97.07</value>
        </longitude>
        <depth>
          <value>27000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C081276A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C081276A/origin#cmtorigin">
        <time>
          <value>1976-08-12T23:26:51.800000Z</value>
          <uncertainty>0.4</uncertainty>
        </time>
        <latitude>
          <value>26.55</value>
          <uncertainty>0.04</uncertainty>
        </latitude>
        <longitude>
          <value>97.12</value>
          <uncertainty>0.04</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C081276A/magnitude#moment_mag">
        <mag>
          <value>5.87</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C081276A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C081276A/magnitude#mb">
        <mag>
          <value>6.4</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C081276A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C081276A/magnitude#MS">
        <mag>
          <value>6.1</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C081276A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C081276A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>148.0</value>
            </strike>
            <dip>
              <value>45.0</value>
            </dip>
            <rake>
              <value>93.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>323.0</value>
            </strike>
            <dip>
              <value>45.0</value>
            </dip>
            <rake>
              <value>87.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>154.0</value>
            </azimuth>
            <plunge>
              <value>88.0</value>
            </plunge>
            <length>
              <value>7.85e+17</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>55.0</value>
            </azimuth>
            <plunge>
              <value>0.0</value>
            </plunge>
            <length>
              <value>-8.14e+17</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>325.0</value>
            </azimuth>
            <plunge>
              <value>2.0</value>
            </plunge>
            <length>
              <value>2.8e+16</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C081276A/momenttensor">
          <derivedOriginID>smi:local/ndk/C081276A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>9</stationCount>
            <componentCount>19</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>7</stationCount>
            <componentCount>12</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>7.99e+17</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>7.84e+17</value>
              <uncertainty>2.1e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>-2.44e+17</value>
              <uncertainty>2.2e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>-5.4e+17</value>
              <uncertainty>2.1e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>-3.1e+16</value>
              <uncertainty>7.7e+16</uncertainty>
            </Mrt>
            <Mrp>
              <value>-9e+15</value>
              <uncertainty>1e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>3.95e+17</value>
              <uncertainty>2.2e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>4.4</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C081276A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C081276A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C081676A/event">
      <preferredOriginID>smi:local/ndk/C081676A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C081676A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C081676A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>SICHUAN, CHINA</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C081676A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C081676A/origin#reforigin">
        <time>
          <value>1976-08-16T14:06:45.900000Z</value>
        </time>
        <latitude>
          <value>32.75</value>
        </latitude>
        <longitude>
          <value>104.16</value>
        </longitude>
        <depth>
          <value>16000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C081676A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C081676A/origin#cmtorigin">
        <time>
          <value>1976-08-16T14:06:55.000000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>32.63</value>
          <uncertainty>0.03</uncertainty>
        </latitude>
        <longitude>
          <value>104.42</value>
          <uncertainty>0.02</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C081676A/magnitude#moment_mag">
        <mag>
          <value>6.67</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C081676A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C081676A/magnitude#mb">
        <mag>
          <value>6.1</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C081676A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C081676A/magnitude#MS">
        <mag>
          <value>6.9</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C081676A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C081676A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>29.0</value>
            </strike>
            <dip>
              <value>48.0</value>
            </dip>
            <rake>
              <value>122.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>166.0</value>
            </strike>
            <dip>
              <value>51.0</value>
            </dip>
            <rake>
              <value>60.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>12.0</value>
            </azimuth>
            <plunge>
              <value>67.0</value>
            </plunge>
            <length>
              <value>1.19e+19</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>277.0</value>
            </azimuth>
            <plunge>
              <value>2.0</value>
            </plunge>
            <length>
              <value>-1.38e+19</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>186.0</value>
            </azimuth>
            <plunge>
              <value>23.0</value>
            </plunge>
            <length>
              <value>1.9e+18</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C081676A/momenttensor">
          <derivedOriginID>smi:local/ndk/C081676A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>9</stationCount>
            <componentCount>20</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>12</stationCount>
            <componentCount>21</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>1.29e+19</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>1.03e+19</value>
              <uncertainty>2e+17</uncertainty>
            </Mrr>
            <Mtt>
              <value>3.1e+18</value>
              <uncertainty>2e+17</uncertainty>
            </Mtt>
            <Mpp>
              <value>-1.35e+19</value>
              <uncertainty>2e+17</uncertainty>
            </Mpp>
            <Mrt>
              <value>3.5e+18</value>
              <uncertainty>6e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>-1.3e+18</value>
              <uncertainty>8e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>-2.3e+18</value>
              <uncertainty>2e+17</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>10.8</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C081676A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C081676A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/M081676B/event">
      <preferredOriginID>smi:local/ndk/M081676B/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/M081676B/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/M081676B/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>MINDANAO, PHILIPPINES</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>M081676B</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/M081676B/origin#reforigin">
        <time>
          <value>1976-08-16T16:11:07.300000Z</value>
        </time>
        <latitude>
          <value>6.26</value>
        </latitude>
        <longitude>
          <value>124.02</value>
        </longitude>
        <depth>
          <value>33000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/M081676B/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/M081676B/origin#cmtorigin">
        <time>
          <value>1976-08-16T16:11:58.700000Z</value>
          <uncertainty>0.3</uncertainty>
        </time>
        <latitude>
          <value>7.07</value>
          <uncertainty>0.03</uncertainty>
        </latitude>
        <longitude>
          <value>123.75</value>
          <uncertainty>0.02</uncertainty>
        </longitude>
        <depth>
          <value>33000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/M081676B/magnitude#moment_mag">
        <mag>
          <value>7.96</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/M081676B/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/M081676B/magnitude#mb">
        <mag>
          <value>6.4</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/M081676B/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/M081676B/magnitude#MS">
        <mag>
          <value>7.9</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/M081676B/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/M081676B/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>341.0</value>
            </strike>
            <dip>
              <value>35.0</value>
            </dip>
            <rake>
              <value>92.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>158.0</value>
            </strike>
            <dip>
              <value>55.0</value>
            </dip>
            <rake>
              <value>89.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>62.0</value>
            </azimuth>
            <plunge>
              <value>80.0</value>
            </plunge>
            <length>
              <value>9.96e+20</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>249.0</value>
            </azimuth>
            <plunge>
              <value>10.0</value>
            </plunge>
            <length>
              <value>-1.183e+21</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>159.0</value>
            </azimuth>
            <plunge>
              <value>1.0</value>
            </plunge>
            <length>
              <value>1.87e+20</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/M081676B/momenttensor">
          <derivedOriginID>smi:local/ndk/M081676B/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>16</stationCount>
            <componentCount>37</componentCount>
            <shortestPeriod>200.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>1.09e+21</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>9.33e+20</value>
              <uncertainty>9e+18</uncertainty>
            </Mrr>
            <Mtt>
              <value>2.4e+19</value>
              <uncertainty>8e+18</uncertainty>
            </Mtt>
            <Mpp>
              <value>-9.57e+20</value>
              <uncertainty>9e+18</uncertainty>
            </Mpp>
            <Mrt>
              <value>1.45e+20</value>
              <uncertainty>8e+19</uncertainty>
            </Mrt>
            <Mrp>
              <value>-3.34e+20</value>
              <uncertainty>6.9e+19</uncertainty>
            </Mrp>
            <Mtp>
              <value>4.33e+20</value>
              <uncertainty>8e+18</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>43.4</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/M081676B/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/M081676B/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/B081776A/event">
      <preferredOriginID>smi:local/ndk/B081776A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/B081776A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/B081776A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>PHILIPPINE ISLANDS REGION</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>B081776A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/B081776A/origin#reforigin">
        <time>
          <value>1976-08-17T01:11:10.200000Z</value>
        </time>
        <latitude>
          <value>10.06</value>
        </latitude>
        <longitude>
          <value>125.87</value>
        </longitude>
        <depth>
          <value>34000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/B081776A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/B081776A/origin#cmtorigin">
        <time>
          <value>1976-08-17T01:11:16.500000Z</value>
          <uncertainty>0.6</uncertainty>
        </time>
        <latitude>
          <value>10.08</value>
          <uncertainty>0.05</uncertainty>
        </latitude>
        <longitude>
          <value>126.1</value>
          <uncertainty>0.09</uncertainty>
        </longitude>
        <depth>
          <value>47300.0</value>
          <uncertainty>5500.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/B081776A/magnitude#moment_mag">
        <mag>
          <value>6.02</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/B081776A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/B081776A/magnitude#mb">
        <mag>
          <value>6.0</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/B081776A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/B081776A/magnitude#MS">
        <mag>
          <value>5.7</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/B081776A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/B081776A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>340.0</value>
            </strike>
            <dip>
              <value>39.0</value>
            </dip>
            <rake>
              <value>-67.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>131.0</value>
            </strike>
            <dip>
              <value>55.0</value>
            </dip>
            <rake>
              <value>-108.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>234.0</value>
            </azimuth>
            <plunge>
              <value>8.0</value>
            </plunge>
            <length>
              <value>1.29e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>352.0</value>
            </azimuth>
            <plunge>
              <value>73.0</value>
            </plunge>
            <length>
              <value>-1.39e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>142.0</value>
            </azimuth>
            <plunge>
              <value>15.0</value>
            </plunge>
            <length>
              <value>1e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/B081776A/momenttensor">
          <derivedOriginID>smi:local/ndk/B081776A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>10</stationCount>
            <componentCount>17</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>1.34e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>-1.25e+18</value>
              <uncertainty>9e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>3.9e+17</value>
              <uncertainty>1.4e+17</uncertainty>
            </Mtt>
            <Mpp>
              <value>8.6e+17</value>
              <uncertainty>2e+17</uncertainty>
            </Mpp>
            <Mrt>
              <value>-5e+17</value>
              <uncertainty>1.5e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>7e+16</value>
              <uncertainty>1.5e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>-5.7e+17</value>
              <uncertainty>1.1e+17</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>5.2</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/B081776A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/B081776A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C081776B/event">
      <preferredOriginID>smi:local/ndk/C081776B/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C081776B/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C081776B/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>MINDANAO, PHILIPPINES</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C081776B</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C081776B/origin#reforigin">
        <time>
          <value>1976-08-17T04:19:27.300000Z</value>
        </time>
        <latitude>
          <value>7.25</value>
        </latitude>
        <longitude>
          <value>122.94</value>
        </longitude>
        <depth>
          <value>22000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C081776B/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C081776B/origin#cmtorigin">
        <time>
          <value>1976-08-17T04:19:39.800000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>7.14</value>
          <uncertainty>0.02</uncertainty>
        </latitude>
        <longitude>
          <value>123.01</value>
          <uncertainty>0.02</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C081776B/magnitude#moment_mag">
        <mag>
          <value>7.1</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C081776B/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C081776B/magnitude#mb">
        <mag>
          <value>6.2</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C081776B/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C081776B/magnitude#MS">
        <mag>
          <value>6.8</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C081776B/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C081776B/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>214.0</value>
            </strike>
            <dip>
              <value>64.0</value>
            </dip>
            <rake>
              <value>-172.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>120.0</value>
            </strike>
            <dip>
              <value>83.0</value>
            </dip>
            <rake>
              <value>-26.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>170.0</value>
            </azimuth>
            <plunge>
              <value>13.0</value>
            </plunge>
            <length>
              <value>6.13e+19</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>74.0</value>
            </azimuth>
            <plunge>
              <value>24.0</value>
            </plunge>
            <length>
              <value>-5.3e+19</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>286.0</value>
            </azimuth>
            <plunge>
              <value>63.0</value>
            </plunge>
            <length>
              <value>-8.3e+18</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C081776B/momenttensor">
          <derivedOriginID>smi:local/ndk/C081776B/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>10</stationCount>
            <componentCount>16</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>14</stationCount>
            <componentCount>28</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>5.71e+19</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>-1.22e+19</value>
              <uncertainty>7e+17</uncertainty>
            </Mrr>
            <Mtt>
              <value>5.31e+19</value>
              <uncertainty>6e+17</uncertainty>
            </Mtt>
            <Mpp>
              <value>-4.1e+19</value>
              <uncertainty>6e+17</uncertainty>
            </Mpp>
            <Mrt>
              <value>-1.92e+19</value>
              <uncertainty>3.3e+18</uncertainty>
            </Mrt>
            <Mrp>
              <value>1.33e+19</value>
              <uncertainty>2.5e+18</uncertainty>
            </Mrp>
            <Mtp>
              <value>2.11e+19</value>
              <uncertainty>5e+17</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>17.4</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C081776B/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C081776B/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C082176A/event">
      <preferredOriginID>smi:local/ndk/C082176A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C082176A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C082176A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>BANDA SEA</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C082176A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C082176A/origin#reforigin">
        <time>
          <value>1976-08-21T06:56:47.200000Z</value>
        </time>
        <latitude>
          <value>-6.72</value>
        </latitude>
        <longitude>
          <value>129.57</value>
        </longitude>
        <depth>
          <value>120000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C082176A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C082176A/origin#cmtorigin">
        <time>
          <value>1976-08-21T06:56:57.500000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>-6.9</value>
          <uncertainty>0.02</uncertainty>
        </latitude>
        <longitude>
          <value>129.74</value>
          <uncertainty>0.02</uncertainty>
        </longitude>
        <depth>
          <value>185500.0</value>
          <uncertainty>1200.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C082176A/magnitude#moment_mag">
        <mag>
          <value>6.34</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C082176A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C082176A/magnitude#mb">
        <mag>
          <value>6.0</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C082176A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C082176A/magnitude#MS">
        <mag>
          <value>0.0</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C082176A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C082176A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>318.0</value>
            </strike>
            <dip>
              <value>46.0</value>
            </dip>
            <rake>
              <value>-174.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>223.0</value>
            </strike>
            <dip>
              <value>85.0</value>
            </dip>
            <rake>
              <value>-44.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>279.0</value>
            </azimuth>
            <plunge>
              <value>26.0</value>
            </plunge>
            <length>
              <value>4.26e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>171.0</value>
            </azimuth>
            <plunge>
              <value>33.0</value>
            </plunge>
            <length>
              <value>-3.82e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>39.0</value>
            </azimuth>
            <plunge>
              <value>46.0</value>
            </plunge>
            <length>
              <value>-4.5e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C082176A/momenttensor">
          <derivedOriginID>smi:local/ndk/C082176A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>11</stationCount>
            <componentCount>28</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>12</stationCount>
            <componentCount>26</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>4.04e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>-5.8e+17</value>
              <uncertainty>5e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>-2.66e+18</value>
              <uncertainty>5e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>3.23e+18</value>
              <uncertainty>5e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>1.81e+18</value>
              <uncertainty>5e+16</uncertainty>
            </Mrt>
            <Mrp>
              <value>2.06e+18</value>
              <uncertainty>4e+16</uncertainty>
            </Mrp>
            <Mtp>
              <value>2.2e+17</value>
              <uncertainty>6e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>7.2</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C082176A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C082176A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C082176B/event">
      <preferredOriginID>smi:local/ndk/C082176B/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C082176B/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C082176B/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>SICHUAN, CHINA</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C082176B</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C082176B/origin#reforigin">
        <time>
          <value>1976-08-21T21:49:54.200000Z</value>
        </time>
        <latitude>
          <value>32.57</value>
        </latitude>
        <longitude>
          <value>104.25</value>
        </longitude>
        <depth>
          <value>33000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C082176B/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C082176B/origin#cmtorigin">
        <time>
          <value>1976-08-21T21:49:57.800000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>32.37</value>
          <uncertainty>0.02</uncertainty>
        </latitude>
        <longitude>
          <value>104.29</value>
          <uncertainty>0.02</uncertainty>
        </longitude>
        <depth>
          <value>15300.0</value>
          <uncertainty>800.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C082176B/magnitude#moment_mag">
        <mag>
          <value>6.26</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C082176B/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C082176B/magnitude#mb">
        <mag>
          <value>6.1</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C082176B/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C082176B/magnitude#MS">
        <mag>
          <value>6.4</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C082176B/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C082176B/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>198.0</value>
            </strike>
            <dip>
              <value>40.0</value>
            </dip>
            <rake>
              <value>113.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>349.0</value>
            </strike>
            <dip>
              <value>54.0</value>
            </dip>
            <rake>
              <value>72.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>208.0</value>
            </azimuth>
            <plunge>
              <value>74.0</value>
            </plunge>
            <length>
              <value>3.18e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>91.0</value>
            </azimuth>
            <plunge>
              <value>7.0</value>
            </plunge>
            <length>
              <value>-3.09e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>0.0</value>
            </azimuth>
            <plunge>
              <value>15.0</value>
            </plunge>
            <length>
              <value>-1e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C082176B/momenttensor">
          <derivedOriginID>smi:local/ndk/C082176B/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>12</stationCount>
            <componentCount>30</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>14</stationCount>
            <componentCount>28</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>3.14e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>2.87e+18</value>
              <uncertainty>4e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>1.1e+17</value>
              <uncertainty>3e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>-2.98e+18</value>
              <uncertainty>4e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>-7.8e+17</value>
              <uncertainty>1.5e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>8e+17</value>
              <uncertainty>1.7e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>-1.8e+17</value>
              <uncertainty>3e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>6.6</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C082176B/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C082176B/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C082376A/event">
      <preferredOriginID>smi:local/ndk/C082376A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C082376A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C082376A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>SICHUAN, CHINA</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C082376A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C082376A/origin#reforigin">
        <time>
          <value>1976-08-23T03:30:07.600000Z</value>
        </time>
        <latitude>
          <value>32.49</value>
        </latitude>
        <longitude>
          <value>104.18</value>
        </longitude>
        <depth>
          <value>33000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C082376A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C082376A/origin#cmtorigin">
        <time>
          <value>1976-08-23T03:30:11.500000Z</value>
          <uncertainty>0.3</uncertainty>
        </time>
        <latitude>
          <value>32.11</value>
          <uncertainty>0.04</uncertainty>
        </latitude>
        <longitude>
          <value>104.21</value>
          <uncertainty>0.03</uncertainty>
        </longitude>
        <depth>
          <value>19600.0</value>
          <uncertainty>1400.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C082376A/magnitude#moment_mag">
        <mag>
          <value>6.38</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C082376A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C082376A/magnitude#mb">
        <mag>
          <value>6.2</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C082376A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C082376A/magnitude#MS">
        <mag>
          <value>6.7</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C082376A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C082376A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>172.0</value>
            </strike>
            <dip>
              <value>45.0</value>
            </dip>
            <rake>
              <value>72.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>16.0</value>
            </strike>
            <dip>
              <value>48.0</value>
            </dip>
            <rake>
              <value>107.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>357.0</value>
            </azimuth>
            <plunge>
              <value>78.0</value>
            </plunge>
            <length>
              <value>4.03e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>94.0</value>
            </azimuth>
            <plunge>
              <value>2.0</value>
            </plunge>
            <length>
              <value>-5.16e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>185.0</value>
            </azimuth>
            <plunge>
              <value>12.0</value>
            </plunge>
            <length>
              <value>1.13e+18</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C082376A/momenttensor">
          <derivedOriginID>smi:local/ndk/C082376A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>12</stationCount>
            <componentCount>28</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>12</stationCount>
            <componentCount>24</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>4.6e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>3.89e+18</value>
              <uncertainty>1.4e+17</uncertainty>
            </Mrr>
            <Mtt>
              <value>1.23e+18</value>
              <uncertainty>1.2e+17</uncertainty>
            </Mtt>
            <Mpp>
              <value>-5.12e+18</value>
              <uncertainty>1.1e+17</uncertainty>
            </Mpp>
            <Mrt>
              <value>6.2e+17</value>
              <uncertainty>3.2e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>2.1e+17</value>
              <uncertainty>3.6e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>-4.8e+17</value>
              <uncertainty>1e+17</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>7.6</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C082376A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C082376A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C091576A/event">
      <preferredOriginID>smi:local/ndk/C091576A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C091576A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C091576A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>AUSTRIA</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C091576A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C091576A/origin#reforigin">
        <time>
          <value>1976-09-15T03:15:19.900000Z</value>
        </time>
        <latitude>
          <value>46.3</value>
        </latitude>
        <longitude>
          <value>13.2</value>
        </longitude>
        <depth>
          <value>10000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C091576A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C091576A/origin#cmtorigin">
        <time>
          <value>1976-09-15T03:15:26.300000Z</value>
          <uncertainty>0.3</uncertainty>
        </time>
        <latitude>
          <value>46.19</value>
          <uncertainty>0.03</uncertainty>
        </latitude>
        <longitude>
          <value>13.23</value>
          <uncertainty>0.04</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C091576A/magnitude#moment_mag">
        <mag>
          <value>5.97</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C091576A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C091576A/magnitude#mb">
        <mag>
          <value>5.7</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C091576A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C091576A/magnitude#MS">
        <mag>
          <value>6.0</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C091576A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C091576A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>251.0</value>
            </strike>
            <dip>
              <value>22.0</value>
            </dip>
            <rake>
              <value>100.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>60.0</value>
            </strike>
            <dip>
              <value>68.0</value>
            </dip>
            <rake>
              <value>86.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>323.0</value>
            </azimuth>
            <plunge>
              <value>67.0</value>
            </plunge>
            <length>
              <value>1.151e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>153.0</value>
            </azimuth>
            <plunge>
              <value>23.0</value>
            </plunge>
            <length>
              <value>-1.131e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>61.0</value>
            </azimuth>
            <plunge>
              <value>4.0</value>
            </plunge>
            <length>
              <value>-2e+16</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C091576A/momenttensor">
          <derivedOriginID>smi:local/ndk/C091576A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>11</stationCount>
            <componentCount>28</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>12</stationCount>
            <componentCount>21</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>1.141e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>7.96e+17</value>
              <uncertainty>2e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>-6.51e+17</value>
              <uncertainty>2.2e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>-1.45e+17</value>
              <uncertainty>1.4e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>6.97e+17</value>
              <uncertainty>7.1e+16</uncertainty>
            </Mrt>
            <Mrp>
              <value>4.4e+17</value>
              <uncertainty>6.6e+16</uncertainty>
            </Mrp>
            <Mtp>
              <value>-2.91e+17</value>
              <uncertainty>1.9e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>4.6</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C091576A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C091576A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C092276A/event">
      <preferredOriginID>smi:local/ndk/C092276A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C092276A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C092276A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>KURIL ISLANDS</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C092276A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C092276A/origin#reforigin">
        <time>
          <value>1976-09-22T00:16:08.200000Z</value>
        </time>
        <latitude>
          <value>44.88</value>
        </latitude>
        <longitude>
          <value>149.23</value>
        </longitude>
        <depth>
          <value>64000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C092276A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C092276A/origin#cmtorigin">
        <time>
          <value>1976-09-22T00:16:12.500000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>44.8</value>
          <uncertainty>0.02</uncertainty>
        </latitude>
        <longitude>
          <value>149.38</value>
          <uncertainty>0.02</uncertainty>
        </longitude>
        <depth>
          <value>46700.0</value>
          <uncertainty>1400.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C092276A/magnitude#moment_mag">
        <mag>
          <value>5.95</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C092276A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C092276A/magnitude#mb">
        <mag>
          <value>6.1</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C092276A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C092276A/magnitude#MS">
        <mag>
          <value>0.0</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C092276A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C092276A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>196.0</value>
            </strike>
            <dip>
              <value>24.0</value>
            </dip>
            <rake>
              <value>32.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>76.0</value>
            </strike>
            <dip>
              <value>77.0</value>
            </dip>
            <rake>
              <value>111.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>11.0</value>
            </azimuth>
            <plunge>
              <value>53.0</value>
            </plunge>
            <length>
              <value>1.093e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>149.0</value>
            </azimuth>
            <plunge>
              <value>29.0</value>
            </plunge>
            <length>
              <value>-1.037e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>251.0</value>
            </azimuth>
            <plunge>
              <value>20.0</value>
            </plunge>
            <length>
              <value>-5.5e+16</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C092276A/momenttensor">
          <derivedOriginID>smi:local/ndk/C092276A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>11</stationCount>
            <componentCount>31</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>12</stationCount>
            <componentCount>17</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>1.065e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>4.44e+17</value>
              <uncertainty>1.4e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>-2.04e+17</value>
              <uncertainty>1.3e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>-2.4e+17</value>
              <uncertainty>1.2e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>9.01e+17</value>
              <uncertainty>3e+16</uncertainty>
            </Mrt>
            <Mrp>
              <value>1.14e+17</value>
              <uncertainty>1.9e+16</uncertainty>
            </Mrp>
            <Mtp>
              <value>-4.05e+17</value>
              <uncertainty>1.2e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>4.6</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C092276A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C092276A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C092976A/event">
      <preferredOriginID>smi:local/ndk/C092976A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C092976A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C092976A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>MINDANAO, PHILIPPINES</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C092976A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C092976A/origin#reforigin">
        <time>
          <value>1976-09-29T21:02:32.700000Z</value>
        </time>
        <latitude>
          <value>6.92</value>
        </latitude>
        <longitude>
          <value>124.07</value>
        </longitude>
        <depth>
          <value>41000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C092976A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C092976A/origin#cmtorigin">
        <time>
          <value>1976-09-29T21:02:31.500000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>6.61</value>
          <uncertainty>0.03</uncertainty>
        </latitude>
        <longitude>
          <value>124.24</value>
          <uncertainty>0.03</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C092976A/magnitude#moment_mag">
        <mag>
          <value>5.72</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C092976A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C092976A/magnitude#mb">
        <mag>
          <value>6.0</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C092976A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C092976A/magnitude#MS">
        <mag>
          <value>5.4</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C092976A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C092976A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>232.0</value>
            </strike>
            <dip>
              <value>35.0</value>
            </dip>
            <rake>
              <value>-76.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>34.0</value>
            </strike>
            <dip>
              <value>56.0</value>
            </dip>
            <rake>
              <value>-100.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>131.0</value>
            </azimuth>
            <plunge>
              <value>11.0</value>
            </plunge>
            <length>
              <value>4.5e+17</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>273.0</value>
            </azimuth>
            <plunge>
              <value>77.0</value>
            </plunge>
            <length>
              <value>-5.06e+17</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>40.0</value>
            </azimuth>
            <plunge>
              <value>8.0</value>
            </plunge>
            <length>
              <value>5.7e+16</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C092976A/momenttensor">
          <derivedOriginID>smi:local/ndk/C092976A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>10</stationCount>
            <componentCount>21</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>14</stationCount>
            <componentCount>19</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>4.78e+17</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>-4.62e+17</value>
              <uncertainty>9e+15</uncertainty>
            </Mrr>
            <Mtt>
              <value>2.22e+17</value>
              <uncertainty>1.1e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>2.4e+17</value>
              <uncertainty>1e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>-5.3e+16</value>
              <uncertainty>4.6e+16</uncertainty>
            </Mrt>
            <Mrp>
              <value>-1.81e+17</value>
              <uncertainty>3.7e+16</uncertainty>
            </Mrp>
            <Mtp>
              <value>1.87e+17</value>
              <uncertainty>9e+15</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>3.6</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C092976A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C092976A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C093076A/event">
      <preferredOriginID>smi:local/ndk/C093076A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C093076A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C093076A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>KERMADEC ISLANDS, NEW ZEALAND</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C093076A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C093076A/origin#reforigin">
        <time>
          <value>1976-09-30T23:34:14.400000Z</value>
        </time>
        <latitude>
          <value>-30.24</value>
        </latitude>
        <longitude>
          <value>-177.88</value>
        </longitude>
        <depth>
          <value>32000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C093076A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C093076A/origin#cmtorigin">
        <time>
          <value>1976-09-30T23:34:20.600000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>-30.41</value>
          <uncertainty>0.02</uncertainty>
        </latitude>
        <longitude>
          <value>-177.32</value>
          <uncertainty>0.01</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C093076A/magnitude#moment_mag">
        <mag>
          <value>6.6</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C093076A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C093076A/magnitude#mb">
        <mag>
          <value>5.7</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C093076A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C093076A/magnitude#MS">
        <mag>
          <value>6.5</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C093076A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C093076A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>208.0</value>
            </strike>
            <dip>
              <value>15.0</value>
            </dip>
            <rake>
              <value>100.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>18.0</value>
            </strike>
            <dip>
              <value>75.0</value>
            </dip>
            <rake>
              <value>87.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>284.0</value>
            </azimuth>
            <plunge>
              <value>60.0</value>
            </plunge>
            <length>
              <value>9.9e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>110.0</value>
            </azimuth>
            <plunge>
              <value>30.0</value>
            </plunge>
            <length>
              <value>-1.03e+19</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>19.0</value>
            </azimuth>
            <plunge>
              <value>3.0</value>
            </plunge>
            <length>
              <value>4.1e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C093076A/momenttensor">
          <derivedOriginID>smi:local/ndk/C093076A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>11</stationCount>
            <componentCount>31</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>15</stationCount>
            <componentCount>32</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>1.01e+19</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>4.91e+18</value>
              <uncertainty>5e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>-4.3e+17</value>
              <uncertainty>4e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>-4.49e+18</value>
              <uncertainty>4e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>2.63e+18</value>
              <uncertainty>2.1e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>8.29e+18</value>
              <uncertainty>2.4e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>-2.07e+18</value>
              <uncertainty>4e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>9.8</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C093076A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C093076A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C100576A/event">
      <preferredOriginID>smi:local/ndk/C100576A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C100576A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C100576A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>NEW BRITAIN REGION, P.N.G.</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C100576A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C100576A/origin#reforigin">
        <time>
          <value>1976-10-05T18:02:15.400000Z</value>
        </time>
        <latitude>
          <value>-6.43</value>
        </latitude>
        <longitude>
          <value>153.0</value>
        </longitude>
        <depth>
          <value>22000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C100576A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C100576A/origin#cmtorigin">
        <time>
          <value>1976-10-05T18:02:20.500000Z</value>
          <uncertainty>0.1</uncertainty>
        </time>
        <latitude>
          <value>-6.57</value>
          <uncertainty>0.01</uncertainty>
        </latitude>
        <longitude>
          <value>153.1</value>
          <uncertainty>0.01</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C100576A/magnitude#moment_mag">
        <mag>
          <value>6.34</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C100576A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C100576A/magnitude#mb">
        <mag>
          <value>6.3</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C100576A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C100576A/magnitude#MS">
        <mag>
          <value>6.0</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C100576A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C100576A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>293.0</value>
            </strike>
            <dip>
              <value>41.0</value>
            </dip>
            <rake>
              <value>-60.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>76.0</value>
            </strike>
            <dip>
              <value>55.0</value>
            </dip>
            <rake>
              <value>-114.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>183.0</value>
            </azimuth>
            <plunge>
              <value>7.0</value>
            </plunge>
            <length>
              <value>3.49e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>293.0</value>
            </azimuth>
            <plunge>
              <value>69.0</value>
            </plunge>
            <length>
              <value>-4.56e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>90.0</value>
            </azimuth>
            <plunge>
              <value>19.0</value>
            </plunge>
            <length>
              <value>1.07e+18</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C100576A/momenttensor">
          <derivedOriginID>smi:local/ndk/C100576A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>11</stationCount>
            <componentCount>29</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>17</stationCount>
            <componentCount>41</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>4.02e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>-3.81e+18</value>
              <uncertainty>3e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>3.34e+18</value>
              <uncertainty>3e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>4.7e+17</value>
              <uncertainty>3e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>-1.03e+18</value>
              <uncertainty>1.8e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>-1.7e+18</value>
              <uncertainty>1.6e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>-3.6e+17</value>
              <uncertainty>3e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>7.2</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C100576A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C100576A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C101276A/event">
      <preferredOriginID>smi:local/ndk/C101276A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C101276A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C101276A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>SOLOMON ISLANDS</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C101276A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C101276A/origin#reforigin">
        <time>
          <value>1976-10-12T00:40:52.900000Z</value>
        </time>
        <latitude>
          <value>-10.45</value>
        </latitude>
        <longitude>
          <value>161.29</value>
        </longitude>
        <depth>
          <value>106000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C101276A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C101276A/origin#cmtorigin">
        <time>
          <value>1976-10-12T00:40:55.900000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>-10.65</value>
          <uncertainty>0.02</uncertainty>
        </latitude>
        <longitude>
          <value>161.42</value>
          <uncertainty>0.02</uncertainty>
        </longitude>
        <depth>
          <value>99000.0</value>
          <uncertainty>1600.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C101276A/magnitude#moment_mag">
        <mag>
          <value>5.95</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C101276A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C101276A/magnitude#mb">
        <mag>
          <value>6.0</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C101276A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C101276A/magnitude#MS">
        <mag>
          <value>0.0</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C101276A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C101276A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>202.0</value>
            </strike>
            <dip>
              <value>4.0</value>
            </dip>
            <rake>
              <value>-50.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>342.0</value>
            </strike>
            <dip>
              <value>87.0</value>
            </dip>
            <rake>
              <value>-93.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>74.0</value>
            </azimuth>
            <plunge>
              <value>42.0</value>
            </plunge>
            <length>
              <value>1.031e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>249.0</value>
            </azimuth>
            <plunge>
              <value>48.0</value>
            </plunge>
            <length>
              <value>-1.081e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>342.0</value>
            </azimuth>
            <plunge>
              <value>3.0</value>
            </plunge>
            <length>
              <value>5e+16</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C101276A/momenttensor">
          <derivedOriginID>smi:local/ndk/C101276A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>11</stationCount>
            <componentCount>30</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>14</stationCount>
            <componentCount>23</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>1.056e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>-1.49e+17</value>
              <uncertainty>1.9e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>2.3e+16</value>
              <uncertainty>2.6e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>1.26e+17</value>
              <uncertainty>2.5e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>3.37e+17</value>
              <uncertainty>1.5e+16</uncertainty>
            </Mrt>
            <Mrp>
              <value>-9.91e+17</value>
              <uncertainty>1.4e+16</uncertainty>
            </Mrp>
            <Mtp>
              <value>2.7e+16</value>
              <uncertainty>2.2e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>4.8</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C101276A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C101276A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C102976A/event">
      <preferredOriginID>smi:local/ndk/C102976A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C102976A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C102976A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>IRIAN JAYA, INDONESIA</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C102976A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C102976A/origin#reforigin">
        <time>
          <value>1976-10-29T02:51:07.600000Z</value>
        </time>
        <latitude>
          <value>-4.52</value>
        </latitude>
        <longitude>
          <value>139.92</value>
        </longitude>
        <depth>
          <value>33000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C102976A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C102976A/origin#cmtorigin">
        <time>
          <value>1976-10-29T02:51:12.300000Z</value>
          <uncertainty>0.1</uncertainty>
        </time>
        <latitude>
          <value>-4.55</value>
          <uncertainty>0.01</uncertainty>
        </latitude>
        <longitude>
          <value>139.93</value>
          <uncertainty>0.01</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C102976A/magnitude#moment_mag">
        <mag>
          <value>6.82</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C102976A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C102976A/magnitude#mb">
        <mag>
          <value>6.1</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C102976A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C102976A/magnitude#MS">
        <mag>
          <value>7.1</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C102976A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C102976A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>1.0</value>
            </strike>
            <dip>
              <value>80.0</value>
            </dip>
            <rake>
              <value>174.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>92.0</value>
            </strike>
            <dip>
              <value>84.0</value>
            </dip>
            <rake>
              <value>10.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>317.0</value>
            </azimuth>
            <plunge>
              <value>11.0</value>
            </plunge>
            <length>
              <value>2.56e+19</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>227.0</value>
            </azimuth>
            <plunge>
              <value>3.0</value>
            </plunge>
            <length>
              <value>-1.66e+19</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>123.0</value>
            </azimuth>
            <plunge>
              <value>79.0</value>
            </plunge>
            <length>
              <value>-9e+18</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C102976A/momenttensor">
          <derivedOriginID>smi:local/ndk/C102976A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>10</stationCount>
            <componentCount>23</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>18</stationCount>
            <componentCount>41</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>2.11e+19</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>-7.8e+18</value>
              <uncertainty>2e+17</uncertainty>
            </Mrr>
            <Mtt>
              <value>5.3e+18</value>
              <uncertainty>2e+17</uncertainty>
            </Mtt>
            <Mpp>
              <value>2.5e+18</value>
              <uncertainty>2e+17</uncertainty>
            </Mpp>
            <Mrt>
              <value>4.9e+18</value>
              <uncertainty>1.2e+18</uncertainty>
            </Mrt>
            <Mrp>
              <value>4.1e+18</value>
              <uncertainty>1.1e+18</uncertainty>
            </Mrp>
            <Mtp>
              <value>2.04e+19</value>
              <uncertainty>1e+17</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>12.6</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C102976A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C102976A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C110276A/event">
      <preferredOriginID>smi:local/ndk/C110276A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C110276A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C110276A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>MID-INDIAN RIDGE</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C110276A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C110276A/origin#reforigin">
        <time>
          <value>1976-11-02T07:13:15.700000Z</value>
        </time>
        <latitude>
          <value>-29.35</value>
        </latitude>
        <longitude>
          <value>77.66</value>
        </longitude>
        <depth>
          <value>33000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C110276A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C110276A/origin#cmtorigin">
        <time>
          <value>1976-11-02T07:13:23.200000Z</value>
          <uncertainty>0.1</uncertainty>
        </time>
        <latitude>
          <value>-28.75</value>
          <uncertainty>0.01</uncertainty>
        </latitude>
        <longitude>
          <value>77.84</value>
          <uncertainty>0.01</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C110276A/magnitude#moment_mag">
        <mag>
          <value>6.56</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C110276A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C110276A/magnitude#mb">
        <mag>
          <value>5.8</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C110276A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C110276A/magnitude#MS">
        <mag>
          <value>6.5</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C110276A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C110276A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>223.0</value>
            </strike>
            <dip>
              <value>29.0</value>
            </dip>
            <rake>
              <value>-93.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>46.0</value>
            </strike>
            <dip>
              <value>62.0</value>
            </dip>
            <rake>
              <value>-88.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>135.0</value>
            </azimuth>
            <plunge>
              <value>16.0</value>
            </plunge>
            <length>
              <value>8.8e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>321.0</value>
            </azimuth>
            <plunge>
              <value>73.0</value>
            </plunge>
            <length>
              <value>-8.92e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>226.0</value>
            </azimuth>
            <plunge>
              <value>2.0</value>
            </plunge>
            <length>
              <value>1.2e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C110276A/momenttensor">
          <derivedOriginID>smi:local/ndk/C110276A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>11</stationCount>
            <componentCount>28</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>17</stationCount>
            <componentCount>36</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>8.86e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>-7.49e+18</value>
              <uncertainty>6e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>3.68e+18</value>
              <uncertainty>6e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>3.8e+18</value>
              <uncertainty>6e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>-3.59e+18</value>
              <uncertainty>2.7e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>-3.23e+18</value>
              <uncertainty>2.8e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>3.62e+18</value>
              <uncertainty>5e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>9.4</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C110276A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C110276A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C110676A/event">
      <preferredOriginID>smi:local/ndk/C110676A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C110676A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C110676A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>SICHUAN, CHINA</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C110676A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C110676A/origin#reforigin">
        <time>
          <value>1976-11-06T18:04:08.900000Z</value>
        </time>
        <latitude>
          <value>27.6</value>
        </latitude>
        <longitude>
          <value>101.05</value>
        </longitude>
        <depth>
          <value>33000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C110676A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C110676A/origin#cmtorigin">
        <time>
          <value>1976-11-06T18:04:16.000000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>27.5</value>
          <uncertainty>0.02</uncertainty>
        </latitude>
        <longitude>
          <value>101.4</value>
          <uncertainty>0.02</uncertainty>
        </longitude>
        <depth>
          <value>22700.0</value>
          <uncertainty>1500.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C110676A/magnitude#moment_mag">
        <mag>
          <value>6.31</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C110676A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C110676A/magnitude#mb">
        <mag>
          <value>5.8</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C110676A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C110676A/magnitude#MS">
        <mag>
          <value>6.5</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C110676A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C110676A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>19.0</value>
            </strike>
            <dip>
              <value>66.0</value>
            </dip>
            <rake>
              <value>-6.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>111.0</value>
            </strike>
            <dip>
              <value>84.0</value>
            </dip>
            <rake>
              <value>-156.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>243.0</value>
            </azimuth>
            <plunge>
              <value>12.0</value>
            </plunge>
            <length>
              <value>4.21e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>337.0</value>
            </azimuth>
            <plunge>
              <value>21.0</value>
            </plunge>
            <length>
              <value>-3.07e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>123.0</value>
            </azimuth>
            <plunge>
              <value>66.0</value>
            </plunge>
            <length>
              <value>-1.15e+18</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C110676A/momenttensor">
          <derivedOriginID>smi:local/ndk/C110676A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>12</stationCount>
            <componentCount>31</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>14</stationCount>
            <componentCount>29</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>3.64e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>-1.13e+18</value>
              <uncertainty>5e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>-1.5e+18</value>
              <uncertainty>5e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>2.63e+18</value>
              <uncertainty>5e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>-1.1e+18</value>
              <uncertainty>1.4e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>7.6e+17</value>
              <uncertainty>1.3e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>-2.68e+18</value>
              <uncertainty>5e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>7.0</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C110676A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C110676A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C110776A/event">
      <preferredOriginID>smi:local/ndk/C110776A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C110776A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C110776A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>NORTHERN AND CENTRAL IRAN</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C110776A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C110776A/origin#reforigin">
        <time>
          <value>1976-11-07T04:00:51.600000Z</value>
        </time>
        <latitude>
          <value>33.8</value>
        </latitude>
        <longitude>
          <value>59.15</value>
        </longitude>
        <depth>
          <value>13000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C110776A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C110776A/origin#cmtorigin">
        <time>
          <value>1976-11-07T04:00:56.000000Z</value>
          <uncertainty>0.3</uncertainty>
        </time>
        <latitude>
          <value>34.07</value>
          <uncertainty>0.03</uncertainty>
        </latitude>
        <longitude>
          <value>59.15</value>
          <uncertainty>0.03</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C110776A/magnitude#moment_mag">
        <mag>
          <value>5.96</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C110776A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C110776A/magnitude#mb">
        <mag>
          <value>5.6</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C110776A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C110776A/magnitude#MS">
        <mag>
          <value>6.2</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C110776A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C110776A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>260.0</value>
            </strike>
            <dip>
              <value>78.0</value>
            </dip>
            <rake>
              <value>6.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>169.0</value>
            </strike>
            <dip>
              <value>84.0</value>
            </dip>
            <rake>
              <value>168.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>124.0</value>
            </azimuth>
            <plunge>
              <value>12.0</value>
            </plunge>
            <length>
              <value>1.176e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>215.0</value>
            </azimuth>
            <plunge>
              <value>4.0</value>
            </plunge>
            <length>
              <value>-1.01e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>323.0</value>
            </azimuth>
            <plunge>
              <value>77.0</value>
            </plunge>
            <length>
              <value>-1.66e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C110776A/momenttensor">
          <derivedOriginID>smi:local/ndk/C110776A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>11</stationCount>
            <componentCount>21</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>15</stationCount>
            <componentCount>25</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>1.093e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>-1.08e+17</value>
              <uncertainty>2.3e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>-3.17e+17</value>
              <uncertainty>2.4e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>4.25e+17</value>
              <uncertainty>2.2e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>-1.12e+17</value>
              <uncertainty>1.07e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>-2.65e+17</value>
              <uncertainty>9.9e+16</uncertainty>
            </Mrp>
            <Mtp>
              <value>9.93e+17</value>
              <uncertainty>1.9e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>4.6</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C110776A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C110776A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C110776B/event">
      <preferredOriginID>smi:local/ndk/C110776B/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C110776B/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C110776B/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>MINDANAO, PHILIPPINES</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C110776B</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C110776B/origin#reforigin">
        <time>
          <value>1976-11-07T17:09:06.100000Z</value>
        </time>
        <latitude>
          <value>8.48</value>
        </latitude>
        <longitude>
          <value>126.38</value>
        </longitude>
        <depth>
          <value>60000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C110776B/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C110776B/origin#cmtorigin">
        <time>
          <value>1976-11-07T17:09:13.700000Z</value>
          <uncertainty>0.1</uncertainty>
        </time>
        <latitude>
          <value>8.35</value>
          <uncertainty>0.02</uncertainty>
        </latitude>
        <longitude>
          <value>126.86</value>
          <uncertainty>0.01</uncertainty>
        </longitude>
        <depth>
          <value>42100.0</value>
          <uncertainty>700.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C110776B/magnitude#moment_mag">
        <mag>
          <value>6.8</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C110776B/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C110776B/magnitude#mb">
        <mag>
          <value>6.0</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C110776B/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C110776B/magnitude#MS">
        <mag>
          <value>6.8</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C110776B/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C110776B/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>162.0</value>
            </strike>
            <dip>
              <value>39.0</value>
            </dip>
            <rake>
              <value>49.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>30.0</value>
            </strike>
            <dip>
              <value>62.0</value>
            </dip>
            <rake>
              <value>118.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>345.0</value>
            </azimuth>
            <plunge>
              <value>62.0</value>
            </plunge>
            <length>
              <value>2.12e+19</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>100.0</value>
            </azimuth>
            <plunge>
              <value>13.0</value>
            </plunge>
            <length>
              <value>-1.94e+19</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>196.0</value>
            </azimuth>
            <plunge>
              <value>24.0</value>
            </plunge>
            <length>
              <value>-1.8e+18</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C110776B/momenttensor">
          <derivedOriginID>smi:local/ndk/C110776B/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>10</stationCount>
            <componentCount>28</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>16</stationCount>
            <componentCount>37</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>2.03e+19</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>1.54e+19</value>
              <uncertainty>2e+17</uncertainty>
            </Mrr>
            <Mtt>
              <value>2.3e+18</value>
              <uncertainty>2e+17</uncertainty>
            </Mtt>
            <Mpp>
              <value>-1.77e+19</value>
              <uncertainty>2e+17</uncertainty>
            </Mpp>
            <Mrt>
              <value>9.9e+18</value>
              <uncertainty>4e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>6.1e+18</value>
              <uncertainty>4e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>-1.7e+18</value>
              <uncertainty>1e+17</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>12.4</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C110776B/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C110776B/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C110876A/event">
      <preferredOriginID>smi:local/ndk/C110876A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C110876A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C110876A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>NEAR EAST COAST OF HONSHU, JAPAN</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C110876A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C110876A/origin#reforigin">
        <time>
          <value>1976-11-08T08:19:27.100000Z</value>
        </time>
        <latitude>
          <value>38.09</value>
        </latitude>
        <longitude>
          <value>142.24</value>
        </longitude>
        <depth>
          <value>38000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C110876A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C110876A/origin#cmtorigin">
        <time>
          <value>1976-11-08T08:19:31.900000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>38.03</value>
          <uncertainty>0.02</uncertainty>
        </latitude>
        <longitude>
          <value>142.23</value>
          <uncertainty>0.02</uncertainty>
        </longitude>
        <depth>
          <value>32400.0</value>
          <uncertainty>1200.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C110876A/magnitude#moment_mag">
        <mag>
          <value>6.23</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C110876A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C110876A/magnitude#mb">
        <mag>
          <value>5.9</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C110876A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C110876A/magnitude#MS">
        <mag>
          <value>6.0</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C110876A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C110876A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>188.0</value>
            </strike>
            <dip>
              <value>19.0</value>
            </dip>
            <rake>
              <value>70.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>30.0</value>
            </strike>
            <dip>
              <value>72.0</value>
            </dip>
            <rake>
              <value>97.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>311.0</value>
            </azimuth>
            <plunge>
              <value>62.0</value>
            </plunge>
            <length>
              <value>2.7e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>114.0</value>
            </azimuth>
            <plunge>
              <value>27.0</value>
            </plunge>
            <length>
              <value>-2.82e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>208.0</value>
            </azimuth>
            <plunge>
              <value>7.0</value>
            </plunge>
            <length>
              <value>1.3e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C110876A/momenttensor">
          <derivedOriginID>smi:local/ndk/C110876A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>10</stationCount>
            <componentCount>27</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>10</stationCount>
            <componentCount>22</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>2.76e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>1.56e+18</value>
              <uncertainty>3e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>-4e+16</value>
              <uncertainty>3e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>-1.51e+18</value>
              <uncertainty>3e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>1.17e+18</value>
              <uncertainty>8e+16</uncertainty>
            </Mrt>
            <Mrp>
              <value>1.88e+18</value>
              <uncertainty>1e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>-6.2e+17</value>
              <uncertainty>3e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>6.4</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C110876A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C110876A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C111576A/event">
      <preferredOriginID>smi:local/ndk/C111576A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C111576A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C111576A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>NORTHEASTERN CHINA</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C111576A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C111576A/origin#reforigin">
        <time>
          <value>1976-11-15T13:53:00.600000Z</value>
        </time>
        <latitude>
          <value>39.44</value>
        </latitude>
        <longitude>
          <value>117.69</value>
        </longitude>
        <depth>
          <value>15000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C111576A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C111576A/origin#cmtorigin">
        <time>
          <value>1976-11-15T13:53:07.200000Z</value>
          <uncertainty>0.1</uncertainty>
        </time>
        <latitude>
          <value>39.45</value>
          <uncertainty>0.01</uncertainty>
        </latitude>
        <longitude>
          <value>117.71</value>
          <uncertainty>0.02</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C111576A/magnitude#moment_mag">
        <mag>
          <value>6.36</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C111576A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C111576A/magnitude#mb">
        <mag>
          <value>6.0</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C111576A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C111576A/magnitude#MS">
        <mag>
          <value>6.3</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C111576A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C111576A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>318.0</value>
            </strike>
            <dip>
              <value>56.0</value>
            </dip>
            <rake>
              <value>-9.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>53.0</value>
            </strike>
            <dip>
              <value>83.0</value>
            </dip>
            <rake>
              <value>-145.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>181.0</value>
            </azimuth>
            <plunge>
              <value>18.0</value>
            </plunge>
            <length>
              <value>4.45e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>281.0</value>
            </azimuth>
            <plunge>
              <value>29.0</value>
            </plunge>
            <length>
              <value>-4.18e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>63.0</value>
            </azimuth>
            <plunge>
              <value>55.0</value>
            </plunge>
            <length>
              <value>-2.7e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C111576A/momenttensor">
          <derivedOriginID>smi:local/ndk/C111576A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>12</stationCount>
            <componentCount>35</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>15</stationCount>
            <componentCount>37</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>4.32e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>-7.4e+17</value>
              <uncertainty>4e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>3.88e+18</value>
              <uncertainty>3e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>-3.14e+18</value>
              <uncertainty>4e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>-1.72e+18</value>
              <uncertainty>1.6e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>-1.61e+18</value>
              <uncertainty>1.6e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>-6.3e+17</value>
              <uncertainty>3e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>7.2</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C111576A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C111576A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C111676A/event">
      <preferredOriginID>smi:local/ndk/C111676A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C111676A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C111676A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>MID-INDIAN RIDGE</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C111676A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C111676A/origin#reforigin">
        <time>
          <value>1976-11-16T18:20:50.200000Z</value>
        </time>
        <latitude>
          <value>-41.64</value>
        </latitude>
        <longitude>
          <value>80.21</value>
        </longitude>
        <depth>
          <value>33000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C111676A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C111676A/origin#cmtorigin">
        <time>
          <value>1976-11-16T18:20:53.300000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>-41.32</value>
          <uncertainty>0.02</uncertainty>
        </latitude>
        <longitude>
          <value>79.88</value>
          <uncertainty>0.02</uncertainty>
        </longitude>
        <depth>
          <value>15400.0</value>
          <uncertainty>1800.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C111676A/magnitude#moment_mag">
        <mag>
          <value>6.18</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C111676A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C111676A/magnitude#mb">
        <mag>
          <value>5.3</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C111676A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C111676A/magnitude#MS">
        <mag>
          <value>6.2</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C111676A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C111676A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>323.0</value>
            </strike>
            <dip>
              <value>84.0</value>
            </dip>
            <rake>
              <value>5.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>232.0</value>
            </strike>
            <dip>
              <value>85.0</value>
            </dip>
            <rake>
              <value>174.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>188.0</value>
            </azimuth>
            <plunge>
              <value>7.0</value>
            </plunge>
            <length>
              <value>2.35e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>278.0</value>
            </azimuth>
            <plunge>
              <value>1.0</value>
            </plunge>
            <length>
              <value>-2.27e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>13.0</value>
            </azimuth>
            <plunge>
              <value>83.0</value>
            </plunge>
            <length>
              <value>-9e+16</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C111676A/momenttensor">
          <derivedOriginID>smi:local/ndk/C111676A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>14</stationCount>
            <componentCount>31</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>16</stationCount>
            <componentCount>34</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>2.31e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>-5e+16</value>
              <uncertainty>3e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>2.23e+18</value>
              <uncertainty>3e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>-2.18e+18</value>
              <uncertainty>3e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>-3e+17</value>
              <uncertainty>1.1e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>2e+16</value>
              <uncertainty>1e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>-6.1e+17</value>
              <uncertainty>3e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>6.0</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C111676A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C111676A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C111876A/event">
      <preferredOriginID>smi:local/ndk/C111876A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C111876A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C111876A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>SOLOMON ISLANDS</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C111876A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C111876A/origin#reforigin">
        <time>
          <value>1976-11-18T03:24:00.200000Z</value>
        </time>
        <latitude>
          <value>-8.82</value>
        </latitude>
        <longitude>
          <value>156.94</value>
        </longitude>
        <depth>
          <value>33000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C111876A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C111876A/origin#cmtorigin">
        <time>
          <value>1976-11-18T03:24:04.200000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>-8.75</value>
          <uncertainty>0.02</uncertainty>
        </latitude>
        <longitude>
          <value>157.07</value>
          <uncertainty>0.01</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C111876A/magnitude#moment_mag">
        <mag>
          <value>6.41</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C111876A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C111876A/magnitude#mb">
        <mag>
          <value>6.1</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C111876A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C111876A/magnitude#MS">
        <mag>
          <value>6.5</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C111876A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C111876A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>254.0</value>
            </strike>
            <dip>
              <value>77.0</value>
            </dip>
            <rake>
              <value>-3.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>345.0</value>
            </strike>
            <dip>
              <value>87.0</value>
            </dip>
            <rake>
              <value>-167.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>119.0</value>
            </azimuth>
            <plunge>
              <value>7.0</value>
            </plunge>
            <length>
              <value>4.93e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>210.0</value>
            </azimuth>
            <plunge>
              <value>11.0</value>
            </plunge>
            <length>
              <value>-5.55e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>357.0</value>
            </azimuth>
            <plunge>
              <value>77.0</value>
            </plunge>
            <length>
              <value>6.2e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C111876A/momenttensor">
          <derivedOriginID>smi:local/ndk/C111876A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>10</stationCount>
            <componentCount>28</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>14</stationCount>
            <componentCount>30</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>5.24e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>4.6e+17</value>
              <uncertainty>6e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>-2.86e+18</value>
              <uncertainty>7e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>2.41e+18</value>
              <uncertainty>6e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>7.6e+17</value>
              <uncertainty>2.6e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>-1.04e+18</value>
              <uncertainty>2.6e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>4.36e+18</value>
              <uncertainty>5e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>7.8</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C111876A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C111876A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C111876B/event">
      <preferredOriginID>smi:local/ndk/C111876B/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C111876B/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C111876B/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>IRIAN JAYA REGION, INDONESIA</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C111876B</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C111876B/origin#reforigin">
        <time>
          <value>1976-11-18T05:43:41.300000Z</value>
        </time>
        <latitude>
          <value>-4.17</value>
        </latitude>
        <longitude>
          <value>135.14</value>
        </longitude>
        <depth>
          <value>33000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C111876B/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C111876B/origin#cmtorigin">
        <time>
          <value>1976-11-18T05:43:45.700000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>-4.17</value>
          <uncertainty>0.02</uncertainty>
        </latitude>
        <longitude>
          <value>134.93</value>
          <uncertainty>0.02</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C111876B/magnitude#moment_mag">
        <mag>
          <value>6.47</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C111876B/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C111876B/magnitude#mb">
        <mag>
          <value>5.8</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C111876B/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C111876B/magnitude#MS">
        <mag>
          <value>6.3</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C111876B/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C111876B/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>259.0</value>
            </strike>
            <dip>
              <value>19.0</value>
            </dip>
            <rake>
              <value>12.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>158.0</value>
            </strike>
            <dip>
              <value>86.0</value>
            </dip>
            <rake>
              <value>109.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>87.0</value>
            </azimuth>
            <plunge>
              <value>46.0</value>
            </plunge>
            <length>
              <value>6.38e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>231.0</value>
            </azimuth>
            <plunge>
              <value>38.0</value>
            </plunge>
            <length>
              <value>-6.55e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>336.0</value>
            </azimuth>
            <plunge>
              <value>19.0</value>
            </plunge>
            <length>
              <value>1.7e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C111876B/momenttensor">
          <derivedOriginID>smi:local/ndk/C111876B/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>12</stationCount>
            <componentCount>32</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>15</stationCount>
            <componentCount>29</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>6.47e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>7.9e+17</value>
              <uncertainty>4e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>-1.48e+18</value>
              <uncertainty>4e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>6.9e+17</value>
              <uncertainty>4e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>2.24e+18</value>
              <uncertainty>1.7e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>-5.63e+18</value>
              <uncertainty>1.6e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>1.87e+18</value>
              <uncertainty>4e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>8.4</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C111876B/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C111876B/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/B112276A/event">
      <preferredOriginID>smi:local/ndk/B112276A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/B112276A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/B112276A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>MINDANAO, PHILIPPINES</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>B112276A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/B112276A/origin#reforigin">
        <time>
          <value>1976-11-22T04:22:25.300000Z</value>
        </time>
        <latitude>
          <value>7.03</value>
        </latitude>
        <longitude>
          <value>123.58</value>
        </longitude>
        <depth>
          <value>60000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/B112276A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/B112276A/origin#cmtorigin">
        <time>
          <value>1976-11-22T04:22:20.700000Z</value>
          <uncertainty>1.7</uncertainty>
        </time>
        <latitude>
          <value>7.03</value>
          <uncertainty>0.0</uncertainty>
        </latitude>
        <longitude>
          <value>123.58</value>
          <uncertainty>0.0</uncertainty>
        </longitude>
        <depth>
          <value>60000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/B112276A/magnitude#moment_mag">
        <mag>
          <value>5.12</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/B112276A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/B112276A/magnitude#mb">
        <mag>
          <value>6.0</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/B112276A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/B112276A/magnitude#MS">
        <mag>
          <value>0.0</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/B112276A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/B112276A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>136.0</value>
            </strike>
            <dip>
              <value>59.0</value>
            </dip>
            <rake>
              <value>14.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>38.0</value>
            </strike>
            <dip>
              <value>78.0</value>
            </dip>
            <rake>
              <value>148.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>353.0</value>
            </azimuth>
            <plunge>
              <value>31.0</value>
            </plunge>
            <length>
              <value>5.38e+16</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>91.0</value>
            </azimuth>
            <plunge>
              <value>13.0</value>
            </plunge>
            <length>
              <value>-6.76e+16</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>200.0</value>
            </azimuth>
            <plunge>
              <value>56.0</value>
            </plunge>
            <length>
              <value>1.38e+16</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/B112276A/momenttensor">
          <derivedOriginID>smi:local/ndk/B112276A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>6</stationCount>
            <componentCount>7</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>6.07e+16</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>2.03e+16</value>
              <uncertainty>6.5e+15</uncertainty>
            </Mrr>
            <Mtt>
              <value>4.26e+16</value>
              <uncertainty>1e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>-6.29e+16</value>
              <uncertainty>1.27e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>1.78e+16</value>
              <uncertainty>8.9e+15</uncertainty>
            </Mrt>
            <Mrp>
              <value>2.02e+16</value>
              <uncertainty>1.03e+16</uncertainty>
            </Mrp>
            <Mtp>
              <value>2.2e+15</value>
              <uncertainty>9e+15</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>6.0</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/B112276A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/B112276A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C112276B/event">
      <preferredOriginID>smi:local/ndk/C112276B/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C112276B/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C112276B/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>MID-INDIAN RIDGE</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C112276B</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C112276B/origin#reforigin">
        <time>
          <value>1976-11-22T04:46:26.000000Z</value>
        </time>
        <latitude>
          <value>-38.52</value>
        </latitude>
        <longitude>
          <value>78.57</value>
        </longitude>
        <depth>
          <value>33000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C112276B/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C112276B/origin#cmtorigin">
        <time>
          <value>1976-11-22T04:46:26.700000Z</value>
          <uncertainty>0.3</uncertainty>
        </time>
        <latitude>
          <value>-38.4</value>
          <uncertainty>0.04</uncertainty>
        </latitude>
        <longitude>
          <value>78.12</value>
          <uncertainty>0.03</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C112276B/magnitude#moment_mag">
        <mag>
          <value>5.8</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C112276B/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C112276B/magnitude#mb">
        <mag>
          <value>5.5</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C112276B/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C112276B/magnitude#MS">
        <mag>
          <value>6.0</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C112276B/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C112276B/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>309.0</value>
            </strike>
            <dip>
              <value>90.0</value>
            </dip>
            <rake>
              <value>-180.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>39.0</value>
            </strike>
            <dip>
              <value>90.0</value>
            </dip>
            <rake>
              <value>0.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>264.0</value>
            </azimuth>
            <plunge>
              <value>0.0</value>
            </plunge>
            <length>
              <value>7.38e+17</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>174.0</value>
            </azimuth>
            <plunge>
              <value>0.0</value>
            </plunge>
            <length>
              <value>-5.15e+17</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>180.0</value>
            </azimuth>
            <plunge>
              <value>90.0</value>
            </plunge>
            <length>
              <value>-2.24e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C112276B/momenttensor">
          <derivedOriginID>smi:local/ndk/C112276B/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>13</stationCount>
            <componentCount>32</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>13</stationCount>
            <componentCount>24</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>6.26e+17</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>-2.23e+17</value>
              <uncertainty>1.7e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>-5e+17</value>
              <uncertainty>1.9e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>7.24e+17</value>
              <uncertainty>1.3e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>0.0</value>
              <uncertainty>0.0</uncertainty>
            </Mrt>
            <Mrp>
              <value>0.0</value>
              <uncertainty>0.0</uncertainty>
            </Mrp>
            <Mtp>
              <value>-1.33e+17</value>
              <uncertainty>1.7e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>4.0</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C112276B/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C112276B/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C112476A/event">
      <preferredOriginID>smi:local/ndk/C112476A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C112476A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C112476A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>TURKEY</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C112476A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C112476A/origin#reforigin">
        <time>
          <value>1976-11-24T12:22:18.800000Z</value>
        </time>
        <latitude>
          <value>39.12</value>
        </latitude>
        <longitude>
          <value>44.03</value>
        </longitude>
        <depth>
          <value>36000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C112476A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C112476A/origin#cmtorigin">
        <time>
          <value>1976-11-24T12:22:25.300000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>38.88</value>
          <uncertainty>0.02</uncertainty>
        </latitude>
        <longitude>
          <value>43.96</value>
          <uncertainty>0.02</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C112476A/magnitude#moment_mag">
        <mag>
          <value>7.01</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C112476A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C112476A/magnitude#mb">
        <mag>
          <value>6.1</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C112476A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C112476A/magnitude#MS">
        <mag>
          <value>7.3</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C112476A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C112476A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>203.0</value>
            </strike>
            <dip>
              <value>77.0</value>
            </dip>
            <rake>
              <value>9.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>110.0</value>
            </strike>
            <dip>
              <value>81.0</value>
            </dip>
            <rake>
              <value>167.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>66.0</value>
            </azimuth>
            <plunge>
              <value>15.0</value>
            </plunge>
            <length>
              <value>4.18e+19</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>157.0</value>
            </azimuth>
            <plunge>
              <value>2.0</value>
            </plunge>
            <length>
              <value>-4.14e+19</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>255.0</value>
            </azimuth>
            <plunge>
              <value>74.0</value>
            </plunge>
            <length>
              <value>-5e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C112476A/momenttensor">
          <derivedOriginID>smi:local/ndk/C112476A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>10</stationCount>
            <componentCount>21</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>14</stationCount>
            <componentCount>36</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>4.16e+19</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>2.5e+18</value>
              <uncertainty>4e+17</uncertainty>
            </Mrr>
            <Mtt>
              <value>-2.85e+19</value>
              <uncertainty>4e+17</uncertainty>
            </Mtt>
            <Mpp>
              <value>2.61e+19</value>
              <uncertainty>3e+17</uncertainty>
            </Mpp>
            <Mrt>
              <value>6e+18</value>
              <uncertainty>2.1e+18</uncertainty>
            </Mrt>
            <Mrp>
              <value>-9.3e+18</value>
              <uncertainty>2e+18</uncertainty>
            </Mrp>
            <Mtp>
              <value>-2.93e+19</value>
              <uncertainty>3e+17</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>16.0</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C112476A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C112476A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C112576A/event">
      <preferredOriginID>smi:local/ndk/C112576A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C112576A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C112576A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>FIJI ISLANDS REGION</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C112576A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C112576A/origin#reforigin">
        <time>
          <value>1976-11-25T14:06:35.400000Z</value>
        </time>
        <latitude>
          <value>-19.5</value>
        </latitude>
        <longitude>
          <value>-177.71</value>
        </longitude>
        <depth>
          <value>442000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C112576A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C112576A/origin#cmtorigin">
        <time>
          <value>1976-11-25T14:06:42.200000Z</value>
          <uncertainty>0.1</uncertainty>
        </time>
        <latitude>
          <value>-19.46</value>
          <uncertainty>0.02</uncertainty>
        </latitude>
        <longitude>
          <value>-177.61</value>
          <uncertainty>0.01</uncertainty>
        </longitude>
        <depth>
          <value>452800.0</value>
          <uncertainty>1000.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C112576A/magnitude#moment_mag">
        <mag>
          <value>6.48</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C112576A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C112576A/magnitude#mb">
        <mag>
          <value>6.0</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C112576A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C112576A/magnitude#MS">
        <mag>
          <value>0.0</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C112576A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C112576A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>139.0</value>
            </strike>
            <dip>
              <value>46.0</value>
            </dip>
            <rake>
              <value>-138.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>17.0</value>
            </strike>
            <dip>
              <value>62.0</value>
            </dip>
            <rake>
              <value>-53.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>81.0</value>
            </azimuth>
            <plunge>
              <value>9.0</value>
            </plunge>
            <length>
              <value>6.05e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>337.0</value>
            </azimuth>
            <plunge>
              <value>56.0</value>
            </plunge>
            <length>
              <value>-7.09e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>177.0</value>
            </azimuth>
            <plunge>
              <value>32.0</value>
            </plunge>
            <length>
              <value>1.03e+18</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C112576A/momenttensor">
          <derivedOriginID>smi:local/ndk/C112576A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>12</stationCount>
            <componentCount>33</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>16</stationCount>
            <componentCount>35</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>6.57e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>-4.43e+18</value>
              <uncertainty>6e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>-9.9e+17</value>
              <uncertainty>8e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>5.43e+18</value>
              <uncertainty>7e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>-3.34e+18</value>
              <uncertainty>7e+16</uncertainty>
            </Mrt>
            <Mrp>
              <value>-2.25e+18</value>
              <uncertainty>6e+16</uncertainty>
            </Mrp>
            <Mtp>
              <value>-1.65e+18</value>
              <uncertainty>8e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>8.4</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C112576A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C112576A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C112676A/event">
      <preferredOriginID>smi:local/ndk/C112676A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C112676A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C112676A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>OFF COAST OF NORTHERN CALIFORNIA</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C112676A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C112676A/origin#reforigin">
        <time>
          <value>1976-11-26T11:19:25.200000Z</value>
        </time>
        <latitude>
          <value>41.29</value>
        </latitude>
        <longitude>
          <value>-125.71</value>
        </longitude>
        <depth>
          <value>15000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C112676A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C112676A/origin#cmtorigin">
        <time>
          <value>1976-11-26T11:19:31.800000Z</value>
          <uncertainty>0.1</uncertainty>
        </time>
        <latitude>
          <value>41.46</value>
          <uncertainty>0.01</uncertainty>
        </latitude>
        <longitude>
          <value>-126.22</value>
          <uncertainty>0.01</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C112676A/magnitude#moment_mag">
        <mag>
          <value>6.69</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C112676A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C112676A/magnitude#mb">
        <mag>
          <value>6.0</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C112676A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C112676A/magnitude#MS">
        <mag>
          <value>6.8</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C112676A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C112676A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>54.0</value>
            </strike>
            <dip>
              <value>85.0</value>
            </dip>
            <rake>
              <value>5.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>324.0</value>
            </strike>
            <dip>
              <value>85.0</value>
            </dip>
            <rake>
              <value>175.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>279.0</value>
            </azimuth>
            <plunge>
              <value>7.0</value>
            </plunge>
            <length>
              <value>1.34e+19</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>9.0</value>
            </azimuth>
            <plunge>
              <value>0.0</value>
            </plunge>
            <length>
              <value>-1.38e+19</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>100.0</value>
            </azimuth>
            <plunge>
              <value>83.0</value>
            </plunge>
            <length>
              <value>4e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C112676A/momenttensor">
          <derivedOriginID>smi:local/ndk/C112676A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>11</stationCount>
            <componentCount>31</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>15</stationCount>
            <componentCount>41</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>1.36e+19</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>6e+17</value>
              <uncertainty>1e+17</uncertainty>
            </Mrr>
            <Mtt>
              <value>-1.31e+19</value>
              <uncertainty>1e+17</uncertainty>
            </Mtt>
            <Mpp>
              <value>1.25e+19</value>
              <uncertainty>1e+17</uncertainty>
            </Mpp>
            <Mrt>
              <value>2e+17</value>
              <uncertainty>5e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>1.6e+18</value>
              <uncertainty>5e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>4.2e+18</value>
              <uncertainty>1e+17</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>10.8</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C112676A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C112676A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C112776A/event">
      <preferredOriginID>smi:local/ndk/C112776A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C112776A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C112776A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>HINDU KUSH REGION, AFGHANISTAN</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C112776A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C112776A/origin#reforigin">
        <time>
          <value>1976-11-27T21:42:12.200000Z</value>
        </time>
        <latitude>
          <value>36.51</value>
        </latitude>
        <longitude>
          <value>71.04</value>
        </longitude>
        <depth>
          <value>190000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C112776A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C112776A/origin#cmtorigin">
        <time>
          <value>1976-11-27T21:42:14.600000Z</value>
          <uncertainty>0.3</uncertainty>
        </time>
        <latitude>
          <value>36.33</value>
          <uncertainty>0.03</uncertainty>
        </latitude>
        <longitude>
          <value>70.64</value>
          <uncertainty>0.03</uncertainty>
        </longitude>
        <depth>
          <value>196200.0</value>
          <uncertainty>1300.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C112776A/magnitude#moment_mag">
        <mag>
          <value>5.89</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C112776A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C112776A/magnitude#mb">
        <mag>
          <value>6.1</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C112776A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C112776A/magnitude#MS">
        <mag>
          <value>0.0</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C112776A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C112776A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>294.0</value>
            </strike>
            <dip>
              <value>41.0</value>
            </dip>
            <rake>
              <value>139.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>57.0</value>
            </strike>
            <dip>
              <value>65.0</value>
            </dip>
            <rake>
              <value>57.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>282.0</value>
            </azimuth>
            <plunge>
              <value>57.0</value>
            </plunge>
            <length>
              <value>8.75e+17</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>170.0</value>
            </azimuth>
            <plunge>
              <value>14.0</value>
            </plunge>
            <length>
              <value>-8.43e+17</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>73.0</value>
            </azimuth>
            <plunge>
              <value>30.0</value>
            </plunge>
            <length>
              <value>-3.2e+16</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C112776A/momenttensor">
          <derivedOriginID>smi:local/ndk/C112776A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>12</stationCount>
            <componentCount>29</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>13</stationCount>
            <componentCount>24</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>8.59e+17</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>5.57e+17</value>
              <uncertainty>1.6e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>-7.64e+17</value>
              <uncertainty>1.9e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>2.08e+17</value>
              <uncertainty>1.8e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>2.71e+17</value>
              <uncertainty>1.4e+16</uncertainty>
            </Mrt>
            <Mrp>
              <value>4.37e+17</value>
              <uncertainty>1.3e+16</uncertainty>
            </Mrp>
            <Mtp>
              <value>-6.9e+16</value>
              <uncertainty>2.3e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>4.4</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C112776A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C112776A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/M113076A/event">
      <preferredOriginID>smi:local/ndk/M113076A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/M113076A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/M113076A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>CHILE-BOLIVIA BORDER REGION</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>M113076A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/M113076A/origin#reforigin">
        <time>
          <value>1976-11-30T00:40:57.800000Z</value>
        </time>
        <latitude>
          <value>-20.52</value>
        </latitude>
        <longitude>
          <value>-68.92</value>
        </longitude>
        <depth>
          <value>82000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/M113076A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/M113076A/origin#cmtorigin">
        <time>
          <value>1976-11-30T00:41:13.300000Z</value>
          <uncertainty>0.4</uncertainty>
        </time>
        <latitude>
          <value>-20.54</value>
          <uncertainty>0.03</uncertainty>
        </latitude>
        <longitude>
          <value>-68.51</value>
          <uncertainty>0.04</uncertainty>
        </longitude>
        <depth>
          <value>133700.0</value>
          <uncertainty>3000.0</uncertainty>
        </depth>
        <depthType>from moment tensor inversion</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/M113076A/magnitude#moment_mag">
        <mag>
          <value>7.54</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/M113076A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/M113076A/magnitude#mb">
        <mag>
          <value>6.5</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/M113076A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/M113076A/magnitude#MS">
        <mag>
          <value>0.0</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/M113076A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/M113076A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>181.0</value>
            </strike>
            <dip>
              <value>27.0</value>
            </dip>
            <rake>
              <value>-73.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>342.0</value>
            </strike>
            <dip>
              <value>64.0</value>
            </dip>
            <rake>
              <value>-99.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>78.0</value>
            </azimuth>
            <plunge>
              <value>18.0</value>
            </plunge>
            <length>
              <value>2.72e+20</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>234.0</value>
            </azimuth>
            <plunge>
              <value>70.0</value>
            </plunge>
            <length>
              <value>-2.33e+20</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>346.0</value>
            </azimuth>
            <plunge>
              <value>8.0</value>
            </plunge>
            <length>
              <value>-3.9e+19</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/M113076A/momenttensor">
          <derivedOriginID>smi:local/ndk/M113076A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>12</stationCount>
            <componentCount>23</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>2.53e+20</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>-1.79e+20</value>
              <uncertainty>6e+18</uncertainty>
            </Mrr>
            <Mtt>
              <value>-3.5e+19</value>
              <uncertainty>5e+18</uncertainty>
            </Mtt>
            <Mpp>
              <value>2.14e+20</value>
              <uncertainty>5e+18</uncertainty>
            </Mpp>
            <Mrt>
              <value>5.5e+19</value>
              <uncertainty>3e+18</uncertainty>
            </Mrt>
            <Mrp>
              <value>-1.42e+20</value>
              <uncertainty>5e+18</uncertainty>
            </Mrp>
            <Mtp>
              <value>-4.4e+19</value>
              <uncertainty>4e+18</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>30.2</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/M113076A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/M113076A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C121476A/event">
      <preferredOriginID>smi:local/ndk/C121476A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C121476A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C121476A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>RYUKYU ISLANDS, JAPAN</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C121476A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C121476A/origin#reforigin">
        <time>
          <value>1976-12-14T16:06:44.400000Z</value>
        </time>
        <latitude>
          <value>28.29</value>
        </latitude>
        <longitude>
          <value>130.7</value>
        </longitude>
        <depth>
          <value>41000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C121476A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C121476A/origin#cmtorigin">
        <time>
          <value>1976-12-14T16:06:49.200000Z</value>
          <uncertainty>0.1</uncertainty>
        </time>
        <latitude>
          <value>28.12</value>
          <uncertainty>0.01</uncertainty>
        </latitude>
        <longitude>
          <value>130.64</value>
          <uncertainty>0.02</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C121476A/magnitude#moment_mag">
        <mag>
          <value>6.38</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C121476A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C121476A/magnitude#mb">
        <mag>
          <value>6.3</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C121476A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C121476A/magnitude#MS">
        <mag>
          <value>6.2</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C121476A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C121476A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>230.0</value>
            </strike>
            <dip>
              <value>33.0</value>
            </dip>
            <rake>
              <value>-114.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>78.0</value>
            </strike>
            <dip>
              <value>61.0</value>
            </dip>
            <rake>
              <value>-75.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>157.0</value>
            </azimuth>
            <plunge>
              <value>15.0</value>
            </plunge>
            <length>
              <value>4.2e+18</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>20.0</value>
            </azimuth>
            <plunge>
              <value>70.0</value>
            </plunge>
            <length>
              <value>-5.03e+18</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>251.0</value>
            </azimuth>
            <plunge>
              <value>13.0</value>
            </plunge>
            <length>
              <value>8.3e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C121476A/momenttensor">
          <derivedOriginID>smi:local/ndk/C121476A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>11</stationCount>
            <componentCount>30</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>16</stationCount>
            <componentCount>38</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>4.62e+18</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>-4.16e+18</value>
              <uncertainty>4e+16</uncertainty>
            </Mrr>
            <Mtt>
              <value>2.94e+18</value>
              <uncertainty>4e+16</uncertainty>
            </Mtt>
            <Mpp>
              <value>1.23e+18</value>
              <uncertainty>4e+16</uncertainty>
            </Mpp>
            <Mrt>
              <value>-2.49e+18</value>
              <uncertainty>2.1e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>3.3e+17</value>
              <uncertainty>1.9e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>1.35e+18</value>
              <uncertainty>3e+16</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>7.6</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C121476A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C121476A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
    <event publicID="smi:local/ndk/C122076A/event">
      <preferredOriginID>smi:local/ndk/C122076A/origin#cmtorigin</preferredOriginID>
      <preferredMagnitudeID>smi:local/ndk/C122076A/magnitude#moment_mag</preferredMagnitudeID>
      <preferredFocalMechanismID>smi:local/ndk/C122076A/focal_mechanism</preferredFocalMechanismID>
      <type>earthquake</type>
      <typeCertainty>known</typeCertainty>
      <description>
        <text>VANCOUVER ISLAND, CANADA REGION</text>
        <type>Flinn-Engdahl region</type>
      </description>
      <description>
        <text>C122076A</text>
        <type>earthquake name</type>
      </description>
      <origin publicID="smi:local/ndk/C122076A/origin#reforigin">
        <time>
          <value>1976-12-20T20:33:07.800000Z</value>
        </time>
        <latitude>
          <value>48.8</value>
        </latitude>
        <longitude>
          <value>-129.29</value>
        </longitude>
        <depth>
          <value>10000.0</value>
        </depth>
        <type>hypocenter</type>
        <comment id="smi:local/ndk/C122076A/comment#ref_origin">
          <text>Hypocenter catalog: MLI</text>
        </comment>
      </origin>
      <origin publicID="smi:local/ndk/C122076A/origin#cmtorigin">
        <time>
          <value>1976-12-20T20:33:17.300000Z</value>
          <uncertainty>0.2</uncertainty>
        </time>
        <latitude>
          <value>48.93</value>
          <uncertainty>0.01</uncertainty>
        </latitude>
        <longitude>
          <value>-129.77</value>
          <uncertainty>0.02</uncertainty>
        </longitude>
        <depth>
          <value>15000.0</value>
          <uncertainty>0.0</uncertainty>
        </depth>
        <depthType>from location</depthType>
        <timeFixed>false</timeFixed>
        <epicenterFixed>false</epicenterFixed>
        <type>centroid</type>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </origin>
      <magnitude publicID="smi:local/ndk/C122076A/magnitude#moment_mag">
        <mag>
          <value>6.65</value>
        </mag>
        <type>Mwc</type>
        <originID>smi:local/ndk/C122076A/origin#cmtorigin</originID>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C122076A/magnitude#mb">
        <mag>
          <value>5.9</value>
        </mag>
        <type>mb</type>
        <comment id="smi:local/ndk/C122076A/comment#mb_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'mb'.</text>
        </comment>
      </magnitude>
      <magnitude publicID="smi:local/ndk/C122076A/magnitude#MS">
        <mag>
          <value>6.7</value>
        </mag>
        <type>MS</type>
        <comment id="smi:local/ndk/C122076A/comment#MS_magnitude">
          <text>Reported magnitude in NDK file. Most likely 'MS'.</text>
        </comment>
      </magnitude>
      <focalMechanism publicID="smi:local/ndk/C122076A/focal_mechanism">
        <nodalPlanes>
          <nodalPlane1>
            <strike>
              <value>37.0</value>
            </strike>
            <dip>
              <value>89.0</value>
            </dip>
            <rake>
              <value>-1.0</value>
            </rake>
          </nodalPlane1>
          <nodalPlane2>
            <strike>
              <value>127.0</value>
            </strike>
            <dip>
              <value>89.0</value>
            </dip>
            <rake>
              <value>-179.0</value>
            </rake>
          </nodalPlane2>
        </nodalPlanes>
        <principalAxes>
          <tAxis>
            <azimuth>
              <value>262.0</value>
            </azimuth>
            <plunge>
              <value>0.0</value>
            </plunge>
            <length>
              <value>1.23e+19</value>
            </length>
          </tAxis>
          <pAxis>
            <azimuth>
              <value>352.0</value>
            </azimuth>
            <plunge>
              <value>1.0</value>
            </plunge>
            <length>
              <value>-1.17e+19</value>
            </length>
          </pAxis>
          <nAxis>
            <azimuth>
              <value>158.0</value>
            </azimuth>
            <plunge>
              <value>89.0</value>
            </plunge>
            <length>
              <value>-6e+17</value>
            </length>
          </nAxis>
        </principalAxes>
        <momentTensor publicID="smi:local/ndk/C122076A/momenttensor">
          <derivedOriginID>smi:local/ndk/C122076A/origin#cmtorigin</derivedOriginID>
          <dataUsed>
            <waveType>body waves</waveType>
            <stationCount>9</stationCount>
            <componentCount>22</componentCount>
            <shortestPeriod>45.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>surface waves</waveType>
            <stationCount>0</stationCount>
            <componentCount>0</componentCount>
            <shortestPeriod>0.0</shortestPeriod>
          </dataUsed>
          <dataUsed>
            <waveType>mantle waves</waveType>
            <stationCount>15</stationCount>
            <componentCount>35</componentCount>
            <shortestPeriod>135.0</shortestPeriod>
          </dataUsed>
          <scalarMoment>
            <value>1.2e+19</value>
          </scalarMoment>
          <tensor>
            <Mrr>
              <value>-6e+17</value>
              <uncertainty>1e+17</uncertainty>
            </Mrr>
            <Mtt>
              <value>-1.12e+19</value>
              <uncertainty>1e+17</uncertainty>
            </Mtt>
            <Mpp>
              <value>1.18e+19</value>
              <uncertainty>1e+17</uncertainty>
            </Mpp>
            <Mrt>
              <value>-2e+17</value>
              <uncertainty>5e+17</uncertainty>
            </Mrt>
            <Mrp>
              <value>0.0</value>
              <uncertainty>6e+17</uncertainty>
            </Mrp>
            <Mtp>
              <value>-3.5e+18</value>
              <uncertainty>1e+17</uncertainty>
            </Mtp>
          </tensor>
          <sourceTimeFunction>
            <type>box car</type>
            <duration>10.4</duration>
          </sourceTimeFunction>
          <inversionType>zero trace</inversionType>
          <creationInfo>
            <agencyID>GCMT</agencyID>
            <version>V10</version>
          </creationInfo>
        </momentTensor>
        <comment id="smi:local/ndk/C122076A/comment#cmt_type">
          <text>CMT Analysis Type: Unknown</text>
        </comment>
        <comment id="smi:local/ndk/C122076A/comment#cmt_timestamp">
          <text>CMT Timestamp: O-00000000000000</text>
        </comment>
        <creationInfo>
          <agencyID>GCMT</agencyID>
          <version>V10</version>
        </creationInfo>
      </focalMechanism>
    </event>
  </eventParameters>
</q:quakeml>
