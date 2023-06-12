# queries sql usadas no basip

vlan_pppoe = '''
SELECT pat.Hostname_Pat as Hostname,
       ocupvlan.Num_VLAN_OcupVLAN as VLAN,
       modequip.Modelo_ModEquip as Modelo
FROM ocupvlan
     LEFT JOIN gigametro
          ON (ocupvlan.Cod_GigaMetro_OcupVLAN = gigametro.Cod_GigaMetro)
     LEFT JOIN servicoip
          ON (ocupvlan.Cod_ServicoIP_OcupVLAN = servicoip.Cod_ServicoIP)
     LEFT JOIN conexao
          ON (servicoip.Cod_ServicoIP = conexao.Cod_ServicoIP_Conexao)
     LEFT JOIN patngenerico
          ON (conexao.Cod_PatNG_Conexao = patngenerico.Cod_PatNG)
     LEFT JOIN pat
          ON (patngenerico.Num_Pat_PatNG = pat.Num_Pat)
     LEFT JOIN modequip
          ON (pat.Cod_ModEquip_Pat = modequip.Cod_ModEquip)
     LEFT JOIN fabequip
          ON (modequip.Cod_FabEquip_ModEquip = fabequip.Cod_FabEquip)
WHERE gigametro.Desc_GigaMetro LIKE "Agregacao"
      AND pat.Hostname_Pat LIKE "{olt}"
      AND fabequip.Desc_FabEquip LIKE "ZHONE"
'''


vlan_fxs = '''
SELECT DISTINCT pat.Hostname_Pat as Hostname,
       ocupvlan.Num_VLAN_OcupVLAN as VLAN,
       modequip.Modelo_ModEquip as Modelo,
       vpn.Nome_VPN as VPN,
       servicoip.CodComercial_ServicoIP as Contract
FROM ocupvlan
     LEFT JOIN servicoip
          ON (ocupvlan.Cod_ServicoIP_OcupVLAN = servicoip.Cod_ServicoIP)
     LEFT JOIN conexao
          ON (servicoip.Cod_ServicoIP = conexao.Cod_ServicoIP_Conexao)
     LEFT JOIN ocupvpn
          ON (servicoip.Cod_ServicoIP = ocupvpn.Cod_ServicoIP_OcupVPN)
     LEFT JOIN vpn
           ON (ocupvpn.Numero_VPN_OcupVPN = vpn.Numero_VPN)
     LEFT JOIN patngenerico
          ON (conexao.Cod_PatNG_Conexao = patngenerico.Cod_PatNG)
     LEFT JOIN pat
          ON (patngenerico.Num_Pat_PatNG = pat.Num_Pat)
     LEFT JOIN modequip
          ON (pat.Cod_ModEquip_Pat = modequip.Cod_ModEquip)
     LEFT JOIN fabequip
          ON (modequip.Cod_FabEquip_ModEquip = fabequip.Cod_FabEquip)
WHERE pat.Hostname_Pat LIKE "{olt}"
      AND fabequip.Desc_FabEquip LIKE "ZHONE"
      AND vpn.Nome_VPN LIKE "vpn00273"
'''


modelo_fabricante = '''
SELECT pat.Hostname_Pat, modequip.Modelo_ModEquip, fabequip.Desc_FabEquip
FROM pat
     LEFT JOIN modequip
          ON (pat.Cod_ModEquip_Pat = modequip.Cod_ModEquip)
     LEFT JOIN fabequip
          ON (modequip.Cod_FabEquip_ModEquip = fabequip.Cod_FabEquip)
WHERE pat.Hostname_Pat LIKE "{hostname}"
'''


