#Implemented a DashBoard in Visual Studio Code 


import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.set_page_config(page_title="Advanced Dashboard", layout="wide")

COLORS = {
    "dark": "#0F172A",
    "primary": "#38BDF8",
    "blue": "#3B82F6",
    "green": "#10B981",
    "purple": "#A78BFA",
    "peach": "#FB923C",
    "pink": "#F472B6",
    "teal": "#2DD4BF",
    "grey": "#475569",
    "text": "#E2E8F0",
    "white": "#FFFFFF"
}

st.markdown("""
<style>
.stApp{
    background:linear-gradient(135deg,#EEF2FF,#F8FAFC,#E0F2FE);
    color:#1E293B;
}
[data-testid="stMainBlockContainer"]{
    max-width:1500px;
    padding-top:2rem;
    padding-bottom:2rem;
}
h1{
    color:#172554!important;
    font-size:2.5rem!important;
    font-weight:800!important;
    letter-spacing:-1px;
}
.stApp p{
    line-height:1.6;
}
[data-testid="stVerticalBlockBorderWrapper"]{
    background:linear-gradient(145deg,#0F172A,#111C35,#172554);
    border:1px solid #334155;
    border-radius:18px;
    padding:14px;
    box-shadow:0 12px 35px rgba(15,23,42,.14);
}
[data-testid="stVerticalBlockBorderWrapper"] h2,
[data-testid="stVerticalBlockBorderWrapper"] h3{
    color:#F8FAFC!important;
    font-weight:700;
}
[data-testid="stVerticalBlockBorderWrapper"] p,
[data-testid="stVerticalBlockBorderWrapper"] label,
[data-testid="stVerticalBlockBorderWrapper"] [data-testid="stCaptionContainer"]{
    color:#CBD5E1!important;
}
[data-testid="stVerticalBlockBorderWrapper"] [data-testid="stVerticalBlockBorderWrapper"]{
    background:linear-gradient(145deg,#1E293B,#263449);
    border:1px solid #3B4B63;
    border-radius:14px;
    padding:12px;
    box-shadow:0 5px 15px rgba(0,0,0,.15);
}
[data-testid="stVerticalBlockBorderWrapper"] hr{
    border-color:#334155;
}
[data-testid="stSelectbox"] div[data-baseweb="select"]>div{
    background:#1E293B;
    color:#F8FAFC;
    border:1px solid #475569;
    border-radius:9px;
}
[data-testid="stRadio"] label,
[data-testid="stToggle"] label{
    color:#E2E8F0!important;
}
div[data-testid="stButton"] button{
    background:linear-gradient(135deg,#2563EB,#7C3AED);
    color:white;
    border:0;
    border-radius:9px;
    font-weight:600;
    transition:.2s;
}
div[data-testid="stButton"] button:hover{
    background:linear-gradient(135deg,#1D4ED8,#6D28D9);
    color:white;
    transform:translateY(-2px);
    box-shadow:0 5px 15px rgba(59,130,246,.3);
}
[data-testid="stPopover"] button{
    background:#263449;
    color:#E2E8F0;
    border:1px solid #475569;
    border-radius:9px;
}
[data-testid="stDataFrame"]{
    border:1px solid #334155;
    border-radius:12px;
    overflow:hidden;
}
[data-testid="stVegaLiteChart"]{
    background:#1E293B;
    border-radius:12px;
    padding:8px;
}
@media(max-width:768px){
    h1{font-size:1.8rem!important}
    [data-testid="stMainBlockContainer"]{padding:1rem}
}
</style>
""", unsafe_allow_html=True)

st.title("Build advanced dashboards")
st.text("Streamlit is built and tuned for demanding dashboards: KPI, product metrics, and operating dashboards with drill-down, cross-filtered views over large tables, live monitoring, and the dashboards a whole company relies on. Features that are hard to rebuild correctly in each app are solved once in the framework, and every release makes them faster.")
st.text("Because a dashboard is plain Python, it can also do what a report can't: run forecasts and models, call AI, and let people write decisions back. The query, the logic, and the number on screen sit side by side, so your data team can review every number.")
st.text("To see these features together, try the dashboard demo:")

