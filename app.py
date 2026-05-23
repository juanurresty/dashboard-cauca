# ============================================================
# DASHBOARD STREAMLIT - BRECHA DIGITAL Y SABER PRO CAUCA
# Juan Camilo Urresty Ordóñez · Gueimar Damir Quira Rengifo
# Diplomado en Ingeniería y Ciencia de Datos - Unicomfacauca
# ============================================================
# INSTRUCCIONES PARA PUBLICAR:
# 1. Crea cuenta gratis en github.com
# 2. Crea un repositorio nuevo (ej: "dashboard-cauca")
# 3. Sube este archivo como "app.py"
# 4. Crea cuenta gratis en share.streamlit.io
# 5. Conecta tu repositorio y despliega
# 6. Obtienes un link público para compartir
# ============================================================

import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# ─── CONFIGURACIÓN DE PÁGINA ───────────────────────────────
st.set_page_config(
    page_title="Brecha Digital · Cauca 2018–2022",
    page_icon="📊",
    layout="wide"
)

# ─── ESTILOS ───────────────────────────────────────────────
st.markdown("""
<style>
  .metric-container { background:#f5f4f0; border-radius:10px; padding:16px 20px; text-align:center; }
  .metric-value     { font-size:28px; font-weight:600; margin:6px 0; }
  .metric-label     { font-size:12px; color:#888; }
  .metric-sub       { font-size:11px; color:#aaa; margin-top:3px; }
  .insight-box      { background:#EAF3DE; border-left:4px solid #3B6D11;
                      border-radius:0 8px 8px 0; padding:14px 18px;
                      font-size:13px; color:#27500A; line-height:1.7; }
  .header-title     { font-size:22px; font-weight:600; margin-bottom:4px; }
  .header-sub       { font-size:13px; color:#888; margin-bottom:24px; }
  div[data-testid="stHorizontalBlock"] { gap: 12px; }
</style>
""", unsafe_allow_html=True)

# ─── DATOS ─────────────────────────────────────────────────
COMPETENCIAS = ['Raz. Cuantitativo', 'Com. Escrita', 'Lectura Crítica', 'Inglés', 'Comp. Ciudadanas']
AZUL    = '#378ADD'
NARANJA = '#c47a00'
ROJO    = '#D85A30'
VERDE   = '#3B6D11'
REF     = 150

internet_con  = [141.7, 139.4, 144.4, 144.5, 141.2]
internet_sin  = [134.6, 137.7, 137.0, 133.1, 132.2]
compu_con     = [141.2, 139.3, 143.8, 143.3, 140.4]
compu_sin     = [133.1, 137.6, 135.9, 133.1, 131.2]
brecha_int    = [7.1, 1.7, 7.4, 11.4, 9.0]
brecha_com    = [8.1, 1.7, 7.9, 10.2, 9.2]

# ─── ENCABEZADO ────────────────────────────────────────────
st.markdown('<div class="header-title">📊 Brecha Digital y Rendimiento Académico · Cauca</div>', unsafe_allow_html=True)
st.markdown('<div class="header-sub">Pruebas Saber Pro ICFES · Período 2018–2022 · Análisis descriptivo</div>', unsafe_allow_html=True)

# ─── MÉTRICAS SUPERIORES ───────────────────────────────────
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("""<div class="metric-container">
        <div class="metric-label">Total registros</div>
        <div class="metric-value">20.329</div>
        <div class="metric-sub">57 variables disponibles</div>
    </div>""", unsafe_allow_html=True)
with col2:
    st.markdown(f"""<div class="metric-container">
        <div class="metric-label">Con internet en el hogar</div>
        <div class="metric-value" style="color:{AZUL}">73,6%</div>
        <div class="metric-sub">14.967 estudiantes</div>
    </div>""", unsafe_allow_html=True)
