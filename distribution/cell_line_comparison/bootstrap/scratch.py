JHH7_0uM_bootstrap_dict = perform_bootstrap(dataframe=df, cell_line='JHH7_0uM')
JHH7_0uM_bootstrap_df = pd.DataFrame.from_dict(JHH7_0uM_bootstrap_dict)
JHH7_0uM_bootstrap_df = JHH7_0uM_bootstrap_df.reset_index(drop=True)

sns.displot(JHH7_0uM_bootstrap_df, kind="kde", bw_adjust=.3,
            height=5, aspect=15/8).set(title='JHH7_0uM with bootstrap')

JHH7_1uM_bootstrap_dict = perform_bootstrap(dataframe=df, cell_line='JHH7_1uM')
JHH7_1uM_bootstrap_df = pd.DataFrame.from_dict(JHH7_1uM_bootstrap_dict)
JHH7_1uM_bootstrap_df = JHH7_1uM_bootstrap_df.reset_index(drop=True)

sns.displot(JHH7_1uM_bootstrap_df, kind="kde", bw_adjust=.3,
            height=5, aspect=15/8).set(title='JHH7_1uM with bootstrap')

JHH7_2uM_bootstrap_dict = perform_bootstrap(dataframe=df, cell_line='JHH7_2.5uM')
JHH7_2uM_bootstrap_df = pd.DataFrame.from_dict(JHH7_2uM_bootstrap_dict)
JHH7_2uM_bootstrap_df = JHH7_2uM_bootstrap_df.reset_index(drop=True)

sns.displot(JHH7_2uM_bootstrap_df, kind="kde", bw_adjust=.3,
            height=5, aspect=15/8).set(title='JHH7_2uM with bootstrap')