with st.container(height=500,border=True):
    st.subheader("Overview")
    st.write("All regions · all plans · last 24 months")
    st.divider()
    c1,c2,c3=st.columns([3,2,3])
    with c1:
        time_period=st.radio("Time Period",["3M","6M","12M","24M"],horizontal=True,index=3)
    with c2:
        filter_type=st.selectbox("Filters",["Regions","Plans"])
    with c3:
        annotations=st.toggle("Annotations")
    st.divider()
    c1,c2,c3,c4=st.columns([5,1,1,1])
    with c1:
        st.subheader("Revenue")
    with c2:
        with st.popover("SQL"):
            st.code("""
SELECT month,
       SUM(mrr) * 12 AS arr,
       SUM(mrr) - LAG(SUM(mrr)) OVER (ORDER BY month) AS net_new_mrr
FROM revenue.mrr_monthly
WHERE region IN (:regions) AND plan IN (:plans)
GROUP BY month
ORDER BY month
""",language="sql")
    with c3:
        st.write("Live")
    with c4:
        st.button("Export")
    st.divider()

    data=pd.DataFrame({
        "Month":range(1,13),
        "Revenue":[10,15,13,20,18,25,22,30,28,35,32,40],
        "MRR":[20,25,18,30,22,35,28,40,32,45,38,50],
        "Retention":[90,95,92,100,98,105,103,110,108,115,112,120],
        "Growth":[5,8,6,10,7,12,9,15,11,18,14,20]
    })

    c1,c2,c3,c4=st.columns(4)
    with c1:
        with st.container(border=True):
            st.caption("Annual Revenue")
            st.subheader("$21.69M")
            st.write("+144.3%")
            st.line_chart(data,x="Month",y="Revenue",height=100,color=COLORS["primary"])
    with c2:
        with st.container(border=True):
            st.caption("Net New MRR")
            st.subheader("$37K")
            st.write("-17.7%")
            st.bar_chart(data,x="Month",y="MRR",height=100,color=COLORS["purple"])
    with c3:
        with st.container(border=True):
            st.caption("Net Revenue Retention")
            st.subheader("126.6%")
            st.write("+5.4 pts")
            st.line_chart(data,x="Month",y="Retention",height=100,color=COLORS["teal"])
    with c4:
        with st.container(border=True):
            st.caption("Monthly Growth")
            st.subheader("1.1%")
            st.write("-0.1 pts")
            st.bar_chart(data,x="Month",y="Growth",height=100,color=COLORS["peach"])

    st.divider()
    st.subheader("MRR by Plan")
    st.caption("Monthly recurring revenue, stacked by plan")
    np.random.seed(10)
    chart_data=pd.DataFrame({
        "Month":pd.date_range(start="2024-12-01",periods=24,freq="MS"),
        "Enterprise":np.linspace(450,950,24)+np.random.randint(0,40,24),
        "Pro":np.linspace(200,550,24)+np.random.randint(0,30,24),
        "Starter":np.linspace(120,280,24)+np.random.randint(0,20,24)
    })
    long_data=chart_data.melt(id_vars="Month",var_name="Plan",value_name="Revenue")
    area_chart=alt.Chart(long_data).mark_area(opacity=.85).encode(
        x=alt.X("Month:T",title=None),
        y=alt.Y("Revenue:Q",stack="zero",title="Revenue ($K)"),
        color=alt.Color("Plan:N",scale=alt.Scale(
            domain=["Enterprise","Pro","Starter"],
            range=[COLORS["primary"],COLORS["purple"],COLORS["green"]]
        ),legend=alt.Legend(orient="top",title=None)),
        tooltip=[
            alt.Tooltip("Month:T",title="Month"),
            alt.Tooltip("Plan:N",title="Plan"),
            alt.Tooltip("Revenue:Q",title="Revenue",format=".1f")
        ]
    ).properties(height=350,background="#1E293B")
    st.altair_chart(area_chart,use_container_width=True)

    st.divider()
    st.subheader("MRR Bridge")
    st.caption("How MRR moved over the last 24 months")
    bridge_data=pd.DataFrame({
        "Category":["Start","New","Expand","Contract","Churn","End"],
        "Value":[740,642,544,-32,-86,1808],
        "Type":["MRR","Gain","Gain","Loss","Loss","MRR"],
        "Lower":[0,740,1382,1894,1808,0],
        "Upper":[740,1382,1926,1926,1894,1808],
        "Label":["$740K","$642K","$544K","-$32K","-$86K","$1.81M"]
    })
    waterfall=alt.Chart(bridge_data).mark_bar(size=55).encode(
        x=alt.X("Category:N",sort=None,title=None),
        y=alt.Y("Lower:Q",scale=alt.Scale(domain=[0,2100]),title=None),
        y2="Upper:Q",
        color=alt.Color("Type:N",scale=alt.Scale(
            domain=["MRR","Gain","Loss"],
            range=[COLORS["primary"],COLORS["green"],COLORS["peach"]]
        ),legend=alt.Legend(orient="top",title=None)),
        tooltip=[
            alt.Tooltip("Category:N",title="Category"),
            alt.Tooltip("Value:Q",title="MRR Change",format=",.0f"),
            alt.Tooltip("Type:N",title="Type")
        ]
    )
    labels=alt.Chart(bridge_data).mark_text(dy=-10,fontSize=12,color="#F8FAFC").encode(
        x=alt.X("Category:N",sort=None),
        y=alt.Y("Upper:Q"),
        text="Label:N"
    )
    st.altair_chart((waterfall+labels).properties(height=350,background="#1E293B"),use_container_width=True)

    st.divider()
    st.subheader("When customers use Nimbus")
    st.caption("Product sessions by weekday and hour (UTC) — shifts with the region filter")
    days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    hours=[f"{h:02d}:00" for h in range(24)]
    np.random.seed(10)
    heatmap_data=[]
    for day in days:
        for hour in range(24):
            sessions=150+hour*15+np.random.randint(0,100)
            if day in ["Sat","Sun"]:
                sessions=int(sessions*.25)
            if hour<6:
                sessions=int(sessions*.5)
            if day=="Wed" and hour==7:
                sessions=522
            heatmap_data.append({"Day":day,"Hour":hours[hour],"Sessions":sessions})
    df_heatmap=pd.DataFrame(heatmap_data)
    heatmap=alt.Chart(df_heatmap).mark_rect(cornerRadius=3).encode(
        x=alt.X("Hour:N",sort=hours,title=None,axis=alt.Axis(values=hours[::2],labelAngle=0)),
        y=alt.Y("Day:N",sort=days,title=None),
        color=alt.Color("Sessions:Q",scale=alt.Scale(range=["#172554","#1D4ED8","#38BDF8"]),
            legend=alt.Legend(title=None,orient="bottom",gradientLength=275,gradientThickness=12)),
        tooltip=[
            alt.Tooltip("Day:N",title="Day"),
            alt.Tooltip("Hour:N",title="Time (UTC)"),
            alt.Tooltip("Sessions:Q",title="Sessions")
        ]
    ).properties(height=250,background="#1E293B")
    st.altair_chart(heatmap,use_container_width=True)

    st.divider()
    st.subheader("Revenue by industry")
    st.caption("Click a slice to filter the accounts")
    industry_data=pd.DataFrame({
        "Industry":["Fintech","Healthcare","Retail","Manufacturing","Media","Logistics"],
        "Revenue":[350,320,250,180,400,310]
    })
    industry_select=alt.selection_point(name="industry_select",fields=["Industry"],on="click",clear="dblclick")
    donut=alt.Chart(industry_data).mark_arc(innerRadius=85,outerRadius=145,cornerRadius=5,padAngle=.03).encode(
        theta=alt.Theta("Revenue:Q",stack=True),
        color=alt.Color("Industry:N",scale=alt.Scale(range=[
            "#38BDF8","#8B5CF6","#10B981","#F97316","#EC4899","#14B8A6"
        ]),legend=alt.Legend(title=None,orient="bottom")),
        opacity=alt.condition(industry_select,alt.value(1),alt.value(.8)),
        tooltip=[
            alt.Tooltip("Industry:N",title="Industry"),
            alt.Tooltip("Revenue:Q",title="Revenue",format=",.0f")
        ]
    ).add_params(industry_select)
    center_text=alt.Chart(pd.DataFrame({"Text":["$1.81M"]})).mark_text(
        fontSize=26,fontWeight="bold",color="#F8FAFC",dy=-10
    ).encode(text="Text:N")
    center_subtitle=alt.Chart(pd.DataFrame({"Subtitle":["MRR"]})).mark_text(
        fontSize=13,color="#38BDF8",dy=22
    ).encode(text="Subtitle:N")
    final_donut=(donut+center_text+center_subtitle).properties(height=400,background="#1E293B")
    chart_event=st.altair_chart(final_donut,use_container_width=True,on_select="rerun",selection_mode="industry_select")
    selected=chart_event.selection.get("industry_select",[])
    if selected:
        selected_industry=selected[0]["Industry"]
        st.write("Selected industry:",selected_industry)
        filtered_data=industry_data[industry_data["Industry"]==selected_industry]
        st.dataframe(filtered_data,hide_index=True)
    else:
        st.caption("Select an industry slice to view its revenue.")

    st.divider()
    st.subheader("Top accounts")
    st.caption("Largest customers by MRR")
    accounts=pd.DataFrame({
        "View":["View"]*10,
        "Account":["Fjordline Bio","Umbra Labs","Tidewater Foods","Basalt Foods","Evergreen Logistics","Keystone Analytics","Tidewater Health","Driftwood Foods","Evergreen Labs","Ionix Foods"],
        "Plan":["Enterprise"]*9+["Pro"],
        "MRR":[78810,78790,70460,52870,42430,40220,38830,37540,37490,34390],
        "Trend":[
            [20,25,28,35,40,45,52,60,65,72],
            [15,20,25,30,35,40,48,55,65,75],
            [40,38,35,40,45,48,55,60,68,72],
            [20,25,30,32,40,42,48,55,60,70],
            [80,75,70,65,65,60,62,60,55,50],
            [20,25,30,35,40,45,55,65,75,80],
            [30,32,35,40,45,50,55,60,58,55],
            [20,25,30,35,40,45,48,55,60,65],
            [25,30,35,40,45,50,55,60,65,70],
            [20,25,30,32,38,42,48,50,55,60]
        ],
        "Health":[85,95,56,99,37,99,42,59,99,71],
        "Renewal":["May 19, 2027","Sep 13, 2027","Jul 19, 2027","Jun 25, 2027","Dec 7, 2026","Nov 26, 2026","Aug 4, 2027","Oct 12, 2027","Feb 7, 2027","Nov 23, 2026"]
    })
    accounts["MRR"]=accounts["MRR"].apply(lambda x:f"${x:,.0f}")

    def health_bar(value):
        filled=round(value/10)
        return "■"*filled+"□"*(10-filled)+f" {value}"

    accounts["Health"]=accounts["Health"].apply(health_bar)
    st.dataframe(
        accounts,
        use_container_width=True,
        hide_index=True,
        height=420,
        column_config={
            "View":st.column_config.TextColumn("View",width="small"),
            "Account":st.column_config.TextColumn("Account",width="small"),
            "Plan":st.column_config.TextColumn("Plan",width="small"),
            "MRR":st.column_config.TextColumn("MRR",width="small"),
            "Trend":st.column_config.LineChartColumn("Trend",width="small",y_min=0,y_max=100,color="#38BDF8"),
            "Health":st.column_config.TextColumn("Health",width="small"),
            "Renewal":st.column_config.TextColumn("Renewal",width="small")
        }
    )
