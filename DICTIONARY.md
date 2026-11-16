# Data Dictionary

Source: [AACT (Aggregate Analysis of ClinicalTrials.gov)](https://aact.ctti-clinicaltrials.org/)

## baseline_counts

Sample sizes at baseline for each study group

Source file: `baseline_counts.txt`
Rows: 243,638

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| count | BIGINT | 0.0% | 56 |  |
| scope | VARCHAR | 0.0% | overall |  |
| units | VARCHAR | 0.0% | Participants |  |
| ctgov_group_code | VARCHAR | 0.0% | BG000 |  |
| result_group_id | BIGINT | 0.0% | 924251050 | Joins to result_groups.id |
| nct_id | VARCHAR | 0.0% | NCT05454813 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 102612132 | Table primary key (auto-increment) |

## baseline_measurements

Demographic and baseline measures by group

Source file: `baseline_measurements.txt`
Rows: 3,010,313

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| calculate_percentage | BOOLEAN | 96.5% | false |  |
| population_description | VARCHAR | 94.1% | Patient groups analysed seperately This was requested as per comments from re... |  |
| number_analyzed_units | VARCHAR | 0.0% | Participants |  |
| number_analyzed | BIGINT | 0.1% | 81 |  |
| explanation_of_na | VARCHAR | 99.8% | Only 1 participant was treated in this arm |  |
| dispersion_upper_limit | DOUBLE | 97.8% | 67.5 |  |
| dispersion_lower_limit | DOUBLE | 97.8% | 50.3 |  |
| dispersion_value_num | DOUBLE | 89.4% | 10.3 |  |
| dispersion_value | VARCHAR | 89.3% | 10.3 |  |
| dispersion_type | VARCHAR | 87.1% | STANDARD_DEVIATION |  |
| param_value_num | DOUBLE | 0.3% | 40.3 |  |
| param_value | VARCHAR | 0.1% | 40.3 |  |
| param_type | VARCHAR | 0.0% | MEAN |  |
| units | VARCHAR | 0.0% | years |  |
| description | VARCHAR | 90.1% | Each group was analyzed separately |  |
| title | VARCHAR | 0.0% | Age, Continuous |  |
| category | VARCHAR | 35.3% | Female |  |
| classification | VARCHAR | 74.6% | Age |  |
| ctgov_group_code | VARCHAR | 0.1% | BG000 |  |
| result_group_id | BIGINT | 0.1% | 922466733 | Joins to result_groups.id |
| nct_id | VARCHAR | 0.0% | NCT01189201 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 1202413460 | Table primary key (auto-increment) |

## brief_summaries

Brief text summary of the study protocol

Source file: `brief_summaries.txt`
Rows: 610,773

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| description | VARCHAR | 0.0% | ACT-MBC prospectively assesses the impact of CTCs on treatment decisions, res... |  |
| nct_id | VARCHAR | 0.0% | NCT05662345 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 252386545 | Table primary key (auto-increment) |

## browse_conditions

NLM-generated MeSH terms for study conditions

Source file: `browse_conditions.txt`
Rows: 4,429,716

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| mesh_type | VARCHAR | 0.0% | mesh-ancestor |  |
| downcase_mesh_term | VARCHAR | 0.0% | postoperative complications |  |
| mesh_term | VARCHAR | 0.0% | Postoperative Complications |  |
| nct_id | VARCHAR | 0.0% | NCT05920382 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 1783486722 | Table primary key (auto-increment) |

## browse_interventions

NLM-generated MeSH terms for study interventions

Source file: `browse_interventions.txt`
Rows: 2,578,978

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| mesh_type | VARCHAR | 0.0% | mesh-ancestor |  |
| downcase_mesh_term | VARCHAR | 0.0% | stilbenes |  |
| mesh_term | VARCHAR | 0.0% | Stilbenes |  |
| nct_id | VARCHAR | 0.0% | NCT00003424 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 945582986 | Table primary key (auto-increment) |

## calculated_values

AACT-computed fields: months to report results, facilities count, etc.

Source file: `calculated_values.txt`
Rows: 611,764

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| number_of_other_outcomes_to_measure | BIGINT | 91.3% | 1 |  |
| number_of_secondary_outcomes_to_measure | BIGINT | 27.2% | 2 |  |
| number_of_primary_outcomes_to_measure | BIGINT | 2.9% | 1 |  |
| maximum_age_unit | VARCHAR | 46.9% | year |  |
| minimum_age_unit | VARCHAR | 6.5% | year |  |
| maximum_age_num | BIGINT | 46.9% | 90 |  |
| minimum_age_num | BIGINT | 6.5% | 50 |  |
| has_single_facility | BOOLEAN | 10.0% | true |  |
| has_us_facility | BOOLEAN | 10.0% | true |  |
| months_to_report_results | BIGINT | 86.8% | 12 |  |
| were_results_reported | BOOLEAN | 0.0% | false |  |
| actual_duration | BIGINT | 38.6% | 2 |  |
| nlm_download_date | VARCHAR | 100.0% |  |  |
| registered_in_calendar_year | BIGINT | 0.0% | 2023 |  |
| number_of_sae_subjects | BIGINT | 93.0% | 10 |  |
| number_of_nsae_subjects | BIGINT | 90.9% | 93 |  |
| number_of_facilities | BIGINT | 0.0% | 1 |  |
| nct_id | VARCHAR | 0.0% | NCT06033066 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 276024359 | Table primary key (auto-increment) |

## central_contacts

Primary and backup contacts for enrollment questions

Source file: `central_contacts.txt`
Rows: 228,050

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| role | VARCHAR | 0.0% | CONTACT |  |
| phone_extension | VARCHAR | 88.6% | 475241 |  |
| email | VARCHAR | 2.3% | binan_email@163.com |  |
| phone | VARCHAR | 6.1% | 8613520445135 |  |
| name | VARCHAR | 0.0% | Nan Bi, Doctor |  |
| contact_type | VARCHAR | 0.0% | primary |  |
| nct_id | VARCHAR | 0.0% | NCT04014465 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 96461319 | Table primary key (auto-increment) |

## conditions

Disease or condition names studied in each trial

Source file: `conditions.txt`
Rows: 1,102,470

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| downcase_name | VARCHAR | 0.0% | chronic venous insufficiency |  |
| name | VARCHAR | 0.0% | Chronic Venous Insufficiency |  |
| nct_id | VARCHAR | 0.0% | NCT04054440 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 447582954 | Table primary key (auto-increment) |

## countries

Countries where the study has sites

Source file: `countries.txt`
Rows: 827,485

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| removed | BOOLEAN | 0.0% | true |  |
| name | VARCHAR | 0.0% | United States |  |
| nct_id | VARCHAR | 0.0% | NCT00511173 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 346937429 | Table primary key (auto-increment) |

## design_group_interventions

Cross-reference mapping design groups to interventions

Source file: `design_group_interventions.txt`
Rows: 1,365,520

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| intervention_id | BIGINT | 0.0% | 428833229 | Joins to interventions.id |
| design_group_id | BIGINT | 0.0% | 477297120 | Joins to design_groups.id |
| nct_id | VARCHAR | 0.0% | NCT05598957 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 565212326 | Table primary key (auto-increment) |

## design_groups

Protocol-specified groups or cohorts assigned to interventions

Source file: `design_groups.txt`
Rows: 1,126,933

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| description | VARCHAR | 11.8% | 8 sessions of psychotherapy designed to augment reward anticipation, reward a... |  |
| title | VARCHAR | 0.0% | Positive Affect Treatment |  |
| group_type | VARCHAR | 15.5% | EXPERIMENTAL |  |
| nct_id | VARCHAR | 0.0% | NCT06488859 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 477292335 | Table primary key (auto-increment) |

## design_outcomes

Planned outcome measures and observations

Source file: `design_outcomes.txt`
Rows: 3,835,719

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| description | VARCHAR | 17.3% | Measured in score points. The COEQ is a self-reported measure assessing vario... |  |
| population | VARCHAR | 100.0% |  |  |
| time_frame | VARCHAR | 1.4% | Baseline to week 24 |  |
| measure | VARCHAR | 0.0% | Change in control of eating questionnaire (COEQ), 4 domains: craving control ... |  |
| outcome_type | VARCHAR | 0.0% | secondary |  |
| nct_id | VARCHAR | 0.0% | NCT06267092 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 1558803043 | Table primary key (auto-increment) |

## designs

Study design details: allocation, masking, assignment, purpose

Source file: `designs.txt`
Rows: 606,958

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| outcomes_assessor_masked | BOOLEAN | 67.4% | false |  |
| investigator_masked | BOOLEAN | 67.4% | true |  |
| caregiver_masked | BOOLEAN | 67.4% | true |  |
| subject_masked | BOOLEAN | 67.4% | true |  |
| intervention_model_description | VARCHAR | 84.6% | Parallel Assignment |  |
| masking_description | VARCHAR | 92.1% | Statistician. |  |
| masking | VARCHAR | 24.0% | NONE |  |
| time_perspective | VARCHAR | 76.9% | PROSPECTIVE |  |
| primary_purpose | VARCHAR | 24.2% | PREVENTION |  |
| observational_model | VARCHAR | 77.4% | OTHER |  |
| intervention_model | VARCHAR | 24.2% | SINGLE_GROUP |  |
| allocation | VARCHAR | 24.0% | NA |  |
| nct_id | VARCHAR | 0.0% | NCT04545047 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 250758579 | Table primary key (auto-increment) |

## detailed_descriptions

Detailed text description of the study protocol

Source file: `detailed_descriptions.txt`
Rows: 610,773

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| description | VARCHAR | 32.8% | A bioequivalence study of Eltrombopag will be developed in 30 healthy subject... |  |
| nct_id | VARCHAR | 0.0% | NCT06834451 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 252778200 | Table primary key (auto-increment) |

## documents

Full study protocol and statistical analysis plan

Source file: `documents.txt`
Rows: 10,879

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| comment | VARCHAR | 14.0% | For additional information about this study please refer to the GSK Clinical ... |  |
| url | VARCHAR | 0.0% | https://www.clinicalstudydatarequest.com |  |
| document_type | VARCHAR | 0.0% | Informed Consent Form |  |
| document_id | VARCHAR | 15.6% | DIX110434 | Joins to documents.id |
| nct_id | VARCHAR | 0.0% | NCT00551564 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 4800296 | Table primary key (auto-increment) |

## drop_withdrawals

Summary of participant withdrawals: counts and reasons

Source file: `drop_withdrawals.txt`
Rows: 609,877

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| count_units | VARCHAR | 100.0% |  |  |
| reason_comment | VARCHAR | 100.0% |  |  |
| drop_withdraw_comment | VARCHAR | 100.0% |  |  |
| count | BIGINT | 0.0% | 84 |  |
| reason | VARCHAR | 0.0% | Death |  |
| period | VARCHAR | 0.0% | Overall Study |  |
| ctgov_group_code | VARCHAR | 0.0% | FG000 |  |
| result_group_id | BIGINT | 0.0% | 924120467 | Joins to result_groups.id |
| nct_id | VARCHAR | 0.0% | NCT03391466 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 251627558 | Table primary key (auto-increment) |

## eligibilities

Participant eligibility criteria (inclusion/exclusion, age, sex)

Source file: `eligibilities.txt`
Rows: 610,773

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| older_adult | BOOLEAN | 0.0% | true |  |
| child | BOOLEAN | 0.0% | false |  |
| adult | BOOLEAN | 0.0% | true |  |
| gender_based | BOOLEAN | 96.7% | true |  |
| gender_description | VARCHAR | 97.8% | Biologically female patients only |  |
| criteria | VARCHAR | 0.0% | Inclusion Criteria:~* Participant is willing and able to give informed consen... |  |
| population | VARCHAR | 77.3% | STN (Parkinson's disease) GPi (movement disorder, control) VIM (movement diso... |  |
| healthy_volunteers | BOOLEAN | 2.3% | false |  |
| maximum_age | VARCHAR | 46.8% | 80 Years |  |
| minimum_age | VARCHAR | 6.3% | 18 Years |  |
| gender | VARCHAR | 0.1% | ALL |  |
| sampling_method | VARCHAR | 77.3% | PROBABILITY_SAMPLE |  |
| nct_id | VARCHAR | 0.0% | NCT04058457 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 252811119 | Table primary key (auto-increment) |

## facilities

Facility names, addresses, and recruiting status

Source file: `facilities.txt`
Rows: 3,562,767

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| longitude | DOUBLE | 2.5% | 116.39723 |  |
| latitude | DOUBLE | 2.5% | 39.9075 |  |
| country | VARCHAR | 0.0% | China |  |
| zip | VARCHAR | 19.1% | 100044 |  |
| state | VARCHAR | 39.1% | Beijing Municipality |  |
| city | VARCHAR | 0.0% | Beijing |  |
| name | VARCHAR | 6.2% | Peking University People's Hospital |  |
| status | VARCHAR | 85.4% | RECRUITING |  |
| nct_id | VARCHAR | 0.0% | NCT05084599 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 1536117867 | Table primary key (auto-increment) |

## facility_contacts

Contact information at each study facility

Source file: `facility_contacts.txt`
Rows: 426,291

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| phone_extension | VARCHAR | 94.5% | 8426 |  |
| phone | VARCHAR | 26.9% | +390630155414 |  |
| email | VARCHAR | 27.2% | charlotte.usselman@mcgill.ca |  |
| name | VARCHAR | 3.4% | Charlotte Usselman, Ph.D |  |
| contact_type | VARCHAR | 0.0% | primary |  |
| facility_id | BIGINT | 0.0% | 1535823817 | Joins to facilities.id |
| nct_id | VARCHAR | 0.0% | NCT06155708 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 192715823 | Table primary key (auto-increment) |

## facility_investigators

Investigator names at each study facility

Source file: `facility_investigators.txt`
Rows: 229,550

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| name | VARCHAR | 0.0% | Hani Ashamalla, M.D. |  |
| role | VARCHAR | 0.0% | PRINCIPAL_INVESTIGATOR |  |
| facility_id | BIGINT | 0.0% | 1535746618 | Joins to facilities.id |
| nct_id | VARCHAR | 0.0% | NCT05134779 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 104149453 | Table primary key (auto-increment) |

## id_information

Identifiers other than NCT ID (org study IDs, secondary IDs)

Source file: `id_information.txt`
Rows: 808,976

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| id_link | VARCHAR | 92.9% | https://reporter.nih.gov/quickSearch/R01HL046974 |  |
| id_type_description | VARCHAR | 89.2% | Eli Lilly and Company |  |
| id_type | VARCHAR | 79.6% | OTHER |  |
| id_value | VARCHAR | 0.0% | J4G-OX-JZVB |  |
| id_source | VARCHAR | 0.0% | secondary_id |  |
| nct_id | VARCHAR | 0.0% | NCT06644378 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 330383652 | Table primary key (auto-increment) |

## intervention_other_names

Synonymous names for interventions

Source file: `intervention_other_names.txt`
Rows: 491,652

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| name | VARCHAR | 0.0% | AT-527 is also know as R07496998 |  |
| intervention_id | BIGINT | 0.0% | 428385375 | Joins to interventions.id |
| nct_id | VARCHAR | 0.0% | NCT05137626 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 212250112 | Table primary key (auto-increment) |

## interventions

Interventions or exposures: drugs, devices, procedures, vaccines

Source file: `interventions.txt`
Rows: 1,035,096

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| description | VARCHAR | 8.8% | Subjects will receive single doses of 1,3,6,30,100,200, 400 mg of PF-06260414... |  |
| name | VARCHAR | 0.0% | Anagrelide |  |
| intervention_type | VARCHAR | 0.0% | DRUG |  |
| nct_id | VARCHAR | 0.0% | NCT01065038 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 428509940 | Table primary key (auto-increment) |

## ipd_information_types

Individual participant data sharing information types

Source file: `ipd_information_types.txt`
Rows: 99,070

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| name | VARCHAR | 0.0% | STUDY_PROTOCOL |  |
| nct_id | VARCHAR | 0.0% | NCT05201521 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 37145936 | Table primary key (auto-increment) |

## keywords

Investigator-provided keywords describing the study

Source file: `keywords.txt`
Rows: 1,658,452

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| downcase_name | VARCHAR | 0.0% | meditation |  |
| name | VARCHAR | 0.0% | meditation |  |
| nct_id | VARCHAR | 0.0% | NCT00600561 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 665449843 | Table primary key (auto-increment) |

## links

Web links relevant to the study

Source file: `links.txt`
Rows: 77,438

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| description | VARCHAR | 0.0% | UI Health Islet Cell Transplant |  |
| url | VARCHAR | 0.0% | https://hospital.uillinois.edu/primary-and-specialty-care/transplantation-pro... |  |
| nct_id | VARCHAR | 0.0% | NCT00679042 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 32850698 | Table primary key (auto-increment) |

## milestones

Participant progress through each stage of the study

Source file: `milestones.txt`
Rows: 910,983

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| count_units | VARCHAR | 97.8% | 2 |  |
| milestone_description | VARCHAR | 96.5% | Subjects that completed 2 test days (40%mg ethanol \& 100%mg ethanol) |  |
| count | BIGINT | 0.0% | 43 |  |
| description | VARCHAR | 100.0% |  |  |
| period | VARCHAR | 0.0% | Overall Study |  |
| title | VARCHAR | 0.0% | STARTED |  |
| ctgov_group_code | VARCHAR | 0.0% | FG000 |  |
| result_group_id | BIGINT | 0.0% | 923328497 | Joins to result_groups.id |
| nct_id | VARCHAR | 0.0% | NCT05970991 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 370720401 | Table primary key (auto-increment) |

## outcome_analyses

Statistical analyses performed on outcomes

Source file: `outcome_analyses.txt`
Rows: 330,580

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| p_value_raw | VARCHAR | 18.4% | 0.94896 |  |
| ci_lower_limit_raw | VARCHAR | 36.2% | 0.86 |  |
| ci_upper_limit_raw | VARCHAR | 36.4% | 1.16 |  |
| other_analysis_description | VARCHAR | 98.8% | Mean difference and CI come from a linear regression model adjusting for entr... |  |
| groups_description | VARCHAR | 41.5% | An analysis of covariance (ANCOVA) model with treatment and as a factor and t... |  |
| estimate_description | VARCHAR | 78.1% | Geometric means |  |
| method_description | VARCHAR | 81.0% | ANOVA based on rank transformation. |  |
| method | VARCHAR | 14.9% | Log Rank |  |
| p_value_description | VARCHAR | 71.4% | Mixed Model Analysis has treatment, baseline, time point, and treatment by ti... |  |
| ci_upper_limit_na_comment | VARCHAR | 100.0% | The upper limit of the 95% confidence interval = 13124060000000000000000000000 |  |
| ci_upper_limit | DOUBLE | 36.4% | 1.16 |  |
| ci_lower_limit | DOUBLE | 36.3% | 0.86 |  |
| ci_percent | DOUBLE | 30.5% | 95.0 |  |
| ci_n_sides | VARCHAR | 32.6% | TWO_SIDED |  |
| p_value | DOUBLE | 18.4% | 0.94896 |  |
| p_value_modifier | VARCHAR | 79.6% | < |  |
| dispersion_value | DOUBLE | 81.5% | 0.07 |  |
| dispersion_type | VARCHAR | 81.5% | STANDARD_ERROR_OF_MEAN |  |
| param_value | DOUBLE | 30.8% | 1.0 |  |
| param_type | VARCHAR | 30.8% | Hazard Ratio (HR) |  |
| non_inferiority_description | VARCHAR | 85.6% | Accuracy identifying taught verbs in syntactic vs semantic condition (receptive) |  |
| non_inferiority_type | VARCHAR | 0.0% | SUPERIORITY_OR_OTHER |  |
| outcome_id | BIGINT | 0.0% | 284014649 | Joins to outcomes.id |
| nct_id | VARCHAR | 0.0% | NCT00762034 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 141396001 | Table primary key (auto-increment) |

## outcome_analysis_groups

Groups involved in each outcome analysis

Source file: `outcome_analysis_groups.txt`
Rows: 639,703

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| ctgov_group_code | VARCHAR | 0.0% | OG002 |  |
| result_group_id | BIGINT | 0.0% | 923805437 | Joins to result_groups.id |
| outcome_analysis_id | BIGINT | 0.0% | 141526676 | Joins to outcome_analyses.id |
| nct_id | VARCHAR | 0.0% | NCT00428090 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 274193519 | Table primary key (auto-increment) |

## outcome_counts

Sample sizes for each outcome by study group

Source file: `outcome_counts.txt`
Rows: 1,632,111

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| count | BIGINT | 0.0% | 10 |  |
| units | VARCHAR | 0.0% | Participants |  |
| scope | VARCHAR | 0.0% | Measure |  |
| ctgov_group_code | VARCHAR | 0.0% | OG000 |  |
| result_group_id | BIGINT | 0.0% | 923275535 | Joins to result_groups.id |
| outcome_id | BIGINT | 0.0% | 284105576 | Joins to outcomes.id |
| nct_id | VARCHAR | 0.0% | NCT03853707 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 682814331 | Table primary key (auto-increment) |

## outcome_measurements

Summary data for outcome measures by study group

Source file: `outcome_measurements.txt`
Rows: 5,071,872

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| dispersion_lower_limit_raw | VARCHAR | 82.6% | 1.65 |  |
| dispersion_upper_limit_raw | VARCHAR | 82.7% | 3.00 |  |
| explanation_of_na | VARCHAR | 98.0% | Data for range was not collected, because analysis of median changes from bas... |  |
| dispersion_upper_limit | DOUBLE | 83.4% | 3.0 |  |
| dispersion_lower_limit | DOUBLE | 83.0% | 1.65 |  |
| dispersion_value_num | DOUBLE | 64.8% | 3.21 |  |
| dispersion_value | VARCHAR | 63.8% | 3.21 |  |
| dispersion_type | VARCHAR | 46.8% | Standard Error |  |
| param_value_num | DOUBLE | 1.1% | 0.0 |  |
| param_value | VARCHAR | 0.0% | 0 |  |
| param_type | VARCHAR | 0.0% | COUNT_OF_PARTICIPANTS |  |
| units | VARCHAR | 0.0% | Participants |  |
| description | VARCHAR | 4.5% | An adverse event (AE) is any untoward medical occurrence in a clinical study ... |  |
| title | VARCHAR | 0.0% | Number of Participants With Treatment-emergent Adverse Events (TEAEs) and Ser... |  |
| category | VARCHAR | 92.7% | Strongly Agree |  |
| classification | VARCHAR | 19.7% | Participants with Serious TEAEs |  |
| ctgov_group_code | VARCHAR | 0.0% | OG002 |  |
| result_group_id | BIGINT | 0.0% | 922963505 | Joins to result_groups.id |
| outcome_id | BIGINT | 0.0% | 284012592 | Joins to outcomes.id |
| nct_id | VARCHAR | 0.0% | NCT04571385 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 2119373245 | Table primary key (auto-increment) |

## outcomes

Outcome measure descriptions and time frames

Source file: `outcomes.txt`
Rows: 675,682

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| param_type | VARCHAR | 7.2% | MEAN |  |
| dispersion_type | VARCHAR | 39.2% | 95% Confidence Interval |  |
| units_analyzed | VARCHAR | 98.0% | eyes |  |
| units | VARCHAR | 7.2% | mmol/L |  |
| anticipated_posting_month_year | VARCHAR | 99.1% | 2025-12 |  |
| anticipated_posting_date | DATE | 99.1% | 2025-12-01 |  |
| population | VARCHAR | 24.8% | ITT population included all randomized participants. |  |
| time_frame | VARCHAR | 0.0% | baseline |  |
| description | VARCHAR | 7.3% | PFS was defined as the time from randomization to the first documented PD as ... |  |
| title | VARCHAR | 0.0% | The Fasting Plasma Glucose Value, Baseline |  |
| outcome_type | VARCHAR | 0.0% | PRIMARY |  |
| nct_id | VARCHAR | 0.0% | NCT00425269 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 284155683 | Table primary key (auto-increment) |

## overall_officials

People responsible for overall scientific leadership

Source file: `overall_officials.txt`
Rows: 538,952

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| affiliation | VARCHAR | 0.5% | Aristotle University |  |
| name | VARCHAR | 0.0% | Nikoleta Printza |  |
| role | VARCHAR | 0.3% | PRINCIPAL_INVESTIGATOR |  |
| nct_id | VARCHAR | 0.0% | NCT03964701 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 231186512 | Table primary key (auto-increment) |

## participant_flows

Recruitment and pre-assignment details

Source file: `participant_flows.txt`
Rows: 81,026

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| units_analyzed | VARCHAR | 98.2% | teeth |  |
| pre_assignment_details | VARCHAR | 60.8% | A total of 108 participants were enrolled in the study and randomized. The st... |  |
| recruitment_details | VARCHAR | 59.5% | This 32-week, randomized, double-blind, placebo-controlled study assessed the... |  |
| nct_id | VARCHAR | 0.0% | NCT03716076 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 33499619 | Table primary key (auto-increment) |

## pending_results

Events related to submission of results for QC review

Source file: `pending_results.txt`
Rows: 34,116

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| event_date | DATE | 1.2% | 2019-08-06 |  |
| event_date_description | DATE | 1.2% | 2019-08-06 |  |
| event | VARCHAR | 0.0% | RELEASE |  |
| nct_id | VARCHAR | 0.0% | NCT03559504 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 14279927 | Table primary key (auto-increment) |

## provided_documents

Protocol, SAP, and informed consent form documents

Source file: `provided_documents.txt`
Rows: 88,167

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| url | VARCHAR | 0.0% | https://ClinicalTrials.gov/ProvidedDocs/59/NCT05295459/Prot_002.pdf |  |
| document_date | DATE | 0.0% | 2024-03-29 |  |
| has_sap | BOOLEAN | 0.0% | false |  |
| has_icf | BOOLEAN | 0.0% | false |  |
| has_protocol | BOOLEAN | 0.0% | true |  |
| document_type | VARCHAR | 0.0% | Study Protocol |  |
| nct_id | VARCHAR | 0.0% | NCT05295459 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 32413515 | Table primary key (auto-increment) |

## reported_event_totals

Totals of reported adverse events by category

Source file: `reported_event_totals.txt`
Rows: 612,225

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| updated_at | TIMESTAMP | 0.0% | 2026-11-15 23:30:22.737358 |  |
| created_at | TIMESTAMP | 0.0% | 2026-11-15 23:30:22.737358 |  |
| subjects_at_risk | BIGINT | 11.8% | 22 |  |
| subjects_affected | BIGINT | 11.6% | 0 |  |
| classification | VARCHAR | 0.0% | Total, all-cause mortality |  |
| event_type | VARCHAR | 0.0% | deaths |  |
| ctgov_group_code | VARCHAR | 0.0% | EG000 |  |
| nct_id | VARCHAR | 0.0% | NCT01328717 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 250641334 | Table primary key (auto-increment) |

## reported_events

Summary of reported adverse events

Source file: `reported_events.txt`
Rows: 12,253,285

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| assessment | VARCHAR | 2.1% | SYSTEMATIC_ASSESSMENT |  |
| vocab | VARCHAR | 11.0% | MedDRA 25.1 |  |
| frequency_threshold | BIGINT | 0.0% | 5 |  |
| adverse_event_term | VARCHAR | 0.0% | Bacterial infection |  |
| organ_system | VARCHAR | 0.0% | Infections and infestations |  |
| event_count | BIGINT | 56.1% | 2 |  |
| description | VARCHAR | 32.6% | All randomized participants who received at least 1 dose of investigational p... |  |
| subjects_at_risk | BIGINT | 0.0% | 13 |  |
| subjects_affected | BIGINT | 0.8% | 1 |  |
| default_assessment | VARCHAR | 100.0% |  |  |
| default_vocab | VARCHAR | 100.0% |  |  |
| event_type | VARCHAR | 0.0% | other |  |
| time_frame | VARCHAR | 11.7% | Baseline up to Week 200 |  |
| ctgov_group_code | VARCHAR | 0.0% | EG014 |  |
| result_group_id | BIGINT | 0.0% | 923006582 | Joins to result_groups.id |
| nct_id | VARCHAR | 0.0% | NCT03428100 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 639985305 | Table primary key (auto-increment) |

## responsible_parties

Parties responsible for submitting study information

Source file: `responsible_parties.txt`
Rows: 593,336

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| old_name_title | VARCHAR | 95.7% | MSD |  |
| affiliation | VARCHAR | 56.7% | The Hospital for Sick Children |  |
| organization | VARCHAR | 95.8% | AstraZeneca |  |
| title | VARCHAR | 56.7% | Principal Investigator |  |
| name | VARCHAR | 56.7% | Glenda Courtney-Martin |  |
| responsible_party_type | VARCHAR | 4.3% | SPONSOR |  |
| nct_id | VARCHAR | 0.0% | NCT01822782 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 251722975 | Table primary key (auto-increment) |

## result_agreements

Agreements between sponsor and principal investigators about results

Source file: `result_agreements.txt`
Rows: 81,026

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| restrictive_agreement | BOOLEAN | 23.5% | false |  |
| other_details | VARCHAR | 72.8% | Authorship/contents of any publication is determined by site and provides spo... |  |
| restriction_type | VARCHAR | 62.3% | OTHER |  |
| agreement | VARCHAR | 100.0% |  |  |
| pi_employee | BOOLEAN | 0.0% | true |  |
| nct_id | VARCHAR | 0.0% | NCT05313555 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 34361017 | Table primary key (auto-increment) |

## result_contacts

Points of contact for scientific information about results

Source file: `result_contacts.txt`
Rows: 81,026

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| extension | VARCHAR | 94.7% | 4973 |  |
| email | VARCHAR | 6.0% | anu@scuhs.edu |  |
| phone | VARCHAR | 4.4% | 866-435-7343 |  |
| name | VARCHAR | 0.0% | GSK Response Center |  |
| organization | VARCHAR | 0.0% | GlaxoSmithKline |  |
| nct_id | VARCHAR | 0.0% | NCT01390857 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 34409802 | Table primary key (auto-increment) |

## result_groups

Aggregate list of group titles/descriptions for results reporting

Source file: `result_groups.txt`
Rows: 2,249,303

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| outcome_id | BIGINT | 28.7% | 284492003 | Joins to outcomes.id |
| description | VARCHAR | 0.8% | 50 mL normal saline solution~Normal saline solution: 50 mL normal saline once... |  |
| title | VARCHAR | 0.0% | Control Arm |  |
| result_type | VARCHAR | 0.0% | Outcome |  |
| ctgov_group_code | VARCHAR | 0.0% | OG000 |  |
| nct_id | VARCHAR | 0.0% | NCT02322892 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 924561343 | Table primary key (auto-increment) |

## retractions

Retraction notices for study results or publications

Source file: `retractions.txt`
Rows: 335

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| nct_id | VARCHAR | 0.0% | NCT06369948 | Primary trial identifier, joins across all AACT tables |
| source | VARCHAR | 0.0% | J Clin Anesth. 2022 Aug;79:110722 |  |
| pmid | BIGINT | 0.0% | 35393178 |  |
| reference_id | BIGINT | 0.0% | 474307191 |  |
| id | BIGINT | 0.0% | 151758 | Table primary key (auto-increment) |

## search_term_results

Source file: `search_term_results.txt`
Rows: 520,437

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| updated_at | TIMESTAMP | 0.0% | 2026-11-16 05:31:20.213059 |  |
| created_at | TIMESTAMP | 0.0% | 2026-11-16 05:31:20.213029 |  |
| search_term_id | BIGINT | 0.0% | 45 |  |
| nct_id | VARCHAR | 0.0% | NCT00001191 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 316822502 | Table primary key (auto-increment) |

## search_terms

Source file: `search_terms.txt`
Rows: 186

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| updated_at | TIMESTAMP | 0.0% | 2025-01-28 21:03:58.475729 |  |
| created_at | TIMESTAMP | 0.0% | 2025-01-28 21:03:58.475729 |  |
| group | VARCHAR | 0.0% | diseases of the heart |  |
| term | VARCHAR | 0.0% | rheumatic fever without mention of heart involvement |  |
| id | BIGINT | 0.0% | 1 | Table primary key (auto-increment) |

## sponsors

Sponsor and collaborator names and types

Source file: `sponsors.txt`
Rows: 974,504

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| name | VARCHAR | 0.0% | The eNose Company |  |
| lead_or_collaborator | VARCHAR | 0.0% | collaborator |  |
| agency_class | VARCHAR | 0.1% | INDUSTRY |  |
| nct_id | VARCHAR | 0.0% | NCT02765087 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 416131944 | Table primary key (auto-increment) |

## studies

Core study record: title, status, phase, type, dates, enrollment, and regulatory info

Source file: `studies.txt`
Rows: 611,764

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| patient_registry | BOOLEAN | 80.7% | false |  |
| baseline_type_units_analyzed | VARCHAR | 99.9% | Hospitalizations |  |
| fdaaa801_violation | VARCHAR | 100.0% | t |  |
| expanded_access_status_for_nctid | VARCHAR | 99.9% | APPROVED_FOR_MARKETING |  |
| expanded_access_nctid | VARCHAR | 99.9% | NCT03079687 |  |
| delayed_posting | BOOLEAN | 99.8% | true |  |
| source_class | VARCHAR | 0.2% | OTHER |  |
| updated_at | TIMESTAMP | 0.0% | 2026-11-15 03:38:51.198997 |  |
| created_at | TIMESTAMP | 0.0% | 2026-11-15 03:38:51.198997 |  |
| plan_to_share_ipd_description | VARCHAR | 84.6% | De-identified individual participant data underlying the results reported in ... |  |
| plan_to_share_ipd | VARCHAR | 46.7% | YES |  |
| ipd_url | VARCHAR | 97.8% | https://mail.google.com/mail/u/0/?fs=1&tf=cm&source=mailto&to=empower@ualbert... |  |
| ipd_access_criteria | VARCHAR | 94.8% | Available to qualified researchers upon reasonable request, subject to review... |  |
| ipd_time_frame | VARCHAR | 94.4% | Beginning 3 months after publication, with no end date |  |
| biospec_description | VARCHAR | 95.4% | Exhaled samples |  |
| biospec_retention | VARCHAR | 95.4% | SAMPLES_WITHOUT_DNA |  |
| is_us_export | BOOLEAN | 87.9% | false |  |
| is_ppsd | VARCHAR | 100.0% | t |  |
| is_unapproved_device | BOOLEAN | 99.1% | true |  |
| is_fda_regulated_device | BOOLEAN | 36.6% | false |  |
| is_fda_regulated_drug | BOOLEAN | 36.6% | false |  |
| has_dmc | BOOLEAN | 17.7% | false |  |
| expanded_access_type_treatment | BOOLEAN | 100.0% | true |  |
| expanded_access_type_intermediate | BOOLEAN | 100.0% | true |  |
| expanded_access_type_individual | BOOLEAN | 99.9% | true |  |
| has_expanded_access | BOOLEAN | 1.2% | false |  |
| why_stopped | VARCHAR | 92.2% | The study was stopped earlier than anticipated due to slow accrual |  |
| number_of_groups | BIGINT | 84.5% | 2 |  |
| number_of_arms | BIGINT | 27.6% | 3 |  |
| limitations_and_caveats | VARCHAR | 97.2% | Our study is limited by a small sample size, and further multicenter analyses... |  |
| source | VARCHAR | 0.0% | University of Alberta |  |
| enrollment_type | VARCHAR | 2.8% | ACTUAL |  |
| enrollment | BIGINT | 1.2% | 825 |  |
| phase | VARCHAR | 23.7% | NA |  |
| last_known_status | VARCHAR | 83.9% | RECRUITING |  |
| overall_status | VARCHAR | 0.0% | COMPLETED |  |
| official_title | VARCHAR | 1.6% | Evidence Based Mental Wellness Programming Online for Adults Across Chronic P... |  |
| brief_title | VARCHAR | 0.0% | Evidence Based Mental Wellness Programming Online for Adults Across Chronic P... |  |
| baseline_population | VARCHAR | 95.5% | Demographics data was only collected for participants who completed the study. |  |
| acronym | VARCHAR | 70.8% | EMPOwer |  |
| study_type | VARCHAR | 0.2% | INTERVENTIONAL |  |
| target_duration | VARCHAR | 97.0% | 2 Months |  |
| primary_completion_date | DATE | 3.6% | 2024-09-22 |  |
| primary_completion_date_type | VARCHAR | 3.6% | ACTUAL |  |
| primary_completion_month_year | VARCHAR | 3.6% | 2024-09-22 |  |
| completion_date | DATE | 2.7% | 2024-12-01 |  |
| completion_date_type | VARCHAR | 3.8% | ACTUAL |  |
| completion_month_year | VARCHAR | 2.7% | 2024-12-01 |  |
| verification_date | DATE | 0.2% | 2026-05-31 |  |
| verification_month_year | VARCHAR | 0.2% | 2026-05 |  |
| start_date | DATE | 0.9% | 2023-02-12 |  |
| start_date_type | VARCHAR | 30.4% | ACTUAL |  |
| start_month_year | VARCHAR | 0.9% | 2023-02-12 |  |
| last_update_posted_date_type | VARCHAR | 0.0% | ACTUAL |  |
| last_update_posted_date | DATE | 0.0% | 2026-05-08 |  |
| last_update_submitted_qc_date | DATE | 0.0% | 2026-05-04 |  |
| disposition_first_posted_date_type | VARCHAR | 98.4% | ESTIMATED |  |
| disposition_first_posted_date | DATE | 98.4% | 2016-02-05 |  |
| disposition_first_submitted_qc_date | DATE | 98.7% | 2016-01-06 |  |
| results_first_posted_date_type | VARCHAR | 86.8% | ACTUAL |  |
| results_first_posted_date | DATE | 86.8% | 2022-06-21 |  |
| results_first_submitted_qc_date | DATE | 86.8% | 2022-05-24 |  |
| study_first_posted_date_type | VARCHAR | 0.0% | ACTUAL |  |
| study_first_posted_date | DATE | 0.0% | 2023-03-27 |  |
| study_first_submitted_qc_date | DATE | 0.0% | 2023-03-24 |  |
| last_update_submitted_date | DATE | 0.0% | 2026-05-04 |  |
| disposition_first_submitted_date | DATE | 98.4% | 2016-01-06 |  |
| results_first_submitted_date | DATE | 86.8% | 2022-01-06 |  |
| study_first_submitted_date | DATE | 0.0% | 2023-03-09 |  |
| nlm_download_date_description | VARCHAR | 100.0% |  |  |
| nct_id | VARCHAR | 0.0% | NCT05786482 | Primary trial identifier, joins across all AACT tables |

## study_references

Citations to publications related to the study

Source file: `study_references.txt`
Rows: 1,158,770

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| citation | VARCHAR | 0.0% | Amrein K, Schnedl C, Holl A, Riedl R, Christopher KB, Pachler C, Urbanic Purk... |  |
| reference_type | VARCHAR | 0.0% | BACKGROUND |  |
| pmid | BIGINT | 5.1% | 25268295 |  |
| nct_id | VARCHAR | 0.0% | NCT03188796 | Primary trial identifier, joins across all AACT tables |
| id | BIGINT | 0.0% | 473722780 | Table primary key (auto-increment) |