with col3:
    st.markdown(f"""<div class="metric-container">
        <div class="metric-label">Con computador en el hogar</div>
        <div class="metric-value" style="color:{NARANJA}">80,7%</div>
        <div class="metric-sub">16.420 estudiantes</div>
    </div>""", unsafe_allow_html=True)
with col4:
    st.markdown(f"""<div class="metric-container">
        <div class="metric-label">Media nacional de referencia</div>
        <div class="metric-value" style="color:{VERDE}">150 pts</div>
        <div class="metric-sub">Todos los módulos Saber Pro</div>
    </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ─── FUNCIONES DE GRÁFICAS ─────────────────────────────────
def fig_barras(con, sin, color_con, label_con, label_sin, ymin=122):
    fig = go.Figure()
    fig.add_trace(go.Bar(
        name=label_con, x=COMPETENCIAS, y=con,
        marker_color=color_con, marker_line_width=0,
        text=[f'{v:.1f}' for v in con], textposition='outside'
    ))
    fig.add_trace(go.Bar(
        name=label_sin, x=COMPETENCIAS, y=sin,
        marker_color=ROJO, marker_line_width=0,
        text=[f'{v:.1f}' for v in sin], textposition='outside'
    ))
    fig.add_hline(
        y=REF, line_dash='dash', line_color='gray', line_width=1.5,
        annotation_text='Media nacional: 150',
        annotation_position='top right',
        annotation_font_size=11, annotation_font_color='gray'
    )
    fig.update_layout(
        barmode='group', height=380,
        yaxis=dict(range=[ymin, 160], title='Puntaje promedio', gridcolor='rgba(0,0,0,0.07)'),
        xaxis=dict(title='Módulo'),
        plot_bgcolor='white', paper_bgcolor='white',
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
        margin=dict(t=40, b=40, l=50, r=20),
        font=dict(size=12)
    )
    return fig

def fig_brecha():
    fig = go.Figure()
    fig.add_trace(go.Bar(
        name='Brecha internet', x=COMPETENCIAS, y=brecha_int,
        marker_color=AZUL, marker_line_width=0,
        text=[f'{v:.1f}' for v in brecha_int], textposition='outside'
    ))
    fig.add_trace(go.Bar(
        name='Brecha computador', x=COMPETENCIAS, y=brecha_com,
        marker_color=NARANJA, marker_line_width=0,
        text=[f'{v:.1f}' for v in brecha_com], textposition='outside'
    ))
    fig.update_layout(
        barmode='group', height=380,
        yaxis=dict(range=[0, 15], title='Diferencia en puntos', gridcolor='rgba(0,0,0,0.07)'),
        xaxis=dict(title='Módulo'),
        plot_bgcolor='white', paper_bgcolor='white',
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
        margin=dict(t=40, b=40, l=50, r=20),
        font=dict(size=12)
    )
    return fig

def fig_donas():
    fig = make_subplots(
        rows=1, cols=2, specs=[[{'type':'domain'},{'type':'domain'}]],
        subplot_titles=['Acceso a internet en el hogar','Acceso a computador en el hogar']
    )
    fig.add_trace(go.Pie(
        labels=['Con internet (73,6%)', 'Sin internet (26,4%)'],
        values=[73.6, 26.4], hole=0.65,
        marker_colors=[AZUL, ROJO], textinfo='percent', name='Internet'
    ), row=1, col=1)
    fig.add_trace(go.Pie(
        labels=['Con computador (80,7%)', 'Sin computador (19,3%)'],
        values=[80.7, 19.3], hole=0.65,
        marker_colors=[NARANJA, ROJO], textinfo='percent', name='Computador'
    ), row=1, col=2)
    fig.update_layout(
        height=360, plot_bgcolor='white', paper_bgcolor='white',
        legend=dict(orientation='h', yanchor='bottom', y=-0.2, xanchor='center', x=0.5),
        margin=dict(t=60, b=60, l=20, r=20), font=dict(size=12)
    )
    return fig

# ─── PESTAÑAS ──────────────────────────────────────────────
tab1, tab2, tab3, tab4 = st.tabs([
    "📶  Acceso a internet",
    "💻  Acceso a computador",
    "📊  Brecha digital",
    "🍩  Distribución de acceso"
])

with tab1:
    st.plotly_chart(fig_barras(internet_con, internet_sin, AZUL, 'Con internet', 'Sin internet', 125), use_container_width=True)
    st.markdown("""<div class="insight-box">
        Los estudiantes <b>con internet</b> en el hogar obtienen puntajes superiores en los 5 módulos.
        La mayor diferencia se observa en <b>Inglés (11,4 pts)</b> y la menor en
        <b>Comunicación Escrita (1,7 pts)</b>. Ningún grupo alcanza la media nacional de 150 puntos.<br><br>
        Promedio global con internet: <b>142,25 pts</b> &nbsp;·&nbsp;
        Sin internet: <b>134,93 pts</b> &nbsp;·&nbsp; Brecha: <b>7,32 pts</b>
    </div>""", unsafe_allow_html=True)

with tab2:
    st.plotly_chart(fig_barras(compu_con, compu_sin, NARANJA, 'Con computador', 'Sin computador', 122), use_container_width=True)
    st.markdown("""<div class="insight-box">
        El patrón se repite con el computador: quienes tienen acceso superan consistentemente a quienes no.
        La mayor brecha es en <b>Inglés (10,2 pts)</b> y la menor en
        <b>Comunicación Escrita (1,7 pts)</b>.<br><br>
        Promedio global con computador: <b>141,61 pts</b> &nbsp;·&nbsp;
        Sin computador: <b>134,17 pts</b> &nbsp;·&nbsp; Brecha: <b>7,44 pts</b>
    </div>""", unsafe_allow_html=True)

with tab3:
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown(f"""<div class="metric-container">
            <div class="metric-label">Brecha promedio global — internet</div>
            <div class="metric-value" style="color:#c0392b">7,32 puntos</div>
            <div class="metric-sub">142,25 (con) vs 134,93 (sin)</div>
        </div>""", unsafe_allow_html=True)
    with col_b:
        st.markdown(f"""<div class="metric-container">
            <div class="metric-label">Brecha promedio global — computador</div>
            <div class="metric-value" style="color:#d35400">7,44 puntos</div>
            <div class="metric-sub">141,61 (con) vs 134,17 (sin)</div>
        </div>""", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.plotly_chart(fig_brecha(), use_container_width=True)
    st.markdown("""<div class="insight-box">
        <b>Inglés</b> presenta la mayor brecha en ambas dimensiones
        (11,4 pts por internet · 10,2 pts por computador), sugiriendo que el acceso tecnológico
        está más fuertemente asociado al aprendizaje de idiomas.
        <b>Comunicación Escrita</b> muestra la menor brecha (1,7 pts en ambos casos).
    </div>""", unsafe_allow_html=True)

with tab4:
    st.plotly_chart(fig_donas(), use_container_width=True)
    st.markdown("""<div class="insight-box">
        Aunque la mayoría cuenta con internet (73,6%) y computador (80,7%),
        cerca de <b>1 de cada 4 estudiantes no tiene internet</b> y casi
        <b>1 de cada 5 no tiene computador</b>. Dado que estas brechas se asocian con diferencias
        de hasta 11 puntos en los puntajes, representan una desventaja educativa significativa
        en el departamento del Cauca.
    </div>""", unsafe_allow_html=True)

# ─── PIE DE PÁGINA ─────────────────────────────────────────
st.markdown("---")
st.markdown("""
<div style="text-align:center; font-size:12px; color:#aaa; padding:8px 0;">
  Proyecto final · Diplomado en Ingeniería y Ciencia de Datos Aplicada · Unicomfacauca · 2026<br>
  Juan Camilo Urresty Ordóñez · Gueimar Damir Quira Rengifo · Datos: ICFES Saber Pro 2018–2022
</div>
""", unsafe_allow_html=True)