connections_per_contract = '''
SELECT servicoip.NUM_SEQ_ACT,
       servicoip.CodComercial_ServicoIP,
       sitservicoip.Desc_SitServicoIP,
       produtoip.Sigla_ProdutoIP,
       banda.Bps_Banda,
       fabequip.Desc_FabEquip,
       modequip.Modelo_ModEquip,
       pat.Hostname_Pat,
       patngenerico.Interface_PatNG,
       conexao.Cod_Sit_Uso_Conexao,
       servip_tiposervagreg.Obs_TipoServAgreg
FROM servicoip
     LEFT JOIN produtoip
          ON (servicoip.CodCom_ProdutoIP_ServicoIP = produtoip.CodCom_ProdutoIP)
     LEFT JOIN sitservicoip
          ON (servicoip.Cod_SitServicoIP_ServicoIP = sitservicoip.Cod_SitServicoIP)
     LEFT JOIN banda
          ON (servicoip.BandaContratada_ServicoIP = banda.Cod_Banda)
     LEFT JOIN conexao
          ON (servicoip.Cod_ServicoIP = conexao.Cod_ServicoIP_Conexao)
     LEFT JOIN patngenerico
          ON (conexao.Cod_PatNG_Conexao = patngenerico.Cod_PatNG)
     LEFT JOIN pat
          ON (patngenerico.Num_Pat_PatNG = pat.Num_Pat)
     LEFT JOIN modequip
          ON (pat.Cod_ModEquip_Pat = modequip.Cod_ModEquip)
     LEFT JOIN fabequip
          ON (modequip.Cod_FabEquip_ModEquip = fabequip.Cod_FabEquip)
     LEFT JOIN servip_tiposervagreg
          ON (servicoip.Cod_ServicoIP = servip_tiposervagreg.Cod_ServicoIP)
     LEFT JOIN tiposervicoagregado
          ON (servip_tiposervagreg.Cod_TipoServAgreg = tiposervicoagregado.Cod_TipoServAgreg)
WHERE servicoip.NUM_SEQ_ACT LIKE "{contract}"
     AND (tiposervicoagregado.Descr_TipoServAgreg LIKE "PASSWORD VAREJO"
          OR tiposervicoagregado.Descr_TipoServAgreg IS NULL)
ORDER BY conexao.Seq_Diagr_Conexao
'''

connections_contract = '''
SELECT servicoip.NUM_SEQ_ACT,
       servicoip.CodComercial_ServicoIP,
       sitservicoip.Desc_SitServicoIP,
       produtoip.Sigla_ProdutoIP,
       banda.Bps_Banda,
       fabequip.Desc_FabEquip,
       modequip.Modelo_ModEquip,
       pat.Hostname_Pat,
       patngenerico.Interface_PatNG,
       conexao.Cod_Sit_Uso_Conexao
FROM servicoip
     LEFT JOIN produtoip
          ON (servicoip.CodCom_ProdutoIP_ServicoIP = produtoip.CodCom_ProdutoIP)
     LEFT JOIN sitservicoip
          ON (servicoip.Cod_SitServicoIP_ServicoIP = sitservicoip.Cod_SitServicoIP)
     LEFT JOIN banda
          ON (servicoip.BandaContratada_ServicoIP = banda.Cod_Banda)
     LEFT JOIN conexao
          ON (servicoip.Cod_ServicoIP = conexao.Cod_ServicoIP_Conexao)
     LEFT JOIN patngenerico
          ON (conexao.Cod_PatNG_Conexao = patngenerico.Cod_PatNG)
     LEFT JOIN pat
          ON (patngenerico.Num_Pat_PatNG = pat.Num_Pat)
     LEFT JOIN modequip
          ON (pat.Cod_ModEquip_Pat = modequip.Cod_ModEquip)
     LEFT JOIN fabequip
          ON (modequip.Cod_FabEquip_ModEquip = fabequip.Cod_FabEquip)
WHERE servicoip.NUM_SEQ_ACT LIKE "{contract}"
ORDER BY conexao.Seq_Diagr_Conexao
'''

regid_contract = '''
SELECT servicoip.NUM_SEQ_ACT,
       servip_tiposervagreg.Obs_TipoServAgreg
FROM servicoip
     LEFT JOIN servip_tiposervagreg
          ON (servicoip.Cod_ServicoIP = servip_tiposervagreg.Cod_ServicoIP)
     LEFT JOIN tiposervicoagregado
          ON (servip_tiposervagreg.Cod_TipoServAgreg = tiposervicoagregado.Cod_TipoServAgreg)
WHERE servicoip.NUM_SEQ_ACT LIKE "{contract}"
     AND (tiposervicoagregado.Descr_TipoServAgreg LIKE "PASSWORD VAREJO")
'''

contracts_per_interface = '''
SELECT pat.Hostname_Pat,
       patngenerico.Interface_PatNG,
       produtoip.Sigla_ProdutoIP,
       servicoip.NUM_SEQ_ACT,
       servip_tiposervagreg.Obs_TipoServAgreg
FROM servicoip
     LEFT JOIN produtoip
          ON (servicoip.CodCom_ProdutoIP_ServicoIP = produtoip.CodCom_ProdutoIP)
     LEFT JOIN conexao
          ON (servicoip.Cod_ServicoIP = conexao.Cod_ServicoIP_Conexao)
     LEFT JOIN patngenerico
          ON (conexao.Cod_PatNG_Conexao = patngenerico.Cod_PatNG)
     LEFT JOIN pat
          ON (patngenerico.Num_Pat_PatNG = pat.Num_Pat)
     LEFT JOIN servip_tiposervagreg
          ON (servicoip.Cod_ServicoIP = servip_tiposervagreg.Cod_ServicoIP)
     LEFT JOIN tiposervicoagregado
          ON (servip_tiposervagreg.Cod_TipoServAgreg = tiposervicoagregado.Cod_TipoServAgreg)
WHERE pat.Hostname_Pat LIKE "{hostname}"
      AND patngenerico.Interface_PatNG LIKE "{interface}%"
      AND (tiposervicoagregado.Descr_TipoServAgreg LIKE "PASSWORD VAREJO"
          OR tiposervicoagregado.Descr_TipoServAgreg IS NULL)
ORDER BY patngenerico.Interface_PatNG
'''


