import React from 'react';
import type { Question } from 'src/types';
import { JsonLdProps } from './jsonld';
export interface QAPageJsonLdProps extends JsonLdProps {
    mainEntity: Question;
}
declare function QAPageJsonLd({ type, keyOverride, mainEntity, ...rest }: QAPageJsonLdProps): React.JSX.Element;
export default QAPageJsonLd;