bel_per_vlan = '''
SELECT TA.VLAN, substr(min(TA.Hostname),6) AS Estacao, sum(TB.N_Circuitos) AS N_Circuitos, sum(TB.Soma_Banda_Mbps) AS Soma_Banda_Mbps
FROM
    (SELECT pat.Hostname_Pat AS Hostname, ocupvlan.Num_VLAN_OcupVLAN AS VLAN
     FROM ocupvlan
          LEFT JOIN gigametro
               ON (ocupvlan.Cod_GigaMetro_OcupVLAN = gigametro.Cod_GigaMetro)
          LEFT JOIN servicoip
               ON (ocupvlan.Cod_ServicoIP_OcupVLAN = servicoip.Cod_ServicoIP)
          LEFT JOIN conexao
               ON (servicoip.Cod_ServicoIP = conexao.Cod_ServicoIP_Conexao)
          LEFT JOIN patngenerico
               ON (conexao.Cod_PatNG_Conexao = patngenerico.Cod_PatNG)
          LEFT JOIN pat
               ON (patngenerico.Num_Pat_PatNG = pat.Num_Pat)
     WHERE gigametro.Desc_GigaMetro LIKE "Agregacao"
           AND pat.Hostname_Pat LIKE "olt%"
           AND pat.Hostname_Pat not LIKE "%lab%"
     GROUP BY pat.Hostname_Pat
     ORDER BY substring(pat.Hostname_Pat, 6, 10), substring(pat.Hostname_Pat, 4, 1)) AS TA
LEFT JOIN
    (SELECT pat.Hostname_Pat AS Hostname, count(distinct servicoip.CodComercial_ServicoIP) AS N_Circuitos, sum(banda.Bps_Banda)/1000000 AS Soma_Banda_Mbps
     FROM servicoip
          LEFT JOIN produtoip
               ON (servicoip.CodCom_ProdutoIP_ServicoIP = produtoip.CodCom_ProdutoIP)
          LEFT JOIN banda
               ON (servicoip.BandaContratada_ServicoIP = banda.Cod_Banda)
          LEFT JOIN conexao
               ON (servicoip.Cod_ServicoIP = conexao.Cod_ServicoIP_Conexao)
          LEFT JOIN patngenerico
               ON (conexao.Cod_PatNG_Conexao = patngenerico.Cod_PatNG)
          LEFT JOIN pat
               ON (patngenerico.Num_Pat_PatNG = pat.Num_Pat)
          WHERE pat.Hostname_Pat LIKE "olt%" AND produtoip.Sigla_ProdutoIP LIKE "COPEL-FIBRA"
          GROUP BY pat.Hostname_Pat) AS TB
ON TA.Hostname = TB.Hostname
GROUP BY TA.VLAN
ORDER BY N_Circuitos desc, Estacao
'''


bel_per_olt = '''
SELECT TA.hostname, TA.VLAN, TB.N_Circuitos, TB.Soma_Banda_Mbps, TA.Modelo, TA.Fabricante
FROM (SELECT pat.Hostname_Pat AS Hostname, ocupvlan.Num_VLAN_OcupVLAN AS VLAN, modequip.Modelo_ModEquip AS Modelo, fabequip.Desc_FabEquip AS Fabricante
      FROM ocupvlan
             LEFT JOIN gigametro
                ON (ocupvlan.Cod_GigaMetro_OcupVLAN = gigametro.Cod_GigaMetro)
             LEFT JOIN servicoip
                ON (ocupvlan.Cod_ServicoIP_OcupVLAN = servicoip.Cod_ServicoIP)
             LEFT JOIN conexao
                ON (servicoip.Cod_ServicoIP = conexao.Cod_ServicoIP_Conexao)
             LEFT JOIN patngenerico
                ON (conexao.Cod_PatNG_Conexao = patngenerico.Cod_PatNG)
             LEFT JOIN pat
                ON (patngenerico.Num_Pat_PatNG = pat.Num_Pat)
             LEFT JOIN modequip
                ON (pat.Cod_ModEquip_Pat = modequip.Cod_ModEquip)
             LEFT JOIN fabequip
                ON (modequip.Cod_FabEquip_ModEquip = fabequip.Cod_FabEquip)
      WHERE gigametro.Desc_GigaMetro LIKE "Agregacao"
            AND pat.Hostname_Pat LIKE "olt%"
            AND pat.Hostname_Pat NOT LIKE "%lab%"
      GROUP BY pat.Hostname_Pat
      ORDER BY substring(pat.Hostname_Pat, 6, 10), substring(pat.Hostname_Pat, 4, 1)) AS TA
LEFT JOIN (SELECT pat.Hostname_Pat AS Hostname, COUNT(distinct servicoip.CodComercial_ServicoIP) AS N_Circuitos, sum(banda.Bps_Banda)/1000000 AS Soma_Banda_Mbps
           FROM servicoip
                  LEFT JOIN produtoip
                ON (servicoip.CodCom_ProdutoIP_ServicoIP = produtoip.CodCom_ProdutoIP)
                  LEFT JOIN banda
                ON (servicoip.BandaContratada_ServicoIP = banda.Cod_Banda)
                  LEFT JOIN conexao
                ON (servicoip.Cod_ServicoIP = conexao.Cod_ServicoIP_Conexao)
                  LEFT JOIN patngenerico
                ON (conexao.Cod_PatNG_Conexao = patngenerico.Cod_PatNG)
                  LEFT JOIN pat
                ON (patngenerico.Num_Pat_PatNG = pat.Num_Pat)
           WHERE pat.Hostname_Pat LIKE "olt%"
                 AND produtoip.Sigla_ProdutoIP LIKE "COPEL-FIBRA"
           GROUP BY pat.Hostname_Pat) AS TB
ON TA.Hostname = TB.Hostname
ORDER BY TB.N_Circuitos DESC , TB.Soma_Banda_Mbps DESC
'''


xml_oss_zhone = '''
SELECT *
FROM pade_zhone_xml
'''

get_equip = '''
SELECT pat.Hostname_Pat,
       pat.Num_Pat,
       patendip.EndIP_PatEndIP,
       modequip.Modelo_ModEquip,
       fabequip.Desc_FabEquip
FROM pat
     JOIN patendip
        ON (pat.Num_Pat = patendip.Num_Pat_PatEndIP)
     JOIN modequip
        ON (pat.Cod_ModEquip_Pat = modequip.Cod_ModEquip)
     JOIN fabequip
       ON (modequip.Cod_FabEquip_ModEquip = fabequip.Cod_FabEquip)
WHERE pat.Hostname_Pat LIKE '%'
     AND modequip.Modelo_ModEquip IN {model}
ORDER BY pat.Hostname_Pat
'''

ne40_connections = '''
SELECT pat.Hostname_Pat as hostname,
       patngenerico.Interface_PatNG as interface,
       servicoip.NUM_SEQ_ACT as circuito,
       servicoip.CodComercial_ServicoIP as circuito_old,
       cliente.Nome_Cliente as cliente,
       servicoip.CNPJ_Cliente_ServicoIP,
       sitservicoip.Desc_SitServicoIP as situacao,
       produtoip.Sigla_ProdutoIP as produto,
       banda.Bps_Banda / 1000 as banda_contratada
FROM servicoip
     LEFT JOIN produtoip
          ON (servicoip.CodCom_ProdutoIP_ServicoIP = produtoip.CodCom_ProdutoIP)
     LEFT JOIN cliente
          ON (servicoip.CNPJ_Cliente_ServicoIP = cliente.CNPJ_Cliente)
     LEFT JOIN sitservicoip
          ON (servicoip.Cod_SitServicoIP_ServicoIP = sitservicoip.Cod_SitServicoIP)
     LEFT JOIN banda
          ON (servicoip.BandaContratada_ServicoIP = banda.Cod_Banda)
     LEFT JOIN conexao
          ON (servicoip.Cod_ServicoIP = conexao.Cod_ServicoIP_Conexao)
     LEFT JOIN patngenerico
          ON (conexao.Cod_PatNG_Conexao = patngenerico.Cod_PatNG)
     LEFT JOIN pat
          ON (patngenerico.Num_Pat_PatNG = pat.Num_Pat)
     LEFT JOIN modequip
          ON (pat.Cod_ModEquip_Pat = modequip.Cod_ModEquip)
WHERE modequip.Modelo_ModEquip IN ("NE40E-X3", "NE40E-X8")
ORDER BY 1, 3
'''